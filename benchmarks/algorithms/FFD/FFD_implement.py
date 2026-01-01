"""
FFD (First Fit Decreasing) Scheduling Algorithm Implementation

Algorithm Overview:
1. Sort jobs by qubit requirement (decreasing order - largest first)
2. For each job, find the machine where it can start earliest
3. Allow parallel execution if total qubits don't exceed machine capacity
4. Duration = number of qubits (simplified model)

Time Complexity: O(n * m * t) where n=jobs, m=machines, t=time steps
Space Complexity: O(n + m)
"""

import json
import os

def can_run_at_time(machine_schedule, machine_capacity, job_qubits, start, duration):
    """
    Check if a job can run at a specific time considering parallel execution.
    
    Jobs can run in parallel on the same machine if:
    - Their time windows overlap AND
    - Sum of qubits ≤ machine capacity
    
    Args:
        machine_schedule: List of jobs already scheduled on this machine
        machine_capacity: Total qubit capacity of the machine
        job_qubits: Qubit requirement of the new job
        start: Proposed start time
        duration: Job duration
        
    Returns:
        bool: True if job can run at this time, False otherwise
        
    Example:
        Machine capacity = 10 qubits
        Job A (5 qubits) runs at [0, 5]
        Job B (4 qubits) can run at [2, 6] because 5 + 4 ≤ 10 (overlap but fit)
        Job C (6 qubits) CANNOT run at [2, 8] because 5 + 6 > 10 (exceeds capacity)
    """
    load = 0  # Current qubit load at the proposed time
    
    for job in machine_schedule:
        # Check if time windows overlap
        # Not overlap if: new job ends before existing starts OR new job starts after existing ends
        if not (start + duration <= job["start"] or start >= job["end"]):
            load += job["qubits"]
    
    # Can run if adding this job doesn't exceed capacity
    return load + job_qubits <= machine_capacity


def find_earliest_start(machine_schedule, machine_capacity, job_qubits):
    """
    Find the earliest possible start time for a job on a specific machine.
    
    Uses incremental time search with parallel execution consideration.
    Duration is set equal to qubits (simplified scheduling model).
    
    Args:
        machine_schedule: Current schedule on the machine
        machine_capacity: Machine's qubit capacity
        job_qubits: Job's qubit requirement
        
    Returns:
        float: Earliest start time where job can fit
        
    Algorithm:
        - Start at t=0, increment by 1.0 time unit
        - Check each time slot for availability considering parallel jobs
        - Return first valid time slot
    """
    duration = job_qubits  # Duration = qubits (scheduling model assumption)
    t = 0.0
    step = 1.0
    
    while True:
        if can_run_at_time(machine_schedule, machine_capacity, job_qubits, t, duration):
            return t
        t += step


def schedule_jobs_ffd(job_capacities, machine_capacities):
    """
    FFD (First Fit Decreasing) scheduling with dynamic time allocation.
    
    Main Algorithm Steps:
    1. Sort jobs by qubit requirement (decreasing - largest first)
    2. For each job:
       a. Check all machines
       b. Find earliest start time on each machine
       c. Select machine with earliest start time
       d. Assign job to that machine
    
    Args:
        job_capacities: Dict[str, int] - {job_name: qubit_requirement}
        machine_capacities: Dict[str, int] - {machine_name: qubit_capacity}
        
    Returns:
        List[Dict]: Schedule entries with format:
        [{
            "job": job_id,
            "qubits": qubit_count,
            "machine": machine_name,
            "capacity": machine_capacity,
            "start": start_time,
            "end": end_time,
            "duration": duration
        }, ...]
        
    Example:
        Input:
            jobs = {"job_0": 5, "job_1": 8, "job_2": 3}
            machines = {"machine_A": 10, "machine_B": 7}
        
        Process:
            1. Sort: [job_1(8), job_0(5), job_2(3)]
            2. job_1(8) → machine_A at t=0 (only machine_A fits)
            3. job_0(5) → machine_B at t=0 (can run parallel on B)
            4. job_2(3) → machine_A at t=0 (8+3 > 10, so starts at t=8)
    """
    # Step 1: Sort jobs by qubit requirement (descending)
    jobs = sorted(job_capacities.items(), key=lambda x: -x[1])
    
    # Initialize machine schedules (empty initially)
    machines = {name: [] for name in machine_capacities}
    schedule = []  # Final schedule output

    # Step 2: Process each job in sorted order
    for job_id, qubit in jobs:
        # Skip jobs with 0 qubits (edge case)
        if qubit == 0:
            continue

        duration = qubit  # Duration = qubits (model assumption)
        
        # Variables to track best assignment
        best_machine = None
        best_start = float("inf")  # Initialize to infinity
        best_entry = None

        # Step 3: Try all machines, find the one with earliest start
        for machine_name, capacity in machine_capacities.items():
            machine_schedule = machines[machine_name]
            
            # Find earliest start time on this machine
            start_time = find_earliest_start(machine_schedule, capacity, qubit)
            end_time = start_time + duration

            # Update best if this machine can start earlier
            if start_time < best_start:
                best_start = start_time
                best_machine = machine_name
                best_entry = {
                    "job": job_id,
                    "qubits": qubit,
                    "machine": machine_name,
                    "capacity": capacity,
                    "start": start_time,
                    "end": end_time,
                    "duration": duration
                }

        # Step 4: Assign job to best machine
        schedule.append(best_entry)
        machines[best_machine].append(best_entry)

    return schedule


def example_problem(job_capacities, machine_capacities, location):
    """
    Run FFD scheduling and save results to JSON file.
    
    Args:
        job_capacities: Dictionary of job qubit requirements
        machine_capacities: Dictionary of machine capacities
        location: Output directory path
        
    Returns:
        List[Dict]: Complete schedule
        
    Output Format:
        Creates <location>/schedule.json with scheduling results
    """
    nameOutput = f"{location}/schedule.json"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(nameOutput), exist_ok=True)
    
    # Run FFD algorithm
    schedule = schedule_jobs_ffd(job_capacities, machine_capacities)
    
    # Save to JSON file
    with open(nameOutput, "w") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)
    
    print(f"Schedule saved to {nameOutput}")
    print("Jobs have Updated Information:")
    return schedule
