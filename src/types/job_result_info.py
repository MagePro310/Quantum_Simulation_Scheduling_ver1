from dataclasses import dataclass

@dataclass
class JobResultInfo:
    """Helper to keep track of job results."""

    name: str
    machine: str
    start_time: float
    completion_time: float
    capacity: int