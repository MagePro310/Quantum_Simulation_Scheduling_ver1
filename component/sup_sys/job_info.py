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
    knitted_circuit: QuantumCircuit = None
    transpiled_circuit_measured: QuantumCircuit = None
    
    # Help for fidelity
    fidelity: float = None
    
    # Define function print
    
    def print(self):
        """
        Print the job information.
        """
        print(f"Job ID: {self.job_id}")
        print(f"Job Name: {self.job_name}")
        print(f"Circuit: {self.circuit}")
        print(f"Qubits: {self.qubits}")
        print(f"Machine: {self.machine}")
        print(f"Capacity Machine: {self.capacity_machine}")
        print(f"Start Time: {self.start_time}")
        print(f"Duration: {self.duration}")
        print(f"End Time: {self.end_time}")
        print(f"Children Jobs: {self.childrenJobs}")
        print(f"Result Cut: {self.result_cut}")
        print(f"Transpiled Circuit: {self.transpiled_circuit}")
        print(f"Knitted Circuit: {self.knitted_circuit}")
        print(f"Transpiled Circuit Measured: {self.transpiled_circuit_measured}")
        print(f"Fidelity: {self.fidelity}")
        print("=========================================")