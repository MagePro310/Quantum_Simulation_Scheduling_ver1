import sys
sys.path.append('./')
import json
import os
from qiskit import QuantumCircuit
import numpy as np
from dataclasses import dataclass, asdict
from enum import auto, Enum
import matplotlib.pyplot as plt
import math
from component.d_scheduling.algorithm.ilp.NoTODS.NoTODS import *

from dataclasses import dataclass
from component.a_backend.fake_backend import *

from component.b_benchmark.mqt_tool import benchmark_circuit
from component.sup_sys.job_info import JobInfo

from component.c_circuit_work.cutting.width_c import *
from component.d_scheduling.analyze import analyze_cal
import json

from qiskit import QuantumCircuit, transpile

from qiskit_aer import AerSimulator
from qiskit.visualization import plot_distribution
import qiskit.quantum_info as qi
from qiskit import transpile
from qiskit_ibm_runtime import SamplerV2
from component.f_assemble.assemble_work import fidelity_from_counts

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

aer_simulator = AerSimulator()
for num_jobs in range(2, 10):
    for num_qubits_per_job in range(2, 11):  # Outer loop for num_qubits_per_job
        print(f"Running for num_qubits_per_job = {num_qubits_per_job}")
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
        
        # Define the machines
        machines = {}
        backend0 = FakeBelemV2()
        backend1 = FakeManilaV2()
        machines[backend0.name] = backend0
        machines[backend1.name] = backend1
        
        # num_qubits_per_job = 6
        jobs = {}

        for i in range(num_jobs):
            job_id = str(i + 1)
            jobs[job_id] = num_qubits_per_job

        # update numcircuit
        result_Schedule.numcircuit = len(jobs)
        result_Schedule.averageQubits = sum(jobs.values()) / len(jobs)
        
        origin_job_info = {}

        for job_name, num_qubits in jobs.items():
            circuit = benchmark_circuit(name_algorithm="ghz", circuit_size=num_qubits)
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

        process_job_info = origin_job_info.copy()
        
        backendlist = list(machines.values())
        Tau = [200]*len(backendlist)
        print("Tau: ", Tau) 
        print(backendlist)
        obj_dict = {}
        for job_name, job in process_job_info.items():
            obj_dict[job_name] = NoTODS(job.circuit, backendlist, Tau)

        machine_capacity = {}
        machine_capacity = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
        result_Schedule.typeMachine = machine_capacity
        print(obj_dict)
        
        subcircuit_dict = {}
        sum_overhead = 0
        for obj_name, obj in obj_dict.items():
            subcircuit_dict[obj_name], overhead_item  = obj_dict[obj_name]._cut_circuit()
            sum_overhead += overhead_item
            process_job_info[obj_name].childrenJobs = []
            for i, subcircuit_item in enumerate(subcircuit_dict[obj_name]['subcircuits']):
                process_job_info[obj_name].childrenJobs.append(
                    JobInfo(
                        job_name=f"{obj_name}_{i+1}",
                        qubits=subcircuit_item.num_qubits,
                        machine=None,
                        capacity_machine=0,
                        start_time=0.0,
                        duration=0.0,
                        end_time=0.0,
                        childrenJobs=None,
                        circuit=subcircuit_item,
                        result_cut=None,
                    )
                )

        for job in process_job_info.values():
            job.print()
        result_Schedule.sampling_overhead = sum_overhead
        
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
            
        print("Scheduler Jobs:")
        for job_name, job_info in scheduler_job.items():
            job_info.print()
            
        result_Schedule.nameSchedule = "NoTODS"
        import time
        start_time = time.time()

        model = {}
        for obj_name, obj in obj_dict.items():
            model[obj_name] = obj.schedule(subcircuit_dict[obj_name])
        run_time = time.time() - start_time
        result_Schedule.scheduler_latency = run_time
        return_model = {}
        for obj_name, obj in model.items():
            for index, item in enumerate(obj, start=1):
                return_key = f"{obj_name}_{index}"
                return_model[return_key] = item
                
        print(return_model)
        
        for job_name, job_info in scheduler_job.items():
            if job_name in return_model:
                job_info.machine = return_model[job_name]
                
        machine_dict_NoTODS = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
        result_Schedule.typeMachine = machine_dict_NoTODS
        
        # Initialize machine available time
        machine_times = {machine: 0.0 for machine in machine_dict_NoTODS}

        # Result list
        job_json = []

        # Scheduling
        for job_name, job_info in scheduler_job.items():
            # Select machine that is available earliest
            start_time = machine_times[job_info.machine]
            duration = job_info.qubits  # duration = number of qubits
            end_time = start_time + duration
            
            
            # Create job record
            job_record = {
                "job": job_info.job_name,
                "qubits": job_info.qubits,
                "machine": job_info.machine,
                "capacity": machine_dict_NoTODS[job_info.machine],
                "start": start_time,
                "end": end_time,
                "duration": duration
            }
            
            job_json.append(job_record)
            
            # Update machine's available time
            machine_times[job_info.machine] = end_time

        # Save result to JSON file
        with open('component/d_scheduling/scheduleResult/ilp/NoTODS/schedule.json', 'w') as f:
            json.dump(job_json, f, indent=4)
            
        data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/ilp/NoTODS/schedule.json")
        
        for job_id, job in scheduler_job.items():
            backend = machines.get(job.machine)
            if backend:
                # Perform transpilation
                job.circuit.data = [hasChange for hasChange in job.circuit.data if hasChange.operation.name != "qpd_1q"]
                job.transpiled_circuit = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                job.circuit.measure_all()
                job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
            else:
                print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
                
            job.print()
            
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
                
            job_info.print()
            
        utilization_permachine = analyze_cal.calculate_utilization(data)
        print(utilization_permachine)
        
        for job_name, job_info in origin_job_info.items():
            if job_info.childrenJobs is not None:
                count_fidelity = 0
                for child_job in job_info.childrenJobs:
                    #updata start time and end time from child job to parent job
                    job_info.start_time = min(job_info.start_time, child_job.start_time)
                    job_info.end_time = max(job_info.end_time, child_job.end_time)
                    job_info.duration = job_info.end_time - job_info.start_time
                    count_fidelity += child_job.fidelity * child_job.qubits
                job_info.fidelity = count_fidelity / job_info.qubits
            else:
                print(f"Job {job_name} has no children jobs.")
                
        metrics = analyze_cal.calculate_metrics(data, utilization_permachine)
        analyze_cal.print_metrics(metrics)

        result_Schedule.average_turnaroundTime = metrics['average_turnaroundTime']
        result_Schedule.average_responseTime = metrics['average_responseTime']
        result_Schedule.makespan = metrics['makespan']
        result_Schedule.average_utilization = metrics['average_utilization']
        result_Schedule.average_throughput = metrics['throughput']
        
        sum_fidelity = 0
        for job_name, job_info in origin_job_info.items():
            sum_fidelity += job_info.fidelity * job_info.qubits
        average_fidelity = sum_fidelity / (result_Schedule.averageQubits * result_Schedule.numcircuit)
        result_Schedule.average_fidelity = average_fidelity

        # Create the directory path
        algorithm_folder_path = os.path.join("component", "finalResult","5_5", result_Schedule.nameSchedule, result_Schedule.nameAlgorithm)
        os.makedirs(algorithm_folder_path, exist_ok=True)

        # Construct the base file name
        numcircuit = result_Schedule.numcircuit
        numqubit = result_Schedule.averageQubits
        print(numqubit)
        base_filename = f"{numcircuit}_{numqubit}"

        # Ensure the filename is unique
        existing_files = os.listdir(algorithm_folder_path)
        matching_files = [f for f in existing_files if f.startswith(base_filename) and f.endswith(".json")]

        if not matching_files:
            final_filename = f"{base_filename}_0.json"
        else:
            suffixes = [
                int(f.replace(base_filename, "").replace(".json", "").replace("_", ""))
                for f in matching_files
                if f.replace(base_filename, "").replace(".json", "").replace("_", "").isdigit()
            ]
            next_suffix = max(suffixes, default=0) + 1
            final_filename = f"{base_filename}_{next_suffix}.json"

        # Define the output file path
        output_file_path = os.path.join(algorithm_folder_path, final_filename)

        # Save the result to the JSON file
        with open(output_file_path, "w") as f:
            json.dump(asdict(result_Schedule), f, indent=4)

        # Print the result
        print(f"Result saved to {output_file_path}")