from dataclasses import dataclass

@dataclass
class JobResultInfo:
    """Helper to keep track of job results."""

    name: str
    machine: str
    start_time: float
    completion_time: float
    capacity: int
    
    
@dataclass
class JobResultAnalysis:
    """The data structure to store the result of the analysis."""
    
    name_algorithm: str
    waiting_time: float
    response_time: float
    throughput: float
    utilization: float
    makespan: float