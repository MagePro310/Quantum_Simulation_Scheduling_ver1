from qiskit import QuantumCircuit
from dataclasses import dataclass
from qiskit_addon_cutting import (
    cut_gates,
    partition_problem,
    generate_cutting_experiments,
    reconstruct_expectation_values,
)
import numpy as np
from qiskit.quantum_info import SparsePauliOp

@dataclass
class subCircuit_info:
    """
    Class to store information about subcircuits and their observables.
    """
    subcircuits: dict[QuantumCircuit]
    subobservables: dict[SparsePauliOp]
    bases: list
    overhead: float
    
    
    
def has_measurement(circuit: QuantumCircuit) -> bool:
    # Iterate over all instructions in the circuit
    for instr in circuit.data:
        if instr.operation.name == 'measure':  # Check if the operation name is 'measure'
            return True
    return False

def create_string(num_char, num_dif, position: list):
    """
    """
    # Initialize the string with the first character 'A'
    result = ['A'] * num_char
    print(type(result))
    print(result)  
    # Generate the different characters 'A', 'B', 'C', ..., based on num_dif
    char_list = [chr(ord('A') + i) for i in range(num_dif)]
    print(char_list)
    
    # Modify the positions to introduce new characters
    count = 0
    print(len(position))
    for i in range(len(result)):
        print(type(i))
        print(i)
        if (i) == position[count]:
            count += 1
        result[i] = char_list[count]
    
    # Convert the list back to a string and return
    return ''.join(result)

# Truyen vao circuit, cat o vi tri nao
def gate_to_reduce_width(qc: QuantumCircuit, cut_name: str) -> subCircuit_info:
    result = subCircuit_info({}, {}, [], 0.0)
    if has_measurement(qc):
        qc.remove_final_measurements()
    
    observable = SparsePauliOp(["ZZII", "IZZI", "-IIZZ", "XIXI", "ZIZZ", "IXIX"])
    partitioned_problem = partition_problem(
        circuit=qc, partition_labels= cut_name, observables= observable.paulis
    )
    result.subcircuits = partitioned_problem.subcircuits
    result.subobservables = partitioned_problem.subobservables
    result.bases = partitioned_problem.bases
    result.overhead = np.prod([basis.overhead for basis in result.bases])
    
    # for key, value in result.subcircuits.items():
    #     result.subcircuits[key].data = [hasChange for hasChange in value.data if hasChange.operation.name != "qpd_1q"]
            
    return result

def wire_to_reduce_width():
    # Devide the circuit into many parts following the depth
    # and then add a cut wire gate to the circuit
    # After that merge the parts of the circuit
    # Return the new circuit
    # Apply the cut move to the circuit
    # Then cutting as two parts
    # return new two circuits
    pass