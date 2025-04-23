import ast
from collections import defaultdict
import json

def load_job_data(filepath):
    """Load job data from a JSON file."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def calculate_metrics(data):
    """Calculate various job scheduling metrics."""
    # {'job': '1', 'qubits': 2, 'machine': 'fake_manila', 'capacity': 5, 'start': 0.0, 'end': 1568.0, 'duration': 1568}
    # {'job': '2', 'qubits': 2, 'machine': 'fake_belem', 'capacity': 5, 'start': 0.0, 'end': 3648.0, 'duration': 3648}
    # {'job': '3', 'qubits': 2, 'machine': 'fake_belem', 'capacity': 5, 'start': 0.0, 'end': 3648.0, 'duration': 3648}

    num_jobs = len(data)
    turnaround_average = sum(job['end'] for job in data) / num_jobs  # updated variable name
    responetime_average = sum(job['start'] for job in data) / num_jobs
    makespan = max(job['end'] for job in data)
    throughput = num_jobs / makespan

    # calculate avg_utilization of each machine
    utilization_per_machine = defaultdict(float)
    for job in data:
        utilization_per_machine[job['machine']] += job['qubits'] * job['']
    
        

    return {
        'waiting_time': waiting_time,
        'response_time': response_time,
        'makespan': makespan,
        'throughput': throughput,
        'utilization_per_machine': utilization_per_machine,
        'average_utilization': avg_utilization
    }

def print_metrics(metrics):
    """Print the calculated metrics in a readable format."""
    print("\n=== Metrics ===")
    print(f"Waiting Time: {metrics['waiting_time']}")
    print(f"Response Time: {metrics['response_time']}")
    print(f"Makespan: {metrics['makespan']}")
    print(f"Throughput: {metrics['throughput']:.4f}")
    for machine, util in metrics['utilization_per_machine'].items():
        print(f"Utilization on machine {machine}: {util:.4f}")
    print(f"Average Utilization: {metrics['average_utilization']:.4f}")
