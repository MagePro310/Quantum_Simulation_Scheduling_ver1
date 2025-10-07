"""A utility script to visualize a solution to the scheduling problem."""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import ticker
from matplotlib.patches import Patch


def _read_solution_file(solution_file: str) -> list[dict]:
    """Reads a solution from a file and converts it to a schedule."""

    with open(solution_file, encoding="utf-8") as f:
        data = json.load(f)

    variables = data.get("variables", {})
    params = data.get("params", {})

    jobs = params.get("jobs", [])
    machines = params.get("machines", [])
    job_capacities = params.get("job_capcities", {})
    machine_capacities = params.get("machine_capacities", {})

    rows_list = []

    for job in jobs:
        # Extract schedule from z_ikt variables instead of s_j/c_j
        assigned_machine = None
        start_timestep = None
        end_timestep = None
        
        # Find assigned machine
        for machine in machines:
            machine_key = f"x_ik_{jobs.index(job) + 1}_{machine}"
            if variables.get(machine_key, 0) >= 0.5:
                assigned_machine = machine
                break
        
        if assigned_machine is None:
            print(f"Warning: No machine assigned for job {job}. Skipping...")
            continue
        
        # Find start and end timesteps from z_ikt variables
        job_idx = jobs.index(job) + 1
        active_timesteps = []
        
        for timestep in range(32):  # Assume max 32 timesteps
            z_var = f"z_ikt_{job_idx}_{assigned_machine}_{timestep}"
            if variables.get(z_var, 0) >= 0.5:
                active_timesteps.append(timestep)
        
        if not active_timesteps:
            print(f"Warning: No active timesteps found for job {job}. Skipping...")
            continue
        
        start_timestep = min(active_timesteps)
        end_timestep = max(active_timesteps) + 1  # +1 because end is exclusive
        duration = end_timestep - start_timestep

        capacity = machine_capacities.get(assigned_machine, None)

        rows_list.append({
            "job": job,
            "qubits": job_capacities.get(job, None),
            "machine": assigned_machine,
            "capacity": capacity,
            "start": float(start_timestep),
            "end": float(end_timestep),
            "duration": float(duration),
        })

        # Skip old extraction code
        continue
        
        start_key = f"s_j_{jobs.index(job) + 1}"
        end_key = f"c_j_{jobs.index(job) + 1}"

        start = variables.get(start_key, None)
        end = variables.get(end_key, None)  # Bỏ +1 để end time đúng 

        if start is None or end is None:
            print(f"Warning: Missing start or end time for job {job}. Skipping...")
            continue

        duration = end - start

        assigned_machine = None
        for machine in machines:
            machine_key = f"x_ik_{jobs.index(job) + 1}_{machine}"
            if variables.get(machine_key, 0) >= 0.5:
                assigned_machine = machine
                break

        if assigned_machine is None:
            print(f"Warning: No machine assigned for job {job}. Skipping...")
            continue

        capacity = machine_capacities.get(assigned_machine, None)

        rows_list.append({
            "job": job,
            "qubits": job_capacities.get(job, None),
            "machine": assigned_machine,
            "capacity": capacity,
            "start": start,
            "end": end,
            "duration": duration,
        })

    return rows_list


def extract_schedule_data(solution_file: str, output_dir: str | None = None) -> None:
    """Generates a plot of the schedule in the solution file."""

    if output_dir is None:
        base_dir = os.path.abspath(
            os.path.join(
            os.path.dirname(os.path.abspath(solution_file)),
            "..", "..", "..")
        )
        algorithm_name = "MILQ_extend"  # Replace with the actual algorithm name dynamically if needed
        output_dir = os.path.join(base_dir, "scheduleResult","ilp", algorithm_name)
    
    row_list = _read_solution_file(solution_file)
    # save df to json
    job_json_path = os.path.join(output_dir, 'schedule.json')
    with open(job_json_path, 'w', encoding='utf-8') as f_json:
        json.dump(row_list, f_json, indent=4)
    print(f"Saved job data as JSON to: {job_json_path}")


def extract_data(location):
    base_name = os.path.splitext(os.path.basename(location))[0]
    extract_schedule_data(location, output_dir=None)
