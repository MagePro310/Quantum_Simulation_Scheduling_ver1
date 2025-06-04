from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import SamplerV2, Batch
from qiskit_aer.primitives import EstimatorV2
from qiskit_addon_cutting import (
    cut_gates,
    partition_problem,
    generate_cutting_experiments,
    reconstruct_expectation_values,
)
from qiskit.quantum_info import SparsePauliOp
from dataclasses import dataclass
import numpy as np
import math

@dataclass
class SubCircuitInfo:
    circuit_origin: QuantumCircuit
    observable: SparsePauliOp
    subcircuits: dict
    subobservables: dict
    bases: list
    overhead: float

class WidthCircuitCutter:
    def __init__(self, circuit: QuantumCircuit, max_width: int):
        self.circuit = circuit
        self.max_width = max_width
        self.cutname, self.observable = self.gate_cut_width(self.circuit, self.max_width)
        self.subcircuit_info = None

    @staticmethod
    def has_measurement(circuit: QuantumCircuit) -> bool:
        for instr in circuit.data:
            if instr.operation.name == 'measure':
                return True
        return False

    def gate_to_reduce_width(self):
        qc = self.circuit
        observable = self.observable
        cut_name = self.cutname
        result = SubCircuitInfo(qc, observable, {}, {}, [], 0.0)
        if self.has_measurement(qc):
            qc.remove_final_measurements()
        partitioned_problem = partition_problem(
            circuit=qc, partition_labels=cut_name, observables=observable.paulis
        )
        result.subcircuits = partitioned_problem.subcircuits
        result.subobservables = partitioned_problem.subobservables
        result.bases = partitioned_problem.bases
        result.overhead = np.prod([basis.overhead for basis in result.bases])
        self.subcircuit_info = result
        return result

    @staticmethod
    def gate_cut_width(circuit: QuantumCircuit, max_width: int):
        num_qubits = circuit.num_qubits
        num_of_part = math.ceil(num_qubits / max_width)
        alphabet = [chr(i) for i in range(65, 65 + num_of_part)]
        cutname = ""
        for i in range(num_qubits):
            cutname += alphabet[i // max_width]
        list_observables = ["I"]
        observables = []
        for i in range(num_of_part):
            for k in range(len(list_observables)):
                observable_temp = ""
                for j in range(num_qubits):
                    index = j // len(list_observables) + k
                    if (index >= len(list_observables)):
                        index = 0
                    observable_temp += list_observables[index]
                observables.append(observable_temp)
        unique_observables = list(dict.fromkeys(observables))
        observable = SparsePauliOp(unique_observables)
        return cutname, observable

    # You can add more methods here for subexperiment preparation, running, etc.

# Example usage:
# cutter = WidthCircuitCutter(my_circuit, max_width=3)
# subcircuit_info = cutter.gate_to_reduce_width()