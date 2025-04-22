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
    num_jobs = len(data)
    waiting_time = sum(job['start'] for job in data)  # assuming ready_time = 0
    response_time = sum(job['end'] for job in data)
    makespan = max(job['end'] for job in data)
    throughput = num_jobs / makespan

    # Utilization
    machine_usage = defaultdict(float)
    machine_capacity = {}
    for job in data:
        machine = job['machine']
        machine_usage[machine] += job['qubits'] * job['duration']
        machine_capacity[machine] = job['capacity']

    utilization_per_machine = {}
    for machine in machine_usage:
        utilization = machine_usage[machine] / (machine_capacity[machine] * makespan)
        utilization_per_machine[machine] = utilization

    avg_utilization = sum(utilization_per_machine.values()) / len(utilization_per_machine)

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
