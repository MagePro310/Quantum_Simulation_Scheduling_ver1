
import json
from typing import List, Dict
import os

def find_earliest_start(machine_schedule: List[Dict], machine_capacity: int, job_qubits: int, base_time_per_qubit: float) -> float:
    """Find the earliest time the job can run without exceeding capacity."""
    duration = job_qubits * base_time_per_qubit
    t = 0.0
    time_step = 1.0

    while True:
        # Check current load in interval [t, t+duration]
        load = 0
        for job in machine_schedule:
            if not (t + duration <= job['start'] or t >= job['end']):  # overlap
                load += job['qubits']

        if load + job_qubits <= machine_capacity:
            return t
        t += time_step

def schedule_jobs_parallel(job_capacities, machine_capacities, base_time_per_qubit=1.0):
    # Sort jobs in descending order of qubits
    sorted_jobs = sorted(job_capacities.items(), key=lambda x: -x[1])

    # Initialize per-machine schedules
    machines = {name: [] for name in machine_capacities}

    schedule = []

    for job_id, qubit in sorted_jobs:
        if qubit == 0:
            continue

        duration = qubit * base_time_per_qubit
        assigned = False

        # Iterate over all machines to find the earliest start time
        earliest_start = float('inf')
        chosen_machine = None
        chosen_schedule_entry = None

        for machine_name, capacity in machine_capacities.items():
            machine_schedule = machines[machine_name]
            start_time = find_earliest_start(machine_schedule, capacity, qubit, base_time_per_qubit)
            end_time = start_time + duration

            if start_time < earliest_start:
                earliest_start = start_time
                chosen_machine = machine_name
                chosen_schedule_entry = {
                    "job": job_id,
                    "qubits": qubit,
                    "machine": machine_name,
                    "capacity": capacity,
                    "start": start_time,
                    "end": end_time,
                    "duration": duration
                }

        if chosen_machine and chosen_schedule_entry:
            # Append the job info to the global schedule
            schedule.append(chosen_schedule_entry)
            # Add the job to the chosen machine's schedule
            machines[chosen_machine].append(chosen_schedule_entry)
            assigned = True

        if not assigned:
            raise RuntimeError(f"No machine can accommodate job {job_id} with {qubit} qubits.")

    return schedule


def example_problem(job_capacities, machine_capacities, location):
    """
    Main function to execute the First Fit Decreasing (FFD) algorithm.
    """

    nameOutput = f"{location}/schedule.json"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(nameOutput), exist_ok=True)
    
    schedule = schedule_jobs_parallel(job_capacities, machine_capacities, base_time_per_qubit=10.0)
    
    # Save the schedule to a JSON file
    with open(nameOutput, 'w') as f:
        json.dump(schedule, f, indent=4)
    print(f"Schedule saved to {nameOutput}")