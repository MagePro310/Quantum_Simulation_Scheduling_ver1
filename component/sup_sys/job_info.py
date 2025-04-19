from dataclasses import dataclass
from qiskit import QuantumCircuit
import uuid
from component.c_circuit_work.cutting.width_c import SubCircuitInfo

@dataclass
class JobInfo:
    """
    Class to store job information.
    """

    job_id: str = str(uuid.uuid4())
    job_name: str = None
    circuit: QuantumCircuit = None
    qubits: int = 0
    machine: str = None
    capacity_machine: int = 0
    start_time: float = 0
    duration: float = 0
    end_time: float = 0

    childrenJobs: list['JobInfo'] = None
    
    # Help for cut
    result_cut: SubCircuitInfo = None
    
    # Help for transpile
    transpiled_circuit: QuantumCircuit = None
    
    # Help for fidelity
    fidelity: float = None