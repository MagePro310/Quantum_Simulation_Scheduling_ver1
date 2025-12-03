from abc import ABC, abstractmethod
from typing import List, Tuple, Any, Dict
from dataclasses import dataclass, asdict
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')

from component.a_backend.fake_backend import FakeBelemV2, FakeManilaV2
from component.b_benchmark.mqt_tool import QuantumBenchmark
from component.sup_sys.job_info import JobInfo
from component.c_circuit_work.cutting.width_c import WidthCircuitCutter

@dataclass
class ResultOfSchedule:
    # Proxy information
    numcircuit: int
    nameAlgorithm: str
    averageQubits: float
    nameSchedule: str
    typeMachine: dict
    
    # Calculate metrics
    average_turnaroundTime: float
    average_responseTime: float
    average_fidelity: float
    sampling_overhead: float
    average_throughput: float
    average_utilization: float
    scheduler_latency: float
    makespan: float

class InputPhase(ABC):
    """
    Abstract base class for the Input Phase.
    
    Input: (quantum circuit, priority) and set quantum machine
    Output: (set quantum circuit, priority) and set quantum machine
    """
    
    @abstractmethod
    def execute(self, num_jobs: int, num_qubits_per_job: int) -> Tuple[Dict[str, JobInfo], Dict[str, Any], ResultOfSchedule]:
        """
        Executes the input phase.

        Args:
            num_jobs: Number of jobs.
            num_qubits_per_job: Number of qubits per job.

        Returns:
            A tuple containing:
            - origin_job_info: Dictionary of original jobs.
            - machines: Dictionary of available machines.
            - result_Schedule: Initialized ResultOfSchedule object.
        """
        pass

class ConcreteInputPhase(InputPhase):
    def execute(self, num_jobs: int, num_qubits_per_job: int) -> Tuple[Dict[str, JobInfo], Dict[str, Any], ResultOfSchedule]:
        # Initialize result_Schedule
        result_Schedule = ResultOfSchedule(
            numcircuit=0,
            nameAlgorithm="",
            averageQubits=0.0,
            nameSchedule="",
            typeMachine={},
            average_turnaroundTime=0.0,
            average_responseTime=0.0,
            average_fidelity=0.0,
            sampling_overhead=0.0,
            average_throughput=0.0,
            average_utilization=0.0,
            scheduler_latency=0.0,
            makespan=0.0
        )
        result_Schedule.nameSchedule = "FFD"

        # Define the machines
        machines = {}
        backend0 = FakeBelemV2()
        backend1 = FakeManilaV2()
        machines[backend0.name] = backend0
        machines[backend1.name] = backend0 # Note: In original script backend1 is mapped to backend0 object, keeping as is for fidelity

        # Define benchmark
        jobs = {}
        for i in range(num_jobs):
            job_id = str(i + 1)
            jobs[job_id] = num_qubits_per_job

        # Update info to result_Schedule
        result_Schedule.numcircuit = len(jobs)
        result_Schedule.averageQubits = sum(jobs.values()) / len(jobs)

        # Generate circuits
        origin_job_info = {}

        for job_name, num_qubits in jobs.items():
            circuit, result_Schedule.nameAlgorithm = QuantumBenchmark.create_circuit(num_qubits, job_name)
            origin_job_info[job_name] = JobInfo(
                job_name=job_name,
                qubits=circuit.num_qubits,
                machine=None,
                capacity_machine=0,
                start_time=0.0,
                duration=0.0,
                end_time=0.0,
                childrenJobs=None,
                circuit=circuit,
                result_cut=None,
            )

        # Process job info and cut the circuits if needed
        # Circuit cutting moved to SchedulePhase
            
        return origin_job_info, machines, result_Schedule