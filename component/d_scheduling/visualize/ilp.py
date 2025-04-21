"""A utility script to visualize a solution to the scheduling problem."""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import ticker
from matplotlib.patches import Patch


def _read_solution_file(solution_file: str) -> pd.DataFrame:
    """Reads a solution file and returns a dataframe with job scheduling information."""

    try:
        with open(solution_file, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{solution_file}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Error: File '{solution_file}' is not a valid JSON.")

    if "params" not in data or "variables" not in data:
        raise KeyError("Error: JSON file structure is incorrect. Missing 'params' or 'variables'.")

    params = data["params"]
    variables = data["variables"]

    jobs = params.get("jobs", [])
    machines = params.get("machines", [])
    job_capacities = params.get("job_capcities", {})
    machine_capacities = params.get("machine_capacities", {})

    rows_list = []

    for job in jobs:
        start_key = f"s_j_{jobs.index(job) + 1}"
        end_key = f"c_j_{jobs.index(job) + 1}"

        start = variables.get(start_key, None)
        end = variables.get(end_key, None) + 1 

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

    # Save outputs in the same directory as the solution file
    output_dir = os.path.dirname(os.path.abspath(solution_file))

    # Save job_data.txt (dict each line)
    job_data_txt = os.path.join(output_dir, 'job_data.txt')
    with open(job_data_txt, 'w', encoding='utf-8') as f_txt:
        for item in rows_list:
            f_txt.write(f"{item}\n")
    print(f"Saved job data to: {job_data_txt}")

    # Save job_data.json (full JSON)
    job_json_path = os.path.join(output_dir, 'job_data.json')
    with open(job_json_path, 'w', encoding='utf-8') as f_json:
        json.dump(rows_list, f_json, indent=4)
    print(f"Saved job data as JSON to: {job_json_path}")

    df = pd.DataFrame(rows_list)
    return df


def generate_schedule_plot(solution_file: str, pdf_name: str | None = None, output_dir: str | None = None) -> None:
    """Generates a plot of the schedule in the solution file."""

    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(solution_file))

    df = _read_solution_file(solution_file)
    print(df)

    # Color mapping for machines
    machine_colors = ["#154060", "#98c6ea", "#527a9c"]
    color_mapping = dict(zip(df["machine"].unique(), machine_colors))

    _, ax = plt.subplots()

    for i, row in df.iterrows():
        padding = 0.1
        height = 1 - 2 * padding
        ax.barh(
            i,
            row["duration"],
            left=row["start"],
            height=height,
            edgecolor="black",
            linewidth=2,
            color=color_mapping[row["machine"]],
        )

    patches = []
    for color in color_mapping.values():
        p = Patch(color=color)
        p.set_edgecolor("black")
        p.set_linewidth(1)
        patches.append(p)

    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    yticks = np.arange(len(df))
    ytick_labels = [f"{job} ({qubits})" for job, qubits in zip(df["job"], df["qubits"])]
    ax.set_yticks(yticks)
    ax.set_yticklabels(ytick_labels)
    ax.invert_yaxis()

    plt.xlabel("Time")
    plt.grid(axis="x", which="major")
    plt.grid(axis="x", which="minor", alpha=0.4)

    legend_labels = [
        f"{label} ({df[df['machine'] == label]['capacity'].iloc[0]})"
        for label in color_mapping.keys()
    ]
    plt.legend(handles=patches, labels=legend_labels)

    if pdf_name:
        pdf_path = os.path.join(output_dir, pdf_name)
        plt.tight_layout()
        plt.savefig(pdf_path, format="pdf", bbox_inches="tight")
        print(f"Saved plot to: {pdf_path}")
    else:
        plt.show()


def visualize(location):
    base_name = os.path.splitext(os.path.basename(location))[0]
    pdf_output = f"{base_name}_plot.pdf"
    generate_schedule_plot(location, pdf_output, output_dir=None)
