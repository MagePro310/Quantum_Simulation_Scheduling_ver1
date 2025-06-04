import sys
import json
import os
import time
import numpy as np
from dataclasses import dataclass, asdict
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit_ibm_runtime import SamplerV2

from component.a_backend.fake_backend import *
from component.b_benchmark.mqt_tool import create_circuit
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import gate_cut_width, gate_to_reduce_width
from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
from component.d_scheduling.analyze import analyze_cal
from component.d_scheduling.datawork.updateToDict import update_scheduler_jobs
from component.d_scheduling.simulation.scheduling_multithread import simulate_scheduling
from component.f_assemble.assemble_work import fidelity_from_counts

@dataclass
class ResultOfSchedule:
    # Input parameters
    numcircuit: int
    nameAlgorithm: str
    averageQubits: float
    nameSchedule: str
    typeMachine: dict
    # Results
    average_turnaroundTime: float
    average_responseTime: float
    average_fidelity: float
    sampling_overhead: float
    average_throughput: float
    average_utilization: float
    scheduler_latency: float
    makespan: float

class QuantumScheduler:
    def __init__(self, num_jobs: int, num_qubits_per_job: int):
        self.num_jobs = num_jobs
        self.num_qubits_per_job = num_qubits_per_job
        self.result_schedule = ResultOfSchedule()
        

    def get_config(self):
        return {
            "num_jobs": self.num_jobs,
            "num_qubits_per_job": self.num_qubits_per_job,
            "machines": self.machines,
            "jobs": self.jobs
        }

    def _define_jobs(self):
        return {str(i + 1): self.num_qubits_per_job for i in range(self.num_jobs)}

    def _generate_circuits(self):
        info = {}
        for job_name, num_qubits in self.jobs.items():
            circuit = create_circuit(num_qubits, job_name)
            circuit.remove_final_measurements()
            info[job_name] = JobInfo(job_name, circuit.num_qubits, None, 0, 0.0, 0.0, 0.0, None, circuit, None)
        self.result_schedule.numcircuit = len(info)
        self.result_schedule.averageQubits = sum(self.jobs.values()) / len(self.jobs)
        self.result_schedule.nameAlgorithm = "ghz"
        return info

    def _prepare_scheduler_jobs(self):
        max_width = max(backend.num_qubits for backend in self.machines.values())
        scheduler_job = {}

        def get_scheduler_jobs(job_info):
            if job_info.childrenJobs is None:
                return {job_info.job_name: job_info}
            all_jobs = {}
            for child in job_info.childrenJobs:
                all_jobs.update(get_scheduler_jobs(child))
            return all_jobs

        for job_name, job_info in self.origin_job_info.items():
            if job_info.qubits > max_width:
                job_info.childrenJobs = []
                cut_name, observable = gate_cut_width(job_info.circuit, max_width)
                result_cut = gate_to_reduce_width(job_info.circuit, cut_name, observable)
                self.result_schedule.sampling_overhead += result_cut.overhead
                for i, (sub_name, subcircuit) in enumerate(result_cut.subcircuits.items()):
                    job_info.childrenJobs.append(JobInfo(f"{job_name}_{i+1}", subcircuit.num_qubits, None, 0, 0.0, 0.0, 0.0, None, subcircuit, None))
                job_info.result_cut = result_cut
            scheduler_job.update(get_scheduler_jobs(job_info))
        return scheduler_job

    def schedule_and_simulate(self):
        job_cap = {job: info.qubits for job, info in self.scheduler_jobs.items()}
        machine_cap = {name: backend.num_qubits for name, backend in self.machines.items()}
        self.result_schedule.typeMachine = machine_cap

        start = time.time()
        FFD_implement.example_problem(job_cap, machine_cap, "component/d_scheduling/scheduleResult/heuristic/FFD")
        self.result_schedule.scheduler_latency = time.time() - start

        data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/heuristic/FFD/schedule.json")
        update_scheduler_jobs(data, self.scheduler_jobs)
        updated_jobs = simulate_scheduling(data, self.scheduler_jobs)
        return data, updated_jobs

    def transpile_and_simulate(self, data):
        for job_id, job in self.scheduler_jobs.items():
            backend = self.machines.get(job.machine)
            if backend:
                job.circuit.measure_all()
                job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                result = self.aer_simulator.run(job.transpiled_circuit_measured, shots=1024).result()
                ideal_counts = result.get_counts(job.transpiled_circuit_measured)
                job_result = SamplerV2(backend).run([job.transpiled_circuit_measured], shots=1024).result()[0]
                sim_counts = job_result.data.meas.get_counts()
                fidelity, _, _ = fidelity_from_counts(ideal_counts, sim_counts)
                job.fidelity = fidelity

    def compute_metrics(self, data):
        util = analyze_cal.calculate_utilization(data)
        metrics = analyze_cal.calculate_metrics(data, util)
        analyze_cal.print_metrics(metrics)

        self.result_schedule.average_turnaroundTime = metrics['average_turnaroundTime']
        self.result_schedule.average_responseTime = metrics['average_responseTime']
        self.result_schedule.makespan = metrics['makespan']
        self.result_schedule.average_utilization = metrics['average_utilization']
        self.result_schedule.average_throughput = metrics['throughput']

        total_fidelity = 0
        for job_name, job_info in self.origin_job_info.items():
            if job_info.childrenJobs:
                f_sum = sum(child.fidelity * child.qubits for child in job_info.childrenJobs)
                job_info.fidelity = f_sum / job_info.qubits
            total_fidelity += job_info.fidelity * job_info.qubits

        self.result_schedule.average_fidelity = total_fidelity / (self.result_schedule.averageQubits * self.result_schedule.numcircuit)

    def save_result(self):
        path = os.path.join("component", "finalResult", "5_5", self.result_schedule.nameSchedule, self.result_schedule.nameAlgorithm)
        os.makedirs(path, exist_ok=True)

        base_name = f"{self.result_schedule.numcircuit}_{self.result_schedule.averageQubits}"
        existing = [f for f in os.listdir(path) if f.startswith(base_name) and f.endswith(".json")]

        if not existing:
            filename = f"{base_name}_0.json"
        else:
            suffix = max([int(f.replace(base_name, '').replace('.json', '').replace('_', '')) for f in existing if f.replace(base_name, '').replace('.json', '').replace('_', '').isdigit()] + [0]) + 1
            filename = f"{base_name}_{suffix}.json"

        with open(os.path.join(path, filename), "w") as f:
            json.dump(asdict(self.result_schedule), f, indent=4)

        print(f"Result saved to {os.path.join(path, filename)}")

if __name__ == '__main__':
    num_jobs = int(sys.argv[1])
    num_qubits_per_job = int(sys.argv[2])

    scheduler = QuantumScheduler(num_jobs, num_qubits_per_job)
    schedule_data, updated_jobs = scheduler.schedule_and_simulate()
    scheduler.transpile_and_simulate(schedule_data)
    scheduler.compute_metrics(schedule_data)
    scheduler.save_result()
