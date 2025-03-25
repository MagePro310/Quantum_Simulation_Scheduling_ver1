from dataclasses import dataclass, field
from enum import Enum, auto

from qiskit import QuantumCircuit
import pulp


@dataclass
class JobResultInfor:
    
    name: str
    assign_machine: int
    start_time: float
    completion_time: float
    JobCapacity: int
      
    def __repr__(self) -> str:
        return (
            f"Job: {self.name}, Machine: {self.assign_machine}, "
            + f"Start Time: {self.start_time:.2f}, "
            + f"Completion Time: {self.completion_time:.2f}, "
            + f"Capacity: {self.capacity}"
        )
        
@dataclass
class ResultInfor:
    """Dataclass for storing the result of a scheduling algorithm.
    """
    
    algorithm: str
    ultilization: float
    through_put: float
    waitting_time: float
    response_time: float
    