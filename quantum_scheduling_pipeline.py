#!/usr/bin/env python3
"""
Quantum Scheduling Pipeline

A comprehensive quantum circuit scheduling and simulation framework that implements
the First Fit Decreasing (FFD) algorithm for quantum job scheduling across multiple
quantum backends. This pipeline includes circuit generation, cutting, scheduling,
knitting, and performance evaluation.

Author: Quantum Simulation Team
Version: 1.0.0
"""

import sys
import json
import os
import time
import logging
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# Qiskit imports
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2

# Component imports
sys.path.append('./')
# Import configuration and utilities
from config import PipelineConfig, SimulationMode, SchedulingAlgorithm
from component.utils import setup_logging, save_json

# Component imports
from component.sup_sys.algorithm_loader import load_algorithms
from component.a_backend.fake_backend import get_backend_by_name, get_available_backends
from component.b_benchmark.mqt_tool import QuantumBenchmark
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import WidthCircuitCutter
from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
from component.d_scheduling.analyze import analyze_cal
from component.d_scheduling.datawork.visualize import visualize_data
from component.d_scheduling.datawork.updateToDict import update_scheduler_jobs
from component.d_scheduling.simulation.scheduling_sim import simulate_scheduling
from component.c_circuit_work.knitting.width_k import merge_multiple_circuits
from component.f_assemble.assemble_work import fidelity_from_counts

# Set matplotlib to non-interactive backend for headless operation
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class SchedulingMetrics:
    """Data class to store all scheduling and performance metrics."""
    
    # Job configuration
    num_circuits: int
    algorithm_name: str
    average_qubits: float
    schedule_name: str
    machine_types: Dict[str, int]
    
    # Performance metrics
    average_turnaround_time: float
    average_response_time: float
    average_fidelity: float
    sampling_overhead: float
    average_throughput: float
    average_utilization: float
    scheduler_latency: float
    makespan: float
    
    def __init__(self):
        """Initialize all metrics to default values."""
        self.num_circuits = 0
        self.algorithm_name = ""
        self.average_qubits = 0.0
        self.schedule_name = "FFD"
        self.machine_types = {}
        
        # Performance metrics
        self.average_turnaround_time = 0.0
        self.average_response_time = 0.0
        self.average_fidelity = 0.0
        self.sampling_overhead = 0.0
        self.average_throughput = 0.0
        self.average_utilization = 0.0
        self.scheduler_latency = 0.0
        self.makespan = 0.0


class QuantumSchedulingPipeline:
    """
    Main pipeline class for quantum circuit scheduling and simulation.
    
    This class orchestrates the entire workflow from circuit generation
    to performance evaluation, providing a clean and modular interface.
    """
    
    def __init__(self, config: Optional[PipelineConfig] = None):
        """
        Initialize the quantum scheduling pipeline.
        
        Args:
            config: Pipeline configuration object
        """
        self.config = config or PipelineConfig()
        self.config.validate()
        
        self.num_qubits_per_job = self.config.num_qubits_per_job
        self.num_jobs = self.config.num_jobs
        self.metrics = SchedulingMetrics()
        self.machines = {}
        self.origin_job_info = {}
        self.scheduler_job = {}
        self.aer_simulator = AerSimulator()
        
        # Set up logging
        self.logger = setup_logging(self.config.log_level)
        self.logger.info(f"Initialized pipeline with {self.num_jobs} jobs of {self.num_qubits_per_job} qubits each")
    
    def setup_backends(self) -> None:
        """Initialize and configure quantum backends."""
        self.logger.info("Setting up quantum backends...")
        
        load_algorithms()
        backend_list = get_available_backends()
        self.logger.info(f"Available backends: {len(backend_list)} found")
        
        # Configure specified backends
        for backend_name in self.config.backend_names:
            try:
                backend = get_backend_by_name(backend_name)()
                self.machines[backend.name] = backend
            except Exception as e:
                self.logger.warning(f"Failed to load backend {backend_name}: {e}")
        
        if not self.machines:
            raise RuntimeError("No backends could be loaded")
        
        self.logger.info(f"Configured machines: {list(self.machines.keys())}")
    
    def generate_benchmark_circuits(self) -> None:
        """Generate benchmark quantum circuits for scheduling."""
        self.logger.info("Generating benchmark quantum circuits...")
        
        jobs = {}
        for i in range(self.num_jobs):
            job_id = str(i + 1)
            jobs[job_id] = self.num_qubits_per_job
        
        # Update metrics
        self.metrics.num_circuits = len(jobs)
        self.metrics.average_qubits = sum(jobs.values()) / len(jobs)
        
        # Generate circuits and job information
        for job_name, num_qubits in jobs.items():
            circuit, self.metrics.algorithm_name = QuantumBenchmark.create_circuit(
                num_qubits, job_name
            )
            
            self.origin_job_info[job_name] = JobInfo(
                job_name=job_name,
                qubits=circuit.num_qubits,
                machine=None,
                capacity_machine=0,
                start_time=0.0,
                duration=0.0,
                end_time=0.0,
                childrenJobs=None,
                circuit=circuit,
                result_cut=None,
            )
        
        self.logger.info(f"Generated {len(self.origin_job_info)} benchmark circuits")
    
    def perform_circuit_cutting(self) -> None:
        """Cut circuits that exceed maximum backend width."""
        if not self.config.enable_circuit_cutting:
            self.logger.info("Circuit cutting disabled, skipping...")
            self.scheduler_job = self.origin_job_info.copy()
            return
            
        self.logger.info("Performing circuit cutting...")
        
        max_width = max(
            list(self.machines.values()), 
            key=lambda x: x.num_qubits
        ).num_qubits
        
        process_job_info = self.origin_job_info.copy()
        
        for job_name, job_info in process_job_info.items():
            if job_info.qubits > max_width:
                self.logger.info(f"Cutting job {job_name} ({job_info.qubits} qubits > {max_width})")
                
                job_info.childrenJobs = []
                cutter = WidthCircuitCutter(job_info.circuit, max_width)
                result_cut = cutter.gate_to_reduce_width()
                
                self.metrics.sampling_overhead += result_cut.overhead
                
                for i, (subcircuit_name, subcircuit) in enumerate(result_cut.subcircuits.items()):
                    job_info.childrenJobs.append(
                        JobInfo(
                            job_name=f"{job_name}_{i+1}",
                            qubits=subcircuit.num_qubits,
                            machine=None,
                            capacity_machine=0,
                            start_time=0.0,
                            duration=0.0,
                            end_time=0.0,
                            childrenJobs=None,
                            circuit=subcircuit,
                            result_cut=None,
                        )
                    )
                job_info.result_cut = result_cut
        
        # Build scheduler job dictionary
        self.scheduler_job = {}
        for job_name, job_info in process_job_info.items():
            self.scheduler_job.update(self._get_scheduler_jobs(job_info))
        
        self.logger.info(f"Created {len(self.scheduler_job)} scheduler jobs after cutting")
    
    def _get_scheduler_jobs(self, job_info: JobInfo) -> Dict[str, JobInfo]:
        """Recursively extract scheduler jobs from job hierarchy."""
        if job_info.childrenJobs is None:
            return {job_info.job_name: job_info}
        
        scheduler_jobs = {}
        for child_job in job_info.childrenJobs:
            scheduler_jobs.update(self._get_scheduler_jobs(child_job))
        return scheduler_jobs
    
    def _save_gantt_chart(self, data: List[Dict], stage: str) -> Optional[str]:
        """
        Save Gantt chart with structured naming.
        
        Args:
            data: Job scheduling data
            stage: Pipeline stage ('scheduling' or 'simulation')
            
        Returns:
            Path to saved chart or None if saving is disabled
        """
        if not self.config.save_visualizations:
            return None
        
        # Ensure we have algorithm name, default to 'unknown' if not set
        algo_name = self.metrics.algorithm_name or 'unknown'
        
        # Create structured filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = (
            f"{self.metrics.schedule_name}_{algo_name}_"
            f"{self.metrics.num_circuits}jobs_{self.metrics.average_qubits:.0f}qubits_"
            f"{stage}_{timestamp}.pdf"
        )
        
        # Create gantt charts directory
        gantt_dir = os.path.join(
            "component", "finalResult", self.config.experiment_id, 
            self.config.gantt_chart_dir
        )
        os.makedirs(gantt_dir, exist_ok=True)
        
        save_path = os.path.join(gantt_dir, filename)
        
        # Check for existing files with similar pattern and remove them
        import glob
        pattern = (
            f"{self.metrics.schedule_name}_{algo_name}_"
            f"{self.metrics.num_circuits}jobs_{self.metrics.average_qubits:.0f}qubits_"
            f"{stage}_*.pdf"
        )
        existing_files = glob.glob(os.path.join(gantt_dir, pattern))
        
        for existing_file in existing_files:
            try:
                os.remove(existing_file)
                self.logger.info(f"Removed existing chart: {existing_file}")
            except OSError as e:
                self.logger.warning(f"Could not remove {existing_file}: {e}")
        
        try:
            # Create a copy of data to avoid modifying the original
            data_copy = [job.copy() for job in data]
            
            # Call visualization with custom parameters
            from component.d_scheduling.datawork.visualize import visualize_data
            visualize_data(data_copy, save_path=save_path, show_plot=self.config.show_plots)
            
            self.logger.info(f"Gantt chart saved to: {save_path}")
            return save_path
            
        except Exception as e:
            self.logger.warning(f"Failed to save Gantt chart: {e}")
            return None
    
    def execute_scheduling(self) -> List[Dict]:
        """Execute the FFD scheduling algorithm."""
        self.logger.info("Executing FFD scheduling algorithm...")
        
        job_capacities = {
            job_name: job_info.qubits 
            for job_name, job_info in self.scheduler_job.items()
        }
        machine_capacities = {
            machine_name: machine.num_qubits 
            for machine_name, machine in self.machines.items()
        }
        
        self.metrics.machine_types = machine_capacities
        output_path = "component/d_scheduling/scheduleResult/heuristic/FFD"
        
        # Measure scheduling time
        start_time = time.time()
        FFD_implement.example_problem(job_capacities, machine_capacities, output_path)
        self.metrics.scheduler_latency = time.time() - start_time
        
        # Load and process scheduling results
        data = analyze_cal.load_job_data(f"{output_path}/schedule.json")
        update_scheduler_jobs(data, self.scheduler_job)
        
        self.logger.info(f"Scheduling completed in {self.metrics.scheduler_latency:.3f} seconds")
        return data
    
    def transpile_circuits(self) -> None:
        """Transpile quantum circuits for their assigned backends."""
        self.logger.info("Transpiling circuits for assigned backends...")
        
        for job_id, job in self.scheduler_job.items():
            backend = self.machines.get(job.machine)
            if backend:
                # Remove unwanted operations and transpile
                job.circuit.data = [
                    gate for gate in job.circuit.data 
                    if gate.operation.name != "qpd_1q"
                ]
                job.transpiled_circuit = transpile(
                    job.circuit, 
                    backend, 
                    scheduling_method='alap', 
                    layout_method='trivial'
                )
            else:
                self.logger.warning(f"No backend found for machine {job.machine}, skipping job {job_id}")
    
    def run_simulation(self, data: List[Dict], mode: str = 'multi_threaded') -> List[Dict]:
        """
        Run the unified scheduling simulation.
        
        Args:
            data: Scheduling data
            mode: Simulation mode ('single_threaded' or 'multi_threaded')
            
        Returns:
            Updated job data after simulation
        """
        self.logger.info(f"Running scheduling simulation in {mode} mode...")
        
        jobs = data.copy()
        updated_jobs = simulate_scheduling(jobs, self.scheduler_job, mode=mode)
        
        self.logger.info(f"Simulation completed - processed {len(updated_jobs)} jobs")
        return updated_jobs
    
    def perform_circuit_knitting(self, updated_jobs: List[Dict]) -> None:
        """Knit circuits that run simultaneously on the same machine."""
        if not self.config.enable_circuit_knitting:
            self.logger.info("Circuit knitting disabled, skipping...")
            # Still need to prepare circuits for simulation
            for job_info in self.scheduler_job.values():
                job_info.knitted_circuit = job_info.circuit.copy()
                job_info.knitted_circuit.measure_all()
            return
            
        self.logger.info("Performing circuit knitting...")
        
        # Prepare circuit mapping
        job_circuits = {
            job_info.job_name: job_info.circuit 
            for job_info in self.scheduler_job.values()
        }
        
        # Group jobs by (machine, start_time)
        grouped_jobs = defaultdict(list)
        for job in updated_jobs:
            key = (job['machine'], job['start'])
            grouped_jobs[key].append(job['job'])
        
        # Merge circuits for concurrent execution
        expanded_circuits = {}
        for (machine, start_time), job_ids in grouped_jobs.items():
            circuits_to_merge = [job_circuits[job_id] for job_id in job_ids]
            
            if len(circuits_to_merge) == 1:
                merged_circuit = circuits_to_merge[0]
            else:
                merged_circuit = merge_multiple_circuits(circuits_to_merge)
            
            expanded_circuits[tuple(job_ids)] = merged_circuit
        
        # Assign knitted circuits and transpile with measurements
        for keys, circuit_expand in expanded_circuits.items():
            circuit_expand.measure_all()
            for key in keys:
                self.scheduler_job[key].knitted_circuit = circuit_expand
        
        # Transpile knitted circuits
        for job_id, job in self.scheduler_job.items():
            backend = self.machines.get(job.machine)
            if backend:
                job.transpiled_circuit_measured = transpile(
                    job.knitted_circuit, 
                    backend, 
                    scheduling_method='alap', 
                    layout_method='trivial'
                )
        
        self.logger.info("Circuit knitting completed")
    
    def run_quantum_simulation(self) -> None:
        """Execute quantum simulations and calculate fidelities."""
        self.logger.info("Running quantum simulations...")
        
        for job_name, job_info in self.scheduler_job.items():
            backend = self.machines.get(job_info.machine)
            
            if backend:
                transpiled_circuit = job_info.transpiled_circuit_measured
                
                # Run ideal simulation
                ideal_result = self.aer_simulator.run(transpiled_circuit, shots=self.config.shots).result()
                ideal_counts = ideal_result.get_counts(transpiled_circuit)
                
                # Run noisy simulation
                job = SamplerV2(backend).run([transpiled_circuit], shots=self.config.shots)
                sim_result = job.result()[0]
                sim_counts = sim_result.data.meas.get_counts()
                
                # Calculate fidelity
                fidelity_val, _, _ = fidelity_from_counts(ideal_counts, sim_counts)
                job_info.fidelity = fidelity_val
        
        self.logger.info("Quantum simulations completed")
    
    def calculate_metrics(self, data: List[Dict]) -> None:
        """Calculate comprehensive performance metrics."""
        self.logger.info("Calculating performance metrics...")
        
        utilization_per_machine = analyze_cal.calculate_utilization(data)
        
        # Update parent job metrics for cut circuits
        for job_name, job_info in self.origin_job_info.items():
            if job_info.childrenJobs is not None:
                count_fidelity = 0
                min_start = float('inf')
                max_end = 0
                
                for child_job in job_info.childrenJobs:
                    min_start = min(min_start, child_job.start_time)
                    max_end = max(max_end, child_job.end_time)
                    count_fidelity += child_job.fidelity * child_job.qubits
                
                job_info.start_time = min_start
                job_info.end_time = max_end
                job_info.duration = max_end - min_start
                job_info.fidelity = count_fidelity / job_info.qubits
        
        # Calculate system-wide metrics
        metrics = analyze_cal.calculate_metrics(data, utilization_per_machine)
        
        self.metrics.average_turnaround_time = metrics['average_turnaround_time']
        self.metrics.average_response_time = metrics['average_response_time']
        self.metrics.makespan = metrics['makespan']
        self.metrics.average_utilization = metrics['average_utilization']
        self.metrics.average_throughput = metrics['throughput']
        
        # Calculate weighted average fidelity
        sum_fidelity = sum(
            job_info.fidelity * job_info.qubits 
            for job_info in self.origin_job_info.values()
        )
        self.metrics.average_fidelity = sum_fidelity / (
            self.metrics.average_qubits * self.metrics.num_circuits
        )
        
        self.logger.info("Metrics calculation completed")
        self._print_metrics(metrics)
    
    def _print_metrics(self, metrics: Dict) -> None:
        """Print formatted metrics summary."""
        print("\n" + "="*60)
        print("QUANTUM SCHEDULING PERFORMANCE METRICS")
        print("="*60)
        print(f"Algorithm: {self.metrics.schedule_name}")
        print(f"Benchmark: {self.metrics.algorithm_name}")
        print(f"Circuits: {self.metrics.num_circuits}")
        print(f"Average Qubits: {self.metrics.average_qubits:.1f}")
        print(f"Machines: {list(self.metrics.machine_types.keys())}")
        print("-"*60)
        print(f"Scheduler Latency: {self.metrics.scheduler_latency:.3f}s")
        print(f"Makespan: {self.metrics.makespan:.3f}s")
        print(f"Average Turnaround Time: {self.metrics.average_turnaround_time:.3f}s")
        print(f"Average Response Time: {self.metrics.average_response_time:.3f}s")
        print(f"Average Throughput: {self.metrics.average_throughput:.3f} jobs/s")
        print(f"Average Utilization: {self.metrics.average_utilization:.3f}")
        print(f"Average Fidelity: {self.metrics.average_fidelity:.4f}")
        print(f"Sampling Overhead: {self.metrics.sampling_overhead:.3f}")
        print("="*60)
    
    def save_results(self, experiment_id: Optional[str] = None) -> str:
        """
        Save results to JSON file with unique naming.
        
        Args:
            experiment_id: Identifier for the experiment series
            
        Returns:
            Path to the saved file
        """
        self.logger.info("Saving results to JSON...")
        
        exp_id = experiment_id or self.config.experiment_id
        
        # Create directory structure
        algorithm_folder_path = os.path.join(
            "component", "finalResult", exp_id, 
            self.metrics.schedule_name, self.metrics.algorithm_name
        )
        os.makedirs(algorithm_folder_path, exist_ok=True)
        
        # Generate unique filename
        base_filename = f"{self.metrics.num_circuits}_{self.metrics.average_qubits}"
        existing_files = os.listdir(algorithm_folder_path)
        matching_files = [
            f for f in existing_files 
            if f.startswith(base_filename) and f.endswith(".json")
        ]
        
        if not matching_files:
            final_filename = f"{base_filename}_0.json"
        else:
            suffixes = []
            for f in matching_files:
                suffix_str = f.replace(base_filename, "").replace(".json", "").replace("_", "")
                if suffix_str.isdigit():
                    suffixes.append(int(suffix_str))
            
            next_suffix = max(suffixes, default=0) + 1
            final_filename = f"{base_filename}_{next_suffix}.json"
        
        # Save results
        output_file_path = os.path.join(algorithm_folder_path, final_filename)
        with open(output_file_path, "w") as f:
            json.dump(asdict(self.metrics), f, indent=4)
        
        self.logger.info(f"Results saved to {output_file_path}")
        return output_file_path
    
    def run_complete_pipeline(self, experiment_id: Optional[str] = None) -> str:
        """
        Execute the complete quantum scheduling pipeline.
        
        Args:
            experiment_id: Experiment identifier for result storage
            
        Returns:
            Path to the saved results file
        """
        self.logger.info("Starting complete quantum scheduling pipeline...")
        
        try:
            # Execute pipeline stages
            self.setup_backends()
            self.generate_benchmark_circuits()
            self.perform_circuit_cutting()
            
            scheduling_data = self.execute_scheduling()
            self._save_gantt_chart(scheduling_data, "scheduling")
            
            self.transpile_circuits()
            
            updated_jobs = self.run_simulation(scheduling_data, self.config.simulation_mode.value)
            self._save_gantt_chart(updated_jobs, "simulation")
            
            self.perform_circuit_knitting(updated_jobs)
            self.run_quantum_simulation()
            self.calculate_metrics(updated_jobs)
            
            result_path = self.save_results(experiment_id)
            
            self.logger.info("Pipeline execution completed successfully!")
            return result_path
            
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {str(e)}")
            raise


def main():
    """Main execution function with example usage."""
    # Example configuration
    config = PipelineConfig(
        num_qubits_per_job=7,
        num_jobs=2,
        simulation_mode=SimulationMode.MULTI_THREADED,
        experiment_id="5_5"
    )
    
    # Create and run pipeline
    pipeline = QuantumSchedulingPipeline(config)
    
    result_file = pipeline.run_complete_pipeline()
    
    print(f"\n✅ Pipeline completed successfully!")
    print(f"📊 Results saved to: {result_file}")


if __name__ == "__main__":
    main()
