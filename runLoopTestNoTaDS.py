import sys
sys.path.append('./')
import json
import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from dataclasses import dataclass, asdict
from enum import auto, Enum

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_error_map, plot_distribution

from qiskit_ibm_runtime import SamplerV2

from component.a_backend.fake_backend import *
from component.b_benchmark.mqt_tool import QuantumBenchmark
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import *
from component.c_circuit_work.knitting.width_k import merge_multiple_circuits
from component.d_scheduling.algorithm.ilp.MILQ_extend import MILQ_extend_implementation
# from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
# from component.d_scheduling.algorithm.heuristic.MTMC import MTMC_implement
from component.d_scheduling.extract import ilp
from component.d_scheduling.simulation.scheduling_multithread import simulate_scheduling as simulate_multithread
from component.d_scheduling.analyze import analyze_cal
from component.d_scheduling.datawork.visualize import visualize_data
from component.d_scheduling.datawork.updateToDict import update_scheduler_jobs
from component.f_assemble.assemble_work import fidelity_from_counts


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
num_jobs = int(sys.argv[1])
num_qubits_per_job = int(sys.argv[2])

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
result_Schedule.nameSchedule = "NoTaDS"

# Define the machines
machines = {}
backend0 = FakeBelemV2()
backend1 = FakeManilaV2()
machines[backend0.name] = backend0
machines[backend1.name] = backend0

# Define benchmark
jobs = {}
for i in range(num_jobs):
    job_id = str(i + 1)
    jobs[job_id] = num_qubits_per_job

# update to result_Schedule
result_Schedule.numcircuit = len(jobs)
result_Schedule.averageQubits = sum(jobs.values()) / len(jobs)

# generate circuits and job information
origin_job_info = {}

for job_name, num_qubits in jobs.items():
    circuit, result_Schedule.nameAlgorithm = QuantumBenchmark.create_circuit(num_qubits, job_name)
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

for job in origin_job_info.values():
    job.print()
    
process_job_info = origin_job_info.copy()
# Create list obj for each job
from component.d_scheduling.algorithm.ilp.NoTaDS.NoTaDS import *
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

print(subcircuit_dict)
# for job in process_job_info.values():
#     job.print()
result_Schedule.sampling_overhead = sum_overhead

# Get the job for run scheduler

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
    
machine_dict_NoTaDS = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
result_Schedule.typeMachine = machine_dict_NoTaDS

# ============================= MTMC Algorithm ==============================
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
# update to scheduler_job
for job_name, job_info in scheduler_job.items():
    if job_name in return_model:
        job_info.machine = return_model[job_name]
        
for job_name, job_info in scheduler_job.items():
    job_info.print()
    
machine_dict_NoTaDS = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
result_Schedule.typeMachine = machine_dict_NoTaDS

import json

# Initialize machine available time
machine_times = {machine: 0.0 for machine in machine_dict_NoTaDS}

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
        "capacity": machine_dict_NoTaDS[job_info.machine],
        "start": start_time,
        "end": end_time,
        "duration": duration
    }
    
    job_json.append(job_record)
    
    # Update machine's available time
    machine_times[job_info.machine] = end_time

# Save result to JSON file
with open('component/d_scheduling/scheduleResult/ilp/NoTaDS/schedule.json', 'w') as f:
    json.dump(job_json, f, indent=4)

data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/ilp/NoTaDS/schedule.json")
update_scheduler_jobs(data, scheduler_job)
# ============================== MTMC Algorithm ==============================

for job_id, job in scheduler_job.items():
    backend = machines.get(job.machine)
    if backend:
        # Perform transpilation
        job.circuit.data = [hasChange for hasChange in job.circuit.data if hasChange.operation.name != "qpd_1q"]
        job.transpiled_circuit = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
        # job.circuit.measure_all()
        # job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
    else:
        print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
        
jobs = data.copy()
updated_jobs = simulate_multithread(jobs, scheduler_job)



# Example: you have circuits per job_id
# job_circuits = {}
# for job_id, job_info in scheduler_job.items():
#     key = job_info.job_name
    
#     job_circuits[key] = job_info.circuit


# # Group by (machine, start_time)
# grouped_jobs = defaultdict(list)
# for job in updated_jobs:
#     key = (job['machine'], job['start'])
#     grouped_jobs[key].append(job['job'])

# print("Grouped Jobs:")
# for key, job_ids in grouped_jobs.items():
#     print(f"{key}: {job_ids}")

# # Merge circuits for each (machine, start_time)
# expanded_circuits = {}
# for (machine, start_time), job_ids in grouped_jobs.items():
#     print(job_ids)
#     circuits_to_merge = [job_circuits[job_id] for job_id in job_ids]
#     print("Circuit_To_Merge")
#     print(circuits_to_merge)
#     if len(circuits_to_merge) == 1:
#         merged_circuit = circuits_to_merge[0]  # no merge needed
#     else:
#         print(circuits_to_merge)
#         merged_circuit = merge_multiple_circuits(circuits_to_merge)
    
#     expanded_circuits[tuple(job_ids)] = merged_circuit

# print("Expanded Circuits:")
# print(expanded_circuits)

# for keys, circuit_expand in expanded_circuits.items():
#     # print(f"Expanded Circuit for {key}:")
#     # print(circuit)
#     circuit_expand.measure_all()
#     for key in keys:
#         # print(f"Job ID: {key}")
#         scheduler_job[key].knitted_circuit = circuit_expand

# for job_info, job_item in scheduler_job.items():
#     print(job_info)
#     job_item.print()
    

# # Transpile circuits for all scheduled jobs
# for job_id, job in scheduler_job.items():
#     backend = machines.get(job.machine)
#     if backend:
#         # Perform transpilation
#         # job.transpiled_circuit = transpile(job.knitted_circuit, backend, scheduling_method='alap', layout_method='trivial')
#         job.transpiled_circuit_measured = transpile(job.knitted_circuit, backend, scheduling_method='alap', layout_method='trivial')
#     else:
#         print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
#     job.print()

for job_id, job in scheduler_job.items():
    backend = machines.get(job.machine)
    if backend:
        # Perform transpilation
        # job.transpiled_circuit = transpile(job.knitted_circuit, backend, scheduling_method='alap', layout_method='trivial')
        job.circuit.measure_all()
        job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
    else:
        print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
    job.print()


# from qiskit.visualization.timeline import draw, IQXDebugging
# draw(scheduler_job['1'].transpiled_circuit, target=machines['fake_belem'].target)

# after have the circuit we connect to
# from qiskit.visualization import plot_circuit_layout
# plot_circuit_layout(scheduler_job['1'].transpiled_circuit, machines['fake_belem'])


for job_name, job_info in scheduler_job.items():
    backend = machines.get(job_info.machine)
    
    if backend:
        transpiled_circuit = job_info.transpiled_circuit_measured
        # print(transpiled_circuit)
        
        # Run the ideal simulation
        ideal_result = aer_simulator.run(transpiled_circuit, shots=1024).result()
        ideal_counts = ideal_result.get_counts(transpiled_circuit)
        
        # Run circuit on the simulated backend
        job = SamplerV2(backend).run([transpiled_circuit], shots=1024)
        sim_result = job.result()[0]
        sim_counts = sim_result.data.meas.get_counts()
        # print("ideal_counts")
        # print(ideal_counts)
        # print("sim_counts")
        # print(sim_counts)
        # Calculate fidelity
        fidelity_val, rho_ideal, rho_sim = fidelity_from_counts(ideal_counts, sim_counts)
        
        # Store the fidelity values
        job_info.fidelity = fidelity_val
        
utilization_permachine = analyze_cal.calculate_utilization(data)
print(utilization_permachine)

# Check if have children jobs in origin_job_info
for job_name, job_info in origin_job_info.items():
    if job_info.childrenJobs is not None:
        count_fidelity = 0
        for child_job in job_info.childrenJobs:
            #update start time and end time from child job to parent job
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

# Calculate all the values of components
sum_fidelity = 0
for job_name, job_info in origin_job_info.items():
    sum_fidelity += job_info.fidelity * job_info.qubits
average_fidelity = sum_fidelity / (result_Schedule.averageQubits * result_Schedule.numcircuit)
result_Schedule.average_fidelity = average_fidelity


algorithm_folder_path = os.path.join("component", "finalResult","5_5", result_Schedule.nameSchedule, result_Schedule.nameAlgorithm)
os.makedirs(algorithm_folder_path, exist_ok=True)

# Construct the base file name
numcircuit = result_Schedule.numcircuit
numqubit = result_Schedule.averageQubits
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