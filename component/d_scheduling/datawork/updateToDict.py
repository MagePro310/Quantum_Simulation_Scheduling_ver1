from typing import List, Dict
from component.sup_sys.job_info import JobInfo

def update_scheduler_jobs(job_data: List[Dict], scheduler_job: Dict[str, JobInfo]) -> None:
    """
    Updates the scheduler_job dictionary with information from job_data.

    Args:
        job_data (List[Dict]): List of job data dictionaries containing scheduling information.
        scheduler_job (Dict[str, JobInfo]): Dictionary of JobInfo objects to be updated.
    """
    for job in job_data:
        job_name = job['job']
        if job_name in scheduler_job:
            scheduler_job[job_name].qubits = job['qubits']
            scheduler_job[job_name].machine = job['machine']
            scheduler_job[job_name].capacity_machine = job['capacity']
            scheduler_job[job_name].start_time = job['start']
            scheduler_job[job_name].duration = job['duration']
            scheduler_job[job_name].end_time = job['end']

    print("Jobs have Updated Information:")
    # for job_name, job_info in scheduler_job.items():
    #     job_info.print()