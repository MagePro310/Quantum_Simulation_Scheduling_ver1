def get_the_duration_from_transpiled_circuit(circuit):
    return circuit.duration

def simulate_scheduling(jobs, scheduler_job):
    machine_schedules = {'fake_belem': [], 'fake_manila': []}
    jobs = sorted(jobs, key=lambda x: x['start'])
    for job in jobs:
        machine = job['machine']
        unique_duration = get_the_duration_from_transpiled_circuit(scheduler_job[job['job']].transpiled_circuit)
        current_schedule = machine_schedules[machine]
        start_time = job['start']
        while True:
            active_jobs = [j for j in current_schedule if j['end'] > start_time]
            total_qubits_in_use = sum(j['qubits'] for j in active_jobs)
            if total_qubits_in_use + job['qubits'] <= job['capacity']:
                break
            start_time = min(j['end'] for j in active_jobs)
        job['start'] = start_time
        job['end'] = start_time + unique_duration
        job['duration'] = unique_duration
        current_schedule.append(job)
    return jobs