import random

# Define the jobs
jobs = [
    {'job': 'A', 'qubits': 2, 'machine': 'QUITO', 'capacity': 5, 'start': 0.0, 'duration': 12.59},
    {'job': 'B', 'qubits': 3, 'machine': 'QUITO', 'capacity': 5, 'start': 0.0, 'duration': 8.2},
    {'job': 'C', 'qubits': 5, 'machine': 'BELEM', 'capacity': 5, 'start': 0.0, 'duration': 14.63},
    {'job': 'D', 'qubits': 2, 'machine': 'QUITO', 'capacity': 5, 'start': 1.0, 'duration': 11.33},
    {'job': 'E', 'qubits': 2, 'machine': 'QUITO', 'capacity': 5, 'start': 1.0, 'duration': 7.13},
]



# Generate unique execution times
def generate_unique_execution_time(base_duration):
    return round(base_duration * random.uniform(0.8, 1.2), 2)

# Simulate the scheduling with parallel execution support
def simulate_scheduling(jobs):
    machine_current = {'QUITO': [], 'BELEM': []}  # Track active jobs for each machine
    
    ready_queue = { 'QUITO': [], 'BELEM': [] }  # Jobs ready to be executed on each machine
    
    # update job with unique execution times
    for job in jobs:
        job['duration'] = generate_unique_execution_time(job['duration'])
        job['end'] = job['start'] + job['duration']
    
    
    # Schedule jobs on each machine
    
    jobs_QUITO = [job for job in jobs if job['machine'] == 'QUITO']
    jobs_BELEM = [job for job in jobs if job['machine'] == 'BELEM']
    
    current_time_QUITO = 0.0
    current_time_BELEM = 0.0
    current_capacity_QUITO = 5
    current_capacity_BELEM = 5
    

    