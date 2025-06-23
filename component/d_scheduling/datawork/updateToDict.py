"""
Job Scheduler Data Update Module

This module provides utilities for updating job scheduling information between
different data structures, maintaining consistency across the scheduling system.

Author: Quantum Simulation Scheduling Team
Date: June 23, 2025
"""

from typing import List, Dict, Set, Optional, Any, Union
import logging
from dataclasses import dataclass
from component.sup_sys.job_info import JobInfo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class UpdateResult:
    """
    Result of a job update operation.
    
    Attributes:
        updated_jobs: Set of job names that were successfully updated
        skipped_jobs: Set of job names that were skipped (not found in scheduler)
        errors: Dict mapping job names to error messages
        total_processed: Total number of jobs processed
    """
    updated_jobs: Set[str]
    skipped_jobs: Set[str]
    errors: Dict[str, str]
    total_processed: int
    
    @property
    def success_rate(self) -> float:
        """Calculate the success rate of the update operation."""
        if self.total_processed == 0:
            return 0.0
        return len(self.updated_jobs) / self.total_processed
    
    @property
    def has_errors(self) -> bool:
        """Check if any errors occurred during the update."""
        return len(self.errors) > 0


class JobSchedulerUpdater:
    """
    A professional utility class for updating job scheduling information.
    
    This class provides methods to synchronize job data between different
    representations while maintaining data integrity and providing comprehensive
    error handling and reporting.
    """
    
    REQUIRED_JOB_FIELDS = {
        'job', 'qubits', 'machine', 'capacity', 'start', 'duration', 'end'
    }
    
    @staticmethod
    def validate_job_data(job_data: List[Dict[str, Any]]) -> None:
        """
        Validate the structure and content of job data.
        
        Args:
            job_data (List[Dict[str, Any]]): List of job data dictionaries.
            
        Raises:
            TypeError: If job_data is not a list or contains non-dict elements.
            ValueError: If job data is empty or missing required fields.
        """
        if not isinstance(job_data, list):
            raise TypeError(f"job_data must be a list, got {type(job_data).__name__}")
        
        if not job_data:
            raise ValueError("job_data cannot be empty")
        
        for i, job in enumerate(job_data):
            if not isinstance(job, dict):
                raise TypeError(f"job_data[{i}] must be a dictionary, got {type(job).__name__}")
            
            missing_fields = JobSchedulerUpdater.REQUIRED_JOB_FIELDS - set(job.keys())
            if missing_fields:
                raise ValueError(
                    f"job_data[{i}] missing required fields: {missing_fields}. "
                    f"Required fields: {JobSchedulerUpdater.REQUIRED_JOB_FIELDS}"
                )
            
            # Validate data types for critical fields
            try:
                job_id = str(job['job'])
                qubits = int(job['qubits'])
                capacity = int(job['capacity'])
                start_time = float(job['start'])
                duration = float(job['duration'])
                end_time = float(job['end'])
                machine = str(job['machine'])
                
                # Validate logical constraints
                if qubits <= 0:
                    raise ValueError(f"job_data[{i}]: qubits must be positive, got {qubits}")
                if capacity <= 0:
                    raise ValueError(f"job_data[{i}]: capacity must be positive, got {capacity}")
                if duration < 0:
                    raise ValueError(f"job_data[{i}]: duration cannot be negative, got {duration}")
                if start_time < 0:
                    raise ValueError(f"job_data[{i}]: start time cannot be negative, got {start_time}")
                if end_time < start_time:
                    raise ValueError(f"job_data[{i}]: end time ({end_time}) cannot be before start time ({start_time})")
                if not machine.strip():
                    raise ValueError(f"job_data[{i}]: machine name cannot be empty")
                    
            except (ValueError, TypeError) as e:
                raise ValueError(f"job_data[{i}] has invalid data types or values: {e}")
    
    @staticmethod
    def validate_scheduler_jobs(scheduler_job: Dict[str, JobInfo]) -> None:
        """
        Validate the scheduler job dictionary.
        
        Args:
            scheduler_job (Dict[str, JobInfo]): Dictionary of JobInfo objects.
            
        Raises:
            TypeError: If scheduler_job is not a dict or contains non-JobInfo values.
            ValueError: If scheduler_job is empty.
        """
        if not isinstance(scheduler_job, dict):
            raise TypeError(f"scheduler_job must be a dictionary, got {type(scheduler_job).__name__}")
        
        if not scheduler_job:
            raise ValueError("scheduler_job dictionary cannot be empty")
        
        for job_name, job_info in scheduler_job.items():
            if not isinstance(job_name, str):
                raise TypeError(f"Job name must be a string, got {type(job_name).__name__}")
            if not isinstance(job_info, JobInfo):
                raise TypeError(f"Job info for '{job_name}' must be a JobInfo instance, got {type(job_info).__name__}")
    
    @staticmethod
    def update_scheduler_jobs(
        job_data: List[Dict[str, Any]], 
        scheduler_job: Dict[str, JobInfo],
        validate_inputs: bool = True,
        strict_mode: bool = False
    ) -> UpdateResult:
        """
        Update scheduler job objects with information from job data.
        
        This method synchronizes job scheduling information between different
        data representations, ensuring consistency across the system.
        
        Args:
            job_data (List[Dict[str, Any]]): List of job data dictionaries containing
                scheduling information with keys: 'job', 'qubits', 'machine', 
                'capacity', 'start', 'duration', 'end'.
            scheduler_job (Dict[str, JobInfo]): Dictionary mapping job names to
                JobInfo objects to be updated.
            validate_inputs (bool): Whether to validate input data. Default is True.
            strict_mode (bool): If True, raises exception for any job not found
                in scheduler_job. If False, skips missing jobs. Default is False.
        
        Returns:
            UpdateResult: Comprehensive result of the update operation including
                success/failure statistics and detailed information.
            
        Raises:
            TypeError: If inputs have incorrect types.
            ValueError: If inputs are invalid or strict_mode is True and jobs are missing.
            
        Example:
            >>> updater = JobSchedulerUpdater()
            >>> job_data = [
            ...     {'job': '1', 'qubits': 2, 'machine': 'qpu1', 'capacity': 5, 
            ...      'start': 0.0, 'end': 100.0, 'duration': 100.0}
            ... ]
            >>> scheduler_jobs = {'1': JobInfo()}
            >>> result = updater.update_scheduler_jobs(job_data, scheduler_jobs)
            >>> print(f"Updated {len(result.updated_jobs)} jobs successfully")
        """
        if validate_inputs:
            JobSchedulerUpdater.validate_job_data(job_data)
            JobSchedulerUpdater.validate_scheduler_jobs(scheduler_job)
        
        updated_jobs = set()
        skipped_jobs = set()
        errors = {}
        
        logger.info(f"Starting update of {len(job_data)} jobs")
        
        for i, job in enumerate(job_data):
            job_name = str(job['job'])
            
            try:
                if job_name not in scheduler_job:
                    if strict_mode:
                        raise ValueError(f"Job '{job_name}' not found in scheduler_job dictionary")
                    else:
                        skipped_jobs.add(job_name)
                        logger.warning(f"Job '{job_name}' not found in scheduler, skipping")
                        continue
                
                # Update JobInfo object with new data
                job_info = scheduler_job[job_name]
                job_info.qubits = int(job['qubits'])
                job_info.machine = str(job['machine'])
                job_info.capacity_machine = int(job['capacity'])
                job_info.start_time = float(job['start'])
                job_info.duration = float(job['duration'])
                job_info.end_time = float(job['end'])
                
                updated_jobs.add(job_name)
                logger.debug(f"Successfully updated job '{job_name}'")
                
            except Exception as e:
                error_msg = f"Failed to update job '{job_name}': {str(e)}"
                errors[job_name] = error_msg
                logger.error(error_msg)
        
        result = UpdateResult(
            updated_jobs=updated_jobs,
            skipped_jobs=skipped_jobs,
            errors=errors,
            total_processed=len(job_data)
        )
        
        logger.info(f"Update completed: {len(updated_jobs)} updated, {len(skipped_jobs)} skipped, {len(errors)} errors")
        
        return result
    
    @staticmethod
    def print_update_summary(
        result: UpdateResult, 
        show_details: bool = True,
        show_job_info: bool = False,
        scheduler_job: Optional[Dict[str, JobInfo]] = None
    ) -> None:
        """
        Print a comprehensive summary of the update operation.
        
        Args:
            result (UpdateResult): Result of the update operation.
            show_details (bool): Whether to show detailed job lists. Default is True.
            show_job_info (bool): Whether to show updated job information. Default is False.
            scheduler_job (Optional[Dict[str, JobInfo]]): Scheduler job dictionary for
                displaying job information. Required if show_job_info is True.
        """
        print("\n" + "="*60)
        print("JOB SCHEDULER UPDATE SUMMARY")
        print("="*60)
        
        # Overall statistics
        print(f"\n📊 OPERATION STATISTICS:")
        print(f"   • Total Jobs Processed:    {result.total_processed}")
        print(f"   • Successfully Updated:    {len(result.updated_jobs)}")
        print(f"   • Skipped (Not Found):     {len(result.skipped_jobs)}")
        print(f"   • Errors Encountered:      {len(result.errors)}")
        print(f"   • Success Rate:            {result.success_rate:.1%}")
        
        if show_details:
            # Updated jobs
            if result.updated_jobs:
                print(f"\n✅ SUCCESSFULLY UPDATED JOBS:")
                for job_name in sorted(result.updated_jobs):
                    print(f"   • {job_name}")
            
            # Skipped jobs
            if result.skipped_jobs:
                print(f"\n⚠️  SKIPPED JOBS (Not Found):")
                for job_name in sorted(result.skipped_jobs):
                    print(f"   • {job_name}")
            
            # Errors
            if result.errors:
                print(f"\n❌ ERRORS:")
                for job_name, error_msg in result.errors.items():
                    print(f"   • {job_name}: {error_msg}")
        
        # Job information display
        if show_job_info and scheduler_job and result.updated_jobs:
            print(f"\n📋 UPDATED JOB INFORMATION:")
            for job_name in sorted(result.updated_jobs):
                if job_name in scheduler_job:
                    job_info = scheduler_job[job_name]
                    print(f"\n   Job: {job_name}")
                    print(f"   ├─ Machine: {job_info.machine}")
                    print(f"   ├─ Qubits: {job_info.qubits}")
                    print(f"   ├─ Capacity: {job_info.capacity_machine}")
                    print(f"   ├─ Start Time: {job_info.start_time}")
                    print(f"   ├─ Duration: {job_info.duration}")
                    print(f"   └─ End Time: {job_info.end_time}")
        
        print("="*60)
    
    @staticmethod
    def verify_update_consistency(
        job_data: List[Dict[str, Any]], 
        scheduler_job: Dict[str, JobInfo]
    ) -> Dict[str, List[str]]:
        """
        Verify consistency between job data and updated scheduler jobs.
        
        Args:
            job_data (List[Dict[str, Any]]): Original job data.
            scheduler_job (Dict[str, JobInfo]): Updated scheduler jobs.
            
        Returns:
            Dict[str, List[str]]: Dictionary containing inconsistencies found.
        """
        inconsistencies = {
            'missing_jobs': [],
            'data_mismatches': [],
            'timing_errors': []
        }
        
        for job in job_data:
            job_name = str(job['job'])
            
            if job_name not in scheduler_job:
                inconsistencies['missing_jobs'].append(job_name)
                continue
            
            job_info = scheduler_job[job_name]
            
            # Check data consistency
            if (job_info.qubits != int(job['qubits']) or
                job_info.machine != str(job['machine']) or
                job_info.capacity_machine != int(job['capacity'])):
                inconsistencies['data_mismatches'].append(job_name)
            
            # Check timing consistency
            if (abs(job_info.start_time - float(job['start'])) > 1e-6 or
                abs(job_info.duration - float(job['duration'])) > 1e-6 or
                abs(job_info.end_time - float(job['end'])) > 1e-6):
                inconsistencies['timing_errors'].append(job_name)
        
        return inconsistencies


# Legacy function for backward compatibility
def update_scheduler_jobs(
    job_data: List[Dict], 
    scheduler_job: Dict[str, JobInfo]
) -> None:
    """
    Legacy wrapper function for backward compatibility.
    
    Args:
        job_data (List[Dict]): List of job data dictionaries.
        scheduler_job (Dict[str, JobInfo]): Dictionary of JobInfo objects.
        
    Note:
        This function is maintained for backward compatibility.
        New code should use JobSchedulerUpdater.update_scheduler_jobs().
    """
    result = JobSchedulerUpdater.update_scheduler_jobs(job_data, scheduler_job)
    
    # Maintain original behavior with print statement
    print("Jobs have Updated Information:")
    
    # Print summary for better user experience
    if result.has_errors or result.skipped_jobs:
        JobSchedulerUpdater.print_update_summary(result, show_details=False)