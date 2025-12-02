from dataclasses import dataclass
from qiskit import QuantumCircuit

@dataclass
class InputData:
    num_circuits: int
    num_qubits: int
    name_algorithm: str
    
@dataclass
class InputMachine:

    backend_name: str
    num_shots: int
    noise_model: object  # Replace 'object' with the actual type of noise model if known

def input_phase(input_data: InputData, input_machine: InputMachine):

    circuits = []
    machines = []
    for i in range(input_data.num_circuits):
        print(f"Processing circuit {i+1}/{input_data.num_circuits} for algorithm {input_data.name_algorithm}")
        qc = QuantumCircuit(input_data.num_qubits)
        circuits.append(qc)

    for i in range(input_machine.num_shots):
        print(f"Processing shot {i+1}/{input_machine.num_shots} on backend {input_machine.backend_name}")
        machines.append(input_machine)


    return circuits, machines
