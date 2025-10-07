import json
import os

def can_run_at_time(machine_schedule, machine_capacity, job_qubits, start, duration):
    """Kiểm tra tại thời điểm start, job có thể chạy song song nếu tổng qubits ≤ capacity."""
    load = 0
    for job in machine_schedule:
        if not (start + duration <= job["start"] or start >= job["end"]):  # overlap
            load += job["qubits"]
    return load + job_qubits <= machine_capacity


def find_earliest_start(machine_schedule, machine_capacity, job_qubits):
    """Tìm earliest start cho job trên máy (duration = job_qubits)."""
    duration = job_qubits
    t = 0.0
    step = 1.0
    while True:
        if can_run_at_time(machine_schedule, machine_capacity, job_qubits, t, duration):
            return t
        t += step


def schedule_jobs_ffd(job_capacities, machine_capacities):
    """FFD động với thời gian chạy = qubits."""
    jobs = sorted(job_capacities.items(), key=lambda x: -x[1])  # sort giảm dần
    machines = {name: [] for name in machine_capacities}
    schedule = []

    for job_id, qubit in jobs:
        if qubit == 0:
            continue

        duration = qubit
        best_machine = None
        best_start = float("inf")
        best_entry = None

        # duyệt tất cả máy, chọn máy có earliest start nhỏ nhất
        for machine_name, capacity in machine_capacities.items():
            machine_schedule = machines[machine_name]
            start_time = find_earliest_start(machine_schedule, capacity, qubit)
            end_time = start_time + duration

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

        # gán vào máy tốt nhất
        schedule.append(best_entry)
        machines[best_machine].append(best_entry)

    return schedule


def example_problem(job_capacities, machine_capacities, location):
    nameOutput = f"{location}/schedule.json"
    os.makedirs(os.path.dirname(nameOutput), exist_ok=True)
    schedule = schedule_jobs_ffd(job_capacities, machine_capacities)
    with open(nameOutput, "w") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)
    print(f"Schedule saved to {nameOutput}")
    print("Jobs have Updated Information:")
    return schedule
