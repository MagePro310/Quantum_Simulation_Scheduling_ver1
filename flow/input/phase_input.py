from abc import ABC, abstractmethod
from typing import List, Tuple, Any, Dict
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')


from component.b_benchmark.mqt_tool import QuantumBenchmark
from component.sup_sys.job_info import JobInfo
from component.a_backend.fake_backend import FakeBelemV2, FakeManilaV2

class InputPhase(ABC):
    """
    Abstract base class for the Input Phase.
    
    Input: (quantum circuit, priority) and set quantum machine
    Output: (set quantum circuit, priority) and set quantum machine
    """
    
    @abstractmethod
    def execute(self, result_Schedule: Any) -> Tuple[Dict[str, JobInfo], Dict[str, Any], Any]:
        """
        Executes the input phase.

        Args:
            num_jobs: Number of jobs.
            num_qubits_per_job: Number of qubits per job.
            result_Schedule: ResultOfSchedule object.

        Returns:
            A tuple containing:
            - origin_job_info: Dictionary of original jobs.
            - machines: Dictionary of machines.
            - result_Schedule: Updated ResultOfSchedule object.
        """
        pass

class ConcreteInputPhase(InputPhase):
    def execute(self, result_Schedule: Any) -> Tuple[Dict[str, JobInfo], Dict[str, Any], Any]:
        # Initialize result_Schedule
        result_Schedule.nameSchedule = "FFD"

        num_jobs = 2
        num_qubits_per_job = 4
        machines = {}
        backend0 = FakeBelemV2()
        backend1 = FakeManilaV2()
        machines[backend0.name] = backend0
        machines[backend1.name] = backend1

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