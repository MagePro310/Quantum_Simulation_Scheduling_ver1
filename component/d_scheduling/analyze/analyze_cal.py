import ast
from collections import defaultdict
import json

def load_job_data(filepath):
    """Load job data from a JSON file."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def calculate_metrics(data, ultilization_per_machine):
    """Calculate various job scheduling metrics."""
    # {'job': '1', 'qubits': 2, 'machine': 'fake_manila', 'capacity': 5, 'start': 0.0, 'end': 1568.0, 'duration': 1568}
    # {'job': '2', 'qubits': 2, 'machine': 'fake_belem', 'capacity': 5, 'start': 0.0, 'end': 3648.0, 'duration': 3648}
    # {'job': '3', 'qubits': 2, 'machine': 'fake_belem', 'capacity': 5, 'start': 0.0, 'end': 3648.0, 'duration': 3648}

    num_jobs = len(data)
    average_turnaroundTime = sum(job['end'] for job in data) / num_jobs  # updated variable name
    average_responeTime = sum(job['start'] for job in data) / num_jobs  # corrected variable name
    makespan = max(job['end'] for job in data)
    print(makespan)
    print(num_jobs)
    throughput = makespan / num_jobs  # corrected variable name
    print(throughput)
    # calculate avg_utilization of each machin
    # ulization_per_machine = defaultdict(<class 'float'>, {'fake_belem': 0.8, 'fake_manila': 0.4})
    
    average_utilization = 0  # corrected variable name
    sizemachine = defaultdict(float)
    for job in data:
        sizemachine[job['machine']] = job['capacity'] # Store the capacity of each machine
    
    for machine, utilization in ultilization_per_machine.items():
        average_utilization += utilization * sizemachine[machine]
    
    average_utilization = average_utilization / sum(sizemachine.values())

    return {
        'average_turnaroundTime': average_turnaroundTime,
        'average_responseTime': average_responeTime,
        'makespan': makespan,
        'throughput': throughput,
        'average_utilization': average_utilization,  # corrected variable name
    }

def calculate_utilization(data):
    """Calculate the average utilization of each machine."""
    utilization_per_machine = defaultdict(float)
    makespan = defaultdict(float)
    resource_machine = defaultdict(float)
    
    for job in data:
        resource_machine[job['machine']] = job['capacity'] # Store the capacity of each machine
    
    for job in data:
        # Calculate the makespan for each job
        makespan[job['machine']] = max(makespan[job['machine']], job['end'])

    for job in data:
        utilization_per_machine[job['machine']] += job['qubits'] * job['duration']
    # Normalize by the capacity of the machine
    for machine, total_utilization in utilization_per_machine.items():
        total_utilization = total_utilization / (makespan[machine] * resource_machine[machine])
        utilization_per_machine[machine] = total_utilization
        
    return utilization_per_machine




def print_metrics(metrics):
    """Print the calculated metrics in a readable format."""
