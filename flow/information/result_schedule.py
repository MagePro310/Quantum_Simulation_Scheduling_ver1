from dataclasses import dataclass, field

@dataclass
class ResultOfSchedule:
    # Proxy information
    numcircuit: int = 0
    nameAlgorithm: str = ""
    averageQubits: float = 0.0
    nameSchedule: str = ""
    typeMachine: dict = field(default_factory=dict)
    
    # Calculate metrics
    average_turnaroundTime: float = 0.0
    average_responseTime: float = 0.0
    average_fidelity: float = 0.0
    sampling_overhead: float = 0.0
    average_throughput: float = 0.0
    average_utilization: float = 0.0
    scheduler_latency: float = 0.0
    makespan: float = 0.0
