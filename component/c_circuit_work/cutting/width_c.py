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
class Result_of_cutting:
    sub_circuits: list[QuantumCircuit]
    overhead: float # The overhead of the circuit cutting

def gate_to_reduce_width(qc: QuantumCircuit, cutname: str) -> dict[QuantumCircuit]:
    observable = SparsePauliOp(["ZZII", "IZZI", "-IIZZ", "XIXI", "ZIZZ", "IXIX"])  
    partitioned_problem = partition_problem(
        circuit= qc, partition_labels="AAAAABBB", observables=observable.paulis
    )
    subcircuits = partitioned_problem.subcircuits
    subobservables = partitioned_problem.subobservables
    bases = partitioned_problem.bases
    overhead = np.prod([basis.overhead for basis in bases])
    
    return subcircuits 
      

def wire_to_reduce_width():
    # Devide the circuit into many parts following the depth
    # and then add a cut wire gate to the circuit
    # After that merge the parts of the circuit
    # Return the new circuit
    # Apply the cut move to the circuit
    # Then cutting as two parts
    # return new two circuits
    pass