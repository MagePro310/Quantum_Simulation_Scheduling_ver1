from abc import ABC, abstractmethod
from typing import Any, Dict
import json
import os
from dataclasses import asdict
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')

from component.d_scheduling.analyze import analyze_cal
from component.sup_sys.job_info import JobInfo

class ResultPhase(ABC):
    """
    Abstract base class for the Result Phase.
    
    Input: Output of execution phase
    Output: Result of quantum circuit after execution on quantum machine.
    """
    
    @abstractmethod
    def execute(self, scheduler_job: Dict[str, JobInfo], origin_job_info: Dict[str, JobInfo], data: Any, utilization_permachine: Any, result_Schedule: Any) -> Any:
        """
        Executes the result phase.
        
        This phase makes some calculation for analyze the result of quantum circuit.

        Args:
            scheduler_job: Dictionary of scheduled jobs.
            origin_job_info: Original job info.
            data: Data loaded from schedule.json.
            utilization_permachine: Utilization metrics.
            result_Schedule: ResultOfSchedule object.

        Returns:
            The final result of the quantum circuit.
        """
        pass

class ConcreteResultPhase(ResultPhase):
    def execute(self, scheduler_job: Dict[str, JobInfo], origin_job_info: Dict[str, JobInfo], data: Any, utilization_permachine: Any, result_Schedule: Any) -> Any:
        # Check if have children jobs in origin_job_info
        for job_name, job_info in origin_job_info.items():
            if job_info.childrenJobs is not None:
                count_fidelity = 0
                for child_job in job_info.childrenJobs:
                    #update start time and end time from child job to parent job
                    job_info.start_time = min(job_info.start_time, child_job.start_time)
                    job_info.end_time = max(job_info.end_time, child_job.end_time)
                    job_info.duration = job_info.end_time - job_info.start_time
                    count_fidelity += child_job.fidelity * child_job.qubits
                job_info.fidelity = count_fidelity / job_info.qubits
            else:
                # If no children, fidelity is already set in scheduler_job which refers to same objects if not cut?
                # Wait, origin_job_info values might be different objects if not careful.
                # In InputPhase, we created origin_job_info.
                # If not cut, scheduler_job has the same JobInfo object.
                # If cut, scheduler_job has children JobInfo objects.
                # So if not cut, we need to ensure fidelity is set on origin_job_info's object.
                # In ExecutionPhase, we updated scheduler_job.
                # If not cut, scheduler_job[job_name] IS origin_job_info[job_name].
                # So fidelity should be there.
                pass
                # print(f"Job {job_name} has no children jobs.")
                
        metrics = analyze_cal.calculate_metrics(data, utilization_permachine)
        analyze_cal.print_metrics(metrics)
        
        result_Schedule.average_turnaroundTime = metrics['average_turnaroundTime']
        result_Schedule.average_responseTime = metrics['average_responseTime']
        result_Schedule.makespan = metrics['makespan']
        result_Schedule.average_utilization = metrics['average_utilization']
        result_Schedule.average_throughput = metrics['throughput']
        
        # Calculate all the values of components
        sum_fidelity = 0
        for job_name, job_info in origin_job_info.items():
            sum_fidelity += job_info.fidelity * job_info.qubits
        average_fidelity = sum_fidelity / (result_Schedule.averageQubits * result_Schedule.numcircuit)
        result_Schedule.average_fidelity = average_fidelity
        
        
        algorithm_folder_path = os.path.join("component", "finalResult","5_5", result_Schedule.nameSchedule, result_Schedule.nameAlgorithm)
        os.makedirs(algorithm_folder_path, exist_ok=True)
        
        # Construct the base file name
        numcircuit = result_Schedule.numcircuit
        numqubit = result_Schedule.averageQubits
        base_filename = f"{numcircuit}_{numqubit}"
        
        # Ensure the filename is unique
        existing_files = os.listdir(algorithm_folder_path)
        matching_files = [f for f in existing_files if f.startswith(base_filename) and f.endswith(".json")]
        
        if not matching_files:
            final_filename = f"{base_filename}_0.json"
        else:
            suffixes = [
                int(f.replace(base_filename, "").replace(".json", "").replace("_", ""))
                for f in matching_files
                if f.replace(base_filename, "").replace(".json", "").replace("_", "").isdigit()
            ]
            next_suffix = max(suffixes, default=0) + 1
            final_filename = f"{base_filename}_{next_suffix}.json"
        
        # Define the output file path
        output_file_path = os.path.join(algorithm_folder_path, final_filename)
        
        # Save the result to the JSON file
        with open(output_file_path, "w") as f:
            json.dump(asdict(result_Schedule), f, indent=4)
        
        # Print the result
        print(f"Result saved to {output_file_path}")
        
        return result_Schedule
