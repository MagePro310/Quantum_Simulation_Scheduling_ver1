from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple
import time
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')

from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
from component.d_scheduling.analyze import analyze_cal
from component.d_scheduling.datawork.updateToDict import update_scheduler_jobs
from component.c_circuit_work.cutting.width_c import WidthCircuitCutter
from component.sup_sys.job_info import JobInfo

class SchedulePhase(ABC):
    """
    Abstract base class for the Schedule Phase.
    
    Input: Output of input phase
    Output: Order of quantum circuit on quantum machine
    """
    
    @abstractmethod
    def execute(self, origin_job_info: Dict[str, JobInfo], machines: Dict[str, Any], result_Schedule: Any) -> Tuple[Dict[str, JobInfo], Any, Any]:
        """
        Executes the schedule phase.

        Args:
            origin_job_info: Dictionary of original jobs.
            machines: Dictionary of available machines.
            result_Schedule: ResultOfSchedule object.

        Returns:
            A tuple containing:
            - Updated scheduler_job (with schedule info).
            - Loaded data from schedule.json.
            - Updated result_Schedule object.
        """
        pass

class ConcreteSchedulePhase(SchedulePhase):
    def execute(self, origin_job_info: Dict[str, JobInfo], machines: Dict[str, Any], result_Schedule: Any) -> Tuple[Dict[str, JobInfo], Any, Any]:
        # Process job info and cut the circuits if needed
        process_job_info = origin_job_info.copy()
        
        # Determine max width from machines
        max_width = max(list(machines.values()), key=lambda x: x.num_qubits).num_qubits

        for job_name, job_info in process_job_info.items():
            if job_info.qubits > max_width:
                job_info.childrenJobs = []
                cutter = WidthCircuitCutter(job_info.circuit, max_width)
                result_cut = cutter.gate_to_reduce_width()
                result_Schedule.sampling_overhead += result_cut.overhead
                for i, (subcircuit_name, subcircuit) in enumerate(result_cut.subcircuits.items()):
                    job_info.childrenJobs.append(
                        JobInfo(
                            job_name=f"{job_name}_{i+1}",
                            qubits=subcircuit.num_qubits,
                            machine=None,
                            capacity_machine=0,
                            start_time=0.0,
                            duration=0.0,
                            end_time=0.0,
                            childrenJobs=None,
                            circuit=subcircuit,
                            result_cut=None,
                        )
                    )
                job_info.result_cut = result_cut

        # Prepare scheduler jobs
        scheduler_job = {}
        def get_scheduler_jobs(job_info):
            if job_info.childrenJobs is None:
                return {job_info.job_name: job_info}
            scheduler_jobs = {}
            for child_job in job_info.childrenJobs:
                scheduler_jobs.update(get_scheduler_jobs(child_job))
            return scheduler_jobs

        for job_name, job_info in process_job_info.items():
            scheduler_job.update(get_scheduler_jobs(job_info))
            
        # ============================= FFD Algorithm ==============================
        job_capacities_FFD = {job_name: job_info.qubits for job_name, job_info in scheduler_job.items()}
        machine_capacities_FFD = {machine_name: machines[machine_name].num_qubits for machine_name in machines}
        result_Schedule.typeMachine = machine_capacities_FFD
        outputFFD = "component/d_scheduling/scheduleResult/heuristic/FFD"
        
        start_time = time.time()
        FFD_implement.example_problem(job_capacities_FFD, machine_capacities_FFD, outputFFD)
        runtime = time.time() - start_time
        result_Schedule.scheduler_latency = runtime
        
        data = analyze_cal.load_job_data("component/d_scheduling/scheduleResult/heuristic/FFD/schedule.json")
        update_scheduler_jobs(data, scheduler_job)
        # ============================== FFD Algorithm ==============================
        
        return scheduler_job, data, result_Schedule