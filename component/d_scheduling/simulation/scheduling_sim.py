"""
Unified Quantum Circuit Scheduling Simulation Module

This module provides both single-threaded and multi-threaded functionality for simulating 
quantum circuit scheduling across multiple quantum backend machines with resource constraints.
"""

from typing import List, Dict, Any, Union, Optional
from dataclasses import dataclass
from enum import Enum
import logging
import threading
import concurrent.futures

# Configure logging
logger = logging.getLogger(__name__)


class BackendType(Enum):
    """Enumeration of supported quantum computing backends (for backward compatibility)."""
    FAKE_BELEM = 'fake_belem'
    FAKE_MANILA = 'fake_manila'


class SimulationMode(Enum):
    """Enumeration of simulation modes."""
    SINGLE_THREADED = 'single_threaded'
    MULTI_THREADED = 'multi_threaded'


# Constants
class JobKeys:
    """Keys used in job dictionaries."""
    START = 'start'
    END = 'end'
    MACHINE = 'machine'
    JOB_ID = 'job'
    QUBITS = 'qubits'
    CAPACITY = 'capacity'
    DURATION = 'duration'


class SchedulingError(Exception):
    """Custom exception for scheduling-related errors."""
    pass


class InvalidJobDataError(SchedulingError):
    """Raised when job data is invalid or missing required fields."""
    pass


@dataclass
class MachineState:
    """Represents the state of a quantum computing machine."""
    current_time: float = 0.0
    current_capacity: int = 5
    completed_jobs: List[Dict[str, Any]] = None
    ready_queue: List[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.completed_jobs is None:
            self.completed_jobs = []
        if self.ready_queue is None:
            self.ready_queue = []


@dataclass
class ScheduledJob:
    """Represents a scheduled quantum job with all timing information."""
    job_id: str
    machine: str
    start_time: Union[float, int]
    end_time: Union[float, int]
    duration: Union[float, int]
    required_qubits: int
    machine_capacity: int
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format for backward compatibility."""
        return {
            JobKeys.JOB_ID: self.job_id,
            JobKeys.MACHINE: self.machine,
            JobKeys.START: self.start_time,
            JobKeys.END: self.end_time,
            JobKeys.DURATION: self.duration,
            JobKeys.QUBITS: self.required_qubits,
            JobKeys.CAPACITY: self.machine_capacity
        }


class QuantumJobScheduler:
    """
    Unified quantum job scheduler supporting both single-threaded and multi-threaded execution.
    
    This class simulates the scheduling of quantum jobs on multiple
    quantum computing backends with configurable execution modes.
    """
    
    # Constants
    DEFAULT_MACHINE_CAPACITY = 5
    TIME_INCREMENT = 1.0
    
    def __init__(self, machines=None, mode=SimulationMode.SINGLE_THREADED):
        """
        Initialize the quantum job scheduler.
        
        Args:
            machines: Optional dictionary of machine names to initialize.
                     If None, will be set dynamically from job data.
            mode: Simulation mode (single-threaded or multi-threaded)
        """
        if machines is not None:
            self.machines = {machine_name: MachineState() for machine_name in machines}
        else:
            self.machines = {}
        
        self.mode = mode
        self._lock = threading.Lock() if mode == SimulationMode.MULTI_THREADED else None
    
    def get_circuit_duration(self, circuit) -> float:
        """
        Extract the duration from a transpiled quantum circuit.
        
        Args:
            circuit: The transpiled quantum circuit object
            
        Returns:
            float: Duration of the circuit execution
        """
        if not hasattr(circuit, 'duration'):
            error_msg = "Circuit does not have duration attribute"
            logger.error(error_msg)
            raise SchedulingError(error_msg)
        
        try:
            duration = circuit.duration
            if duration is None or duration < 0:
                raise SchedulingError("Circuit duration is invalid (None or negative)")
            
            logger.debug(f"Circuit duration extracted: {duration}")
            return duration
        except Exception as e:
            logger.error(f"Failed to extract circuit duration: {e}")
            raise SchedulingError(f"Failed to extract circuit duration: {e}")
    
    def _initialize_machines_from_jobs(self, jobs: List[Dict[str, Any]]) -> None:
        """
        Initialize machines dynamically based on the machines found in job data.
        
        Args:
            jobs: List of job dictionaries containing machine information
        """
        machine_names = set(job['machine'] for job in jobs)
        
        # Initialize machines if they don't exist
        for machine_name in machine_names:
            if machine_name not in self.machines:
                self.machines[machine_name] = MachineState()
        
        # Reset existing machine states
        for machine_state in self.machines.values():
            machine_state.current_time = 0.0
            machine_state.current_capacity = self.DEFAULT_MACHINE_CAPACITY
            machine_state.completed_jobs.clear()
            machine_state.ready_queue.clear()
    
    def _prepare_jobs(self, jobs: List[Dict[str, Any]], scheduler_job: Dict[str, Any]) -> None:
        """
        Prepare jobs by calculating their duration and end time.
        
        Args:
            jobs: List of job dictionaries to prepare
            scheduler_job: Dictionary containing scheduler job information
        """
        for job in jobs:
            transpiled_circuit = scheduler_job[job['job']].transpiled_circuit
            job['duration'] = self.get_circuit_duration(transpiled_circuit)
            job['end'] = job['start'] + job['duration']
    
    def _validate_job_data(self, job: Dict[str, Any]) -> None:
        """
        Validate that a job contains all required fields.
        
        Args:
            job: Job dictionary to validate
            
        Raises:
            InvalidJobDataError: If required fields are missing or invalid
        """
        required_fields = [
            JobKeys.MACHINE, JobKeys.JOB_ID, JobKeys.QUBITS, 
            JobKeys.CAPACITY, JobKeys.START
        ]
        
        for field in required_fields:
            if field not in job:
                raise InvalidJobDataError(f"Missing required field: {field}")
        
        # Validate data types and values
        if not isinstance(job[JobKeys.QUBITS], int) or job[JobKeys.QUBITS] <= 0:
            raise InvalidJobDataError("Qubits must be a positive integer")
        
        if not isinstance(job[JobKeys.CAPACITY], int) or job[JobKeys.CAPACITY] <= 0:
            raise InvalidJobDataError("Capacity must be a positive integer")
        
        if job[JobKeys.QUBITS] > job[JobKeys.CAPACITY]:
            raise InvalidJobDataError("Required qubits cannot exceed machine capacity")
    
    def _calculate_qubits_in_use(self, schedule: List[Dict[str, Any]], time_point: Union[float, int]) -> int:
        """
        Calculate total qubits in use at a specific time point.
        
        Args:
            schedule: List of scheduled jobs
            time_point: Time point to check
            
        Returns:
            Total number of qubits in use at the time point
        """
        active_jobs = [
            job for job in schedule 
            if (job.get(JobKeys.END, 0) > time_point and 
                job.get(JobKeys.START, 0) <= time_point)
        ]
        
        return sum(job.get(JobKeys.QUBITS, 0) for job in active_jobs)
    
    def _get_next_available_time(self, schedule: List[Dict[str, Any]]) -> Optional[Union[float, int]]:
        """
        Find the next time when resources become available.
        
        Args:
            schedule: List of scheduled jobs
            
        Returns:
            Next available time or None if no jobs are scheduled
        """
        if not schedule:
            return None
        
        end_times = [job.get(JobKeys.END) for job in schedule if job.get(JobKeys.END) is not None]
        return min(end_times) if end_times else None
    
    def _find_earliest_valid_start_time(self, schedule: List[Dict[str, Any]], 
                                       preferred_start: Union[float, int],
                                       required_qubits: int, 
                                       machine_capacity: int) -> Union[float, int]:
        """
        Find the earliest valid start time for a job given resource constraints.
        
        Args:
            schedule: Current machine schedule
            preferred_start: Preferred start time for the job
            required_qubits: Number of qubits required by the job
            machine_capacity: Total qubit capacity of the machine
            
        Returns:
            The earliest valid start time
            
        Raises:
            SchedulingError: If resource requirements cannot be satisfied
        """
        if required_qubits > machine_capacity:
            raise SchedulingError(
                f"Job requires {required_qubits} qubits but machine capacity is {machine_capacity}"
            )
        
        current_start = preferred_start
        max_iterations = 1000  # Prevent infinite loops
        iteration_count = 0
        
        while iteration_count < max_iterations:
            qubits_in_use = self._calculate_qubits_in_use(schedule, current_start)
            
            # Check if there's enough capacity
            if qubits_in_use + required_qubits <= machine_capacity:
                logger.debug(
                    f"Found valid start time: {current_start} "
                    f"(qubits in use: {qubits_in_use}/{machine_capacity})"
                )
                return current_start
            
            # Move to next available time slot
            next_time = self._get_next_available_time([
                job for job in schedule 
                if job.get(JobKeys.END, 0) > current_start
            ])
            
            if next_time is None:
                # No more jobs to wait for, this shouldn't happen
                logger.warning("No future jobs found but capacity exceeded")
                break
            
            current_start = next_time
            iteration_count += 1
        
        if iteration_count >= max_iterations:
            raise SchedulingError("Maximum scheduling iterations exceeded")
        
        return current_start
    
    # Single-threaded implementation methods
    def _filter_jobs_by_machine(self, jobs: List[Dict[str, Any]], 
                               machine_type: str) -> List[Dict[str, Any]]:
        """Filter jobs by machine type."""
        return [job for job in jobs if job['machine'] == machine_type]
    
    def _can_schedule_job(self, job: Dict[str, Any], current_time: float, 
                         current_capacity: int) -> bool:
        """Check if a job can be scheduled at the current time."""
        return (job['start'] <= current_time and 
                job['qubits'] <= current_capacity)
    
    def _move_ready_jobs_to_queue(self, jobs: List[Dict[str, Any]], 
                                 machine_state: MachineState) -> None:
        """Move jobs that are ready to execute to the ready queue."""
        for job in jobs[:]:  # Create a copy to safely modify during iteration
            if self._can_schedule_job(job, machine_state.current_time, 
                                    machine_state.current_capacity):
                machine_state.ready_queue.append(job)
                machine_state.current_capacity -= job['qubits']
    
    def _execute_ready_jobs(self, jobs: List[Dict[str, Any]], 
                           machine_state: MachineState) -> None:
        """Execute all jobs in the ready queue."""
        if not machine_state.ready_queue:
            return
        
        max_end_time = machine_state.current_time
        
        for job in machine_state.ready_queue:
            # Update job timing
            job['start'] = machine_state.current_time
            job['end'] = job['start'] + job['duration']
            max_end_time = max(max_end_time, job['end'])
            
            # Release capacity and move job to completed
            machine_state.current_capacity += job['qubits']
            jobs.remove(job)
            machine_state.completed_jobs.append(job)
        
        # Clear ready queue and update current time
        machine_state.ready_queue.clear()
        machine_state.current_time = max_end_time
    
    def _process_machine_jobs_single_threaded(self, jobs: List[Dict[str, Any]], 
                                             machine_type: str) -> None:
        """Process all jobs for a specific machine in single-threaded mode."""
        machine_state = self.machines[machine_type]
        
        while jobs:
            # Move ready jobs to queue
            self._move_ready_jobs_to_queue(jobs, machine_state)
            
            # Execute ready jobs or advance time
            if machine_state.ready_queue:
                self._execute_ready_jobs(jobs, machine_state)
            else:
                machine_state.current_time += self.TIME_INCREMENT
    
    # Multi-threaded implementation methods
    def _process_single_job_multi_threaded(self, job: Dict[str, Any], 
                                          scheduler_jobs: Dict[str, Any],
                                          machine_schedules: Dict[str, List[Dict[str, Any]]]) -> None:
        """Process and schedule a single job in multi-threaded mode."""
        self._validate_job_data(job)
        
        try:
            machine = job[JobKeys.MACHINE]
            job_id = job[JobKeys.JOB_ID]
            required_qubits = job[JobKeys.QUBITS]
            machine_capacity = job[JobKeys.CAPACITY]
            preferred_start = job[JobKeys.START]
            
            # Get job duration from transpiled circuit
            if job_id not in scheduler_jobs:
                raise InvalidJobDataError(f"Job {job_id} not found in scheduler_jobs")
            
            transpiled_circuit = scheduler_jobs[job_id].transpiled_circuit
            job_duration = self.get_circuit_duration(transpiled_circuit)
            
            # Thread-safe access to machine schedules
            with self._lock:
                # Find optimal start time
                optimal_start_time = self._find_earliest_valid_start_time(
                    machine_schedules[machine], 
                    preferred_start, 
                    required_qubits, 
                    machine_capacity
                )
                
                # Update job with scheduling results
                job.update({
                    JobKeys.START: optimal_start_time,
                    JobKeys.END: optimal_start_time + job_duration,
                    JobKeys.DURATION: job_duration
                })
                
                # Add to machine schedule
                machine_schedules[machine].append(job.copy())
            
            logger.debug(
                f"Scheduled job {job_id} on {machine}: "
                f"start={optimal_start_time}, duration={job_duration}"
            )
            
        except KeyError as e:
            error_msg = f"Missing key in job or scheduler data: {e}"
            logger.error(error_msg)
            raise InvalidJobDataError(error_msg)
        except Exception as e:
            error_msg = f"Failed to process job {job.get(JobKeys.JOB_ID, 'unknown')}: {e}"
            logger.error(error_msg)
            raise SchedulingError(error_msg)
    
    def _extract_available_machines(self, jobs: List[Dict[str, Any]]) -> List[str]:
        """Extract unique machine identifiers from job list."""
        machines = {job[JobKeys.MACHINE] for job in jobs if JobKeys.MACHINE in job}
        if not machines:
            raise InvalidJobDataError("No machines found in job data")
        
        machine_list = list(machines)
        logger.info(f"Detected available machines: {machine_list}")
        return machine_list
    
    def _create_machine_schedules(self, machines: List[str]) -> Dict[str, List[Dict[str, Any]]]:
        """Initialize empty schedules for all machines."""
        return {machine: [] for machine in machines}
    
    def simulate_scheduling(self, jobs: List[Dict[str, Any]], 
                          scheduler_job: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Simulate quantum job scheduling across multiple backends.
        
        This method simulates the scheduling of quantum jobs on available
        quantum computing backends, taking into account resource constraints
        and job dependencies. The simulation mode determines whether to use
        single-threaded or multi-threaded processing.
        
        Args:
            jobs: List of job dictionaries containing job information
            scheduler_job: Dictionary containing scheduler-specific job data
            
        Returns:
            List[Dict[str, Any]]: List of all completed jobs with updated timing
        """
        if not jobs:
            logger.warning("No jobs to schedule")
            return []
        
        if not scheduler_job:
            raise InvalidJobDataError("scheduler_job dictionary is empty")
        
        if self.mode == SimulationMode.SINGLE_THREADED:
            return self._simulate_single_threaded(jobs, scheduler_job)
        else:
            return self._simulate_multi_threaded(jobs, scheduler_job)
    
    def _simulate_single_threaded(self, jobs: List[Dict[str, Any]], 
                                 scheduler_job: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Single-threaded simulation implementation."""
        # Initialize machines dynamically from job data
        self._initialize_machines_from_jobs(jobs)
        
        # Prepare jobs with duration and end time
        self._prepare_jobs(jobs, scheduler_job)
        
        # Group jobs by machine type and process them
        jobs_by_machine = {}
        for machine_name in self.machines.keys():
            jobs_by_machine[machine_name] = self._filter_jobs_by_machine(jobs, machine_name)
        
        # Process jobs for each machine
        for machine_name, machine_jobs in jobs_by_machine.items():
            if machine_jobs:  # Only process if there are jobs for this machine
                self._process_machine_jobs_single_threaded(machine_jobs, machine_name)
        
        # Combine results from all machines
        all_completed_jobs = []
        for machine_state in self.machines.values():
            all_completed_jobs.extend(machine_state.completed_jobs)
        
        return all_completed_jobs
    
    def _simulate_multi_threaded(self, jobs: List[Dict[str, Any]], 
                                scheduler_job: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Multi-threaded simulation implementation."""
        # Extract and validate available machines
        available_machines = self._extract_available_machines(jobs)
        
        # Initialize machine schedules
        machine_schedules = self._create_machine_schedules(available_machines)
        
        # Sort jobs by start time for optimal scheduling
        sorted_jobs = sorted(jobs, key=lambda job: job.get(JobKeys.START, 0))
        
        logger.info(f"Starting multi-threaded simulation for {len(sorted_jobs)} jobs")
        
        # Process jobs using thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(available_machines)) as executor:
            # Submit all jobs for processing
            futures = [
                executor.submit(self._process_single_job_multi_threaded, job, scheduler_job, machine_schedules)
                for job in sorted_jobs
            ]
            
            # Wait for all jobs to complete
            concurrent.futures.wait(futures)
            
            # Check for any exceptions
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Job processing failed: {e}")
                    raise
        
        logger.info("Multi-threaded scheduling simulation completed successfully")
        return sorted_jobs


def create_scheduled_job_from_dict(job_dict: Dict[str, Any]) -> ScheduledJob:
    """
    Create a ScheduledJob object from a dictionary.
    
    Args:
        job_dict: Dictionary containing job information
        
    Returns:
        ScheduledJob object
        
    Raises:
        InvalidJobDataError: If required fields are missing
    """
    try:
        return ScheduledJob(
            job_id=job_dict[JobKeys.JOB_ID],
            machine=job_dict[JobKeys.MACHINE],
            start_time=job_dict[JobKeys.START],
            end_time=job_dict[JobKeys.END],
            duration=job_dict[JobKeys.DURATION],
            required_qubits=job_dict[JobKeys.QUBITS],
            machine_capacity=job_dict[JobKeys.CAPACITY]
        )
    except KeyError as e:
        raise InvalidJobDataError(f"Missing required field for ScheduledJob: {e}")


# Public API functions
def simulate_scheduling(jobs: List[Dict[str, Any]], 
                       scheduler_job: Dict[str, Any],
                       mode: str = 'single_threaded') -> List[Dict[str, Any]]:
    """
    Simulate quantum circuit scheduling across multiple backend machines.
    
    Args:
        jobs: List of job dictionaries containing scheduling information
        scheduler_job: Dictionary mapping job IDs to job objects with transpiled circuits
        mode: Simulation mode ('single_threaded' or 'multi_threaded')
        
    Returns:
        List of scheduled jobs with updated start times, end times, and durations
        
    Raises:
        InvalidJobDataError: If job data is invalid
        SchedulingError: If scheduling fails
    """
    if mode.lower() == 'multi_threaded':
        simulation_mode = SimulationMode.MULTI_THREADED
    else:
        simulation_mode = SimulationMode.SINGLE_THREADED
    
    scheduler = QuantumJobScheduler(mode=simulation_mode)
    return scheduler.simulate_scheduling(jobs, scheduler_job)


def simulate_scheduling_typed(jobs: List[Dict[str, Any]], 
                             scheduler_job: Dict[str, Any],
                             mode: str = 'single_threaded') -> List[ScheduledJob]:
    """
    Typed version of simulate_scheduling that returns ScheduledJob objects.
    
    Args:
        jobs: List of job dictionaries
        scheduler_job: Dictionary mapping job IDs to job objects
        mode: Simulation mode ('single_threaded' or 'multi_threaded')
        
    Returns:
        List of ScheduledJob objects
    """
    scheduled_dicts = simulate_scheduling(jobs, scheduler_job, mode)
    return [create_scheduled_job_from_dict(job) for job in scheduled_dicts]


# Backward compatibility functions
def get_the_duration_from_transpiled_circuit(circuit) -> float:
    """Legacy function for getting circuit duration."""
    scheduler = QuantumJobScheduler()
    return scheduler.get_circuit_duration(circuit)


def extract_circuit_duration(circuit: Any) -> Union[float, int]:
    """Extract the execution duration from a transpiled quantum circuit."""
    scheduler = QuantumJobScheduler()
    return scheduler.get_circuit_duration(circuit)


def simulate_quantum_scheduling(jobs: List[Dict[str, Any]], 
                               scheduler_jobs: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Legacy function for multi-threaded simulation."""
    return simulate_scheduling(jobs, scheduler_jobs, mode='multi_threaded')


def simulate_quantum_scheduling_typed(jobs: List[Dict[str, Any]], 
                                     scheduler_jobs: Dict[str, Any]) -> List[ScheduledJob]:
    """Legacy typed function for multi-threaded simulation."""
    return simulate_scheduling_typed(jobs, scheduler_jobs, mode='multi_threaded')


# Aliases for backward compatibility
get_circuit_duration = extract_circuit_duration
