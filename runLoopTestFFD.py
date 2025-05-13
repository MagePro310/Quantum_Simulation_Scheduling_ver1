import sys
sys.path.append('./')
import json
import os
from qiskit import QuantumCircuit
import numpy as np
from dataclasses import dataclass
from enum import auto, Enum
import matplotlib.pyplot as plt
import math
from dataclasses import dataclass
from qiskit.visualization import plot_error_map
from component.a_backend.fake_backend import *
from component.b_benchmark.mqt_tool import benchmark_circuit, create_circuit
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import *
from component.d_scheduling.algorithm.ilp.MILQ_extend import MILQ_extend_implementation
from component.d_scheduling.extract import ilp
from component.d_scheduling.simulation.scheduling_multithread import simulate_scheduling as simulate_multithread
from component.d_scheduling.analyze import analyze_cal
from component.d_scheduling.datawork.visualize import visualize_data
from component.d_scheduling.datawork.updateToDict import update_scheduler_jobs
from component.f_assemble.assemble_work import fidelity_from_counts
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_distribution
from qiskit import transpile
from qiskit_ibm_runtime import SamplerV2
import time
from dataclasses import asdict
from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement


# Define Dataclass for ResultOfSchedule
@dataclass
class ResultOfSchedule:
    numcircuit: int
    nameAlgorithm: str
    averageQubits: float
    nameSchedule: str
    typeMachine: dict
    
    # Metrics
    average_turnaroundTime: float
    average_responseTime: float
    average_fidelity: float
    sampling_overhead: float
    average_throughput: float
    average_utilization: float
    scheduler_latency: float
    makespan: float

# Main quantum scheduling workflow in a loop
aer_simulator = AerSimulator()

# Loop to iterate over num_qubits_per_job from 1 to 10
for num_jobs in range(2, 10):
    for num_qubits_per_job in range(2, 11):  # Outer loop for num_qubits_per_job
        print(f"num_jobs: {num_jobs}, num_qubits_per_job: {num_qubits_per_job}")
        
        # Nested loop to repeat the process 10 times for each num_qubits_per_job
        
        # Initialize result_Schedule
        result_Schedule = ResultOfSchedule(
        numcircuit=0,
        nameAlgorithm="",
        averageQubits=0.0,
        nameSchedule="",
        typeMachine={},
        
        # Metrics
        average_turnaroundTime=0.0,
        average_responseTime=0.0,
        average_fidelity=0.0,
        sampling_overhead=0.0,
        average_throughput=0.0,
        average_utilization=0.0,
        scheduler_latency=0.0,
        makespan=0.0
        )
        result_Schedule.nameSchedule = "FFD"
        
        # Define the machines
        machines = {}
        backend0 = FakeBelemV2()
        backend1 = FakeManilaV2()
        machines[backend0.name] = backend0
        machines[backend1.name] = backend1
        
        # Define benchmark
        jobs = {}
        for i in range(num_jobs):
            job_id = str(i + 1)
            jobs[job_id] = num_qubits_per_job

        # Update info to result_Schedule
        result_Schedule.numcircuit = len(jobs)
        result_Schedule.averageQubits = sum(jobs.values()) / len(jobs)

        # Generate circuits
        origin_job_info = {}
        
        for job_name, num_qubits in jobs.items():
            circuit = create_circuit(num_qubits, job_name)
            result_Schedule.nameAlgorithm = "ghz"
            circuit.remove_final_measurements()
            origin_job_info[job_name] = JobInfo(
                job_name=job_name,
                qubits=circuit.num_qubits,
                machine=None,  # Placeholder for machine name
                capacity_machine=0,  # Placeholder for machine capacity
                start_time=0.0,  # Placeholder for start time
                duration=0.0,  # Placeholder for duration
                end_time=0.0,  # Placeholder for end time
                childrenJobs=None,  # Placeholder for child jobs
                circuit=circuit,
                result_cut=None,  # Placeholder for result cut
            )
    
        # Process job info and cut the circuits if needed
        process_job_info = origin_job_info.copy()
        
        max_width = max(list(machines.values()), key=lambda x: x.num_qubits).num_qubits
        for job_name, job_info in process_job_info.items():
            if job_info.qubits > max_width:
                job_info.childrenJobs = []
                cut_name, observable = greedy_cut(job_info.circuit, max_width)
                # print(observable)
                result_cut = gate_to_reduce_width(job_info.circuit, cut_name, observable)
                result_Schedule.sampling_overhead += result_cut.overhead
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

        # Prepare scheduler jobs
        scheduler_job = {}
        def get_scheduler_jobs(job_info):
            if job_info.childrenJobs is None:
                return {job_info.job_name: job_info}
            scheduler_jobs = {}
            for child_job in job_info.childrenJobs:
                scheduler_jobs.update(get_scheduler_jobs(child_job))
            return scheduler_jobs

        for job_name, job_info in process_job_info.items():
            scheduler_job.update(get_scheduler_jobs(job_info))

    # ============================= FFD Algorithm ==============================
        job_capacities_FFD = dict()
        job_capacities_FFD = {job_name: job_info.qubits for job_name, job_info in scheduler_job.items()}
        machine_capacities_FFD = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
        result_Schedule.typeMachine = machine_capacities_FFD
        outputFFD = "component/d_scheduling/scheduleResult/heuristic/FFD"
        start_time = time.time()
        FFD_implement.example_problem(job_capacities_FFD, machine_capacities_FFD, outputFFD)
        runtime = time.time() - start_time
        result_Schedule.scheduler_latency = runtime

        data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/heuristic/FFD/schedule.json")
        update_scheduler_jobs(data, scheduler_job)
    # ============================== FFD Algorithm ==============================

        for job_id, job in scheduler_job.items():
            backend = machines.get(job.machine)
            if backend:
                # Perform transpilation
                # job.circuit.data = [hasChange for hasChange in job.circuit.data if hasChange.operation.name != "qpd_1q"]
                job.transpiled_circuit = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                # job.circuit.measure_all()
                # job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
            else:
                print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
                
        jobs = data.copy()
        updated_jobs = simulate_multithread(jobs, scheduler_job)
        
        