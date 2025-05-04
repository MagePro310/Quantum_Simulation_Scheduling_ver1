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
from component.b_benchmark.mqt_tool import benchmark_circuit
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import *
from component.d_scheduling.algorithm.ilp.MILQ_extend import MILQ_extend_implementation
from component.d_scheduling.extract import ilp
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
from component.d_scheduling.algorithm.heuristic.MTMC import MTMC_implement


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
    time_generation: float
    makespan: float

# Main quantum scheduling workflow in a loop
aer_simulator = AerSimulator()

for num_jobs in range(2, 10):
    print(f"Running for num_jobs = {num_jobs}")
    # Loop to iterate over num_qubits_per_job from 1 to 10
    for num_qubits_per_job in range(2, 11):  # Outer loop for num_qubits_per_job
        print(f"Running for num_qubits_per_job = {num_qubits_per_job}")
        
        # Nested loop to repeat the process 10 times for each num_qubits_per_job
        
        # Initialize result_Schedule
        result_Schedule = ResultOfSchedule(
            numcircuit=0,
            nameAlgorithm="",
            averageQubits=0.0,
            nameSchedule="",
            typeMachine={},
            average_turnaroundTime=0.0,
            average_responseTime=0.0,
            average_fidelity=0.0,
            sampling_overhead=0.0,
            average_throughput=0.0,
            average_utilization=0.0,
            time_generation=0.0,
            makespan=0.0
        )
        
        # Define the machines
        machines = {}
        backend0 = FakeBelemV2()
        backend1 = FakeManilaV2()
        machines[backend0.name] = backend0
        machines[backend1.name] = backend1
        

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
            circuit = benchmark_circuit(name_algorithm="ghz", circuit_size=num_qubits)
            result_Schedule.nameAlgorithm = "ghz"
            circuit.remove_final_measurements()
            origin_job_info[job_name] = JobInfo(
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

        # Process job info and cut the circuits if needed
        process_job_info = origin_job_info.copy()
        max_width = max(list(machines.values()), key=lambda x: x.num_qubits).num_qubits
        for job_name, job_info in process_job_info.items():
            if job_info.qubits > max_width:
                job_info.childrenJobs = []
                cut_name, observable = greedy_cut(job_info.circuit, max_width)
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
        result_Schedule.nameSchedule = "MTMC"
        job_capacities_MTMC = dict()
        job_capacities_MTMC = {job_name: job_info.qubits for job_name, job_info in scheduler_job.items()}
        machine_capacities_MTMC = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
        result_Schedule.typeMachine = machine_capacities_MTMC
        start_time = time.time()
        outputMTMC = "component/d_scheduling/scheduleResult/heuristic/MTMC"
        MTMC_implement.example_problem(job_capacities_MTMC, machine_capacities_MTMC, outputMTMC)
        runtime = time.time() - start_time
        result_Schedule.time_generation = runtime
    # ============================== FFD Algorithm ==============================

        data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/heuristic/MTMC/schedule.json")
        # data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/ilp/MILQ_extend/schedule.json")
        update_scheduler_jobs(data, scheduler_job)

        # Transpile circuits for all scheduled jobs
        for job_id, job in scheduler_job.items():
            backend = machines.get(job.machine)
            if backend:
                job.circuit.data = [hasChange for hasChange in job.circuit.data if hasChange.operation.name != "qpd_1q"]
                job.transpiled_circuit = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                job.circuit.measure_all()
                job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                
        for job_name, job_info in scheduler_job.items():
            backend = machines.get(job_info.machine)
            
            if backend:
                transpiled_circuit = job_info.transpiled_circuit_measured
                
                # Run the ideal simulation
                ideal_result = aer_simulator.run(transpiled_circuit, shots=1024).result()
                ideal_counts = ideal_result.get_counts(transpiled_circuit)
                
                # Run circuit on the simulated backend
                job = SamplerV2(backend).run([transpiled_circuit], shots=1024)
                sim_result = job.result()[0]
                sim_counts = sim_result.data.meas.get_counts()
                
                # Calculate fidelity
                fidelity_val, rho_ideal, rho_sim = fidelity_from_counts(ideal_counts, sim_counts)
                
                # Store the fidelity values
                job_info.fidelity = fidelity_val

        # Define the jobs
        jobs = data.copy()

        # Generate unique execution times
        def get_the_duration_from_transpiled_circuit(circuit):
            return circuit.duration

        # Simulate the scheduling with parallel execution support
        def simulate_scheduling(jobs):
            machine_schedules = {'fake_belem': [], 'fake_manila': []}  # Track active jobs for each machine
            jobs = sorted(jobs, key=lambda x: x['start'])  # Sort jobs by start time
            for job in jobs:
                machine = job['machine']
                # base_duration = job['duration']
                unique_duration = get_the_duration_from_transpiled_circuit(scheduler_job[job['job']].transpiled_circuit)

                # Find the earliest time the job can start
                current_schedule = machine_schedules[machine]
                start_time = job['start']
                
                # Check for parallel execution
                while True:
                    # Filter out completed jobs
                    active_jobs = [j for j in current_schedule if j['end'] > start_time]
                    
                    # Calculate total qubits in use
                    total_qubits_in_use = sum(j['qubits'] for j in active_jobs)
                    if total_qubits_in_use + job['qubits'] <= job['capacity']:
                        # Enough resources are available
                        break
                    # Increment start_time to the earliest end time of active jobs
                    start_time = min(j['end'] for j in active_jobs)

                # Update job start, end times, and duration
                job['start'] = start_time
                job['end'] = start_time + unique_duration
                job['duration'] = unique_duration

                # Add job to the machine's schedule
                current_schedule.append(job)

            return jobs

        # Run the simulation
        updated_jobs = simulate_scheduling(jobs)
        print("Updated jobs after scheduling:")
        print(updated_jobs)
        # Simulate the scheduling for updated jobs
        utilization_permachine = analyze_cal.calculate_utilization(data)
        for job_name, job_info in origin_job_info.items():
            if job_info.childrenJobs is not None:
                count_fidelity = 0
                for child_job in job_info.childrenJobs:
                    job_info.start_time = min(job_info.start_time, child_job.start_time)
                    job_info.end_time = max(job_info.end_time, child_job.end_time)
                    job_info.duration = job_info.end_time - job_info.start_time
                    count_fidelity += child_job.fidelity * child_job.qubits
                job_info.fidelity = count_fidelity / job_info.qubits
            else:
                print(f"Job {job_name} has no children jobs.")
        
        # Update metrics in result_Schedule
        metrics = analyze_cal.calculate_metrics(data, utilization_permachine)
        result_Schedule.average_turnaroundTime = metrics['average_turnaroundTime']
        result_Schedule.average_responseTime = metrics['average_responseTime']
        result_Schedule.makespan = metrics['makespan']
        result_Schedule.average_utilization = metrics['average_utilization']
        result_Schedule.average_throughput = metrics['throughput']

        # for job_name, job_info in origin_job_info.items():
        #     job_info.print()
        
        sum_fidelity = 0
        for job_name, job_info in origin_job_info.items():
            sum_fidelity += job_info.fidelity * job_info.qubits
        average_fidelity = sum_fidelity / (result_Schedule.averageQubits * result_Schedule.numcircuit)
        result_Schedule.average_fidelity = average_fidelity

        # Save results to a JSON file
        algorithm_folder_path = os.path.join("component", "finalResult", "5_5", result_Schedule.nameSchedule, result_Schedule.nameAlgorithm)
        os.makedirs(algorithm_folder_path, exist_ok=True)
        output_file_path = os.path.join(algorithm_folder_path, f"{num_jobs}_{num_qubits_per_job}.0_0.json")
        with open(output_file_path, "w") as f:
            json.dump(asdict(result_Schedule), f, indent=4)

        print(f"Result saved for num_qubits_per_job = {num_qubits_per_job}, run at {output_file_path}")