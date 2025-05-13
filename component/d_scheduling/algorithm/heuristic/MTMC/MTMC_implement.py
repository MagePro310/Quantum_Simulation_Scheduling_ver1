import random
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor

def multi_task_multi_chip_scheduling(chiplist, tasks):
    task_remaining = tasks.copy()
    count_loop = 0
    results_success = []

    chip_status = {chip['name']: {'capacity': chip['capacity'], 'running_tasks': []} for chip in chiplist}

    global_time = 0

    while task_remaining or any(chip_status[c]['running_tasks'] for c in chip_status):
        epsilon = len(task_remaining)

        tasklist = sorted(task_remaining, key=lambda x: x['name'])
        task_remaining = []

        for chip in chip_status.values():
            finished = []
            for task in chip['running_tasks']:
                task['time_left'] -= 1
                if task['time_left'] == 0:
                    chip['capacity'] += task['qubits']
                    finished.append(task)
            chip['running_tasks'] = [t for t in chip['running_tasks'] if t not in finished]

        allocated, not_allocated = MultiTaskMultiChipsPreAlloc(tasklist, chip_status, global_time)
        results_success.extend(allocated)

        task_remaining.extend(not_allocated)

        global_time += 1
        count_loop += 1

    return format_result_json(results_success, chiplist)


def MultiTaskMultiChipsPreAlloc(tasklist, chip_status, global_time):
    allocated = []
    no_execute = []
    lock = threading.Lock()

    def allocate_task(task):
        nonlocal allocated, no_execute
        with lock:
            possible_chips = [chip_name for chip_name, chip in chip_status.items() if chip['capacity'] >= task['qubits']]
            if possible_chips:
                selected_chip = max(possible_chips, key=lambda chip_name: chip_status[chip_name]['capacity'])
                chip_status[selected_chip]['capacity'] -= task['qubits']
                task_copy = task.copy()
                task_copy['assigned_chip'] = selected_chip
                task_copy['capacity'] = chip_status[selected_chip]['capacity'] + task['qubits']
                task_copy['time_left'] = task_copy['qubits']
                task_copy['start_time'] = global_time
                task_copy['end_time'] = global_time + task_copy['qubits']
                task_copy['duration'] = task_copy['end_time'] - task_copy['start_time']
                chip_status[selected_chip]['running_tasks'].append(task_copy)
                allocated.append(task_copy)
            else:
                no_execute.append(task)

    with ThreadPoolExecutor() as executor:
        executor.map(allocate_task, tasklist)

    return allocated, no_execute


def format_result_json(results_success, chiplist):
    result_json = []
    chip_capacity_map = {chip['name']: chip['capacity'] for chip in chiplist}

    for task in sorted(results_success, key=lambda x: x['start_time']):
        result_json.append({
            "job": task['name'],
            "qubits": task['qubits'],
            "machine": task['assigned_chip'],
            "capacity": chip_capacity_map[task['assigned_chip']],
            "start": float(task['start_time']),
            "end": float(task['end_time']),
            "duration": float(task['duration'])
        })

    return result_json


def example_problem(tasks_dict, chiplist_dict, output_folder):
    tasks_list = [{'name': k, 'qubits': v} for k, v in tasks_dict.items()]
    chiplist_list = [{'name': k, 'capacity': v} for k, v in chiplist_dict.items()]

    results_json = multi_task_multi_chip_scheduling(chiplist_list, tasks_list)

    output_file = os.path.join(output_folder, "schedule.json")
    os.makedirs(output_folder, exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(results_json, f, indent=4)

    return results_json
