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
# from component.sup_sys.job_info import JobInfo

@dataclass
class SubCircuitInfo:
    """
    Class to store information about subcircuits and their observables.
    """
    circuit_origin: QuantumCircuit
    observable: SparsePauliOp
    subcircuits: dict[QuantumCircuit]
    subobservables: dict[SparsePauliOp]
    bases: list
    overhead: float
    subexperiments: dict
    coefficients: list


def has_measurement(circuit: QuantumCircuit) -> bool:
    """
    Check if a quantum circuit contains any measurement operations.
    """
    for instr in circuit.data:
        if instr.operation.name == 'measure':  # Check if the operation name is 'measure'
            return True
    return False


def gate_to_reduce_width(qc: QuantumCircuit, cut_name: str, observable) -> SubCircuitInfo:
    """
    Partition a quantum circuit to reduce its width and return subcircuits with observables.
    """
    result = SubCircuitInfo(qc, observable, {},{},[],0.0,{},[] )
    if has_measurement(qc):
        qc.remove_final_measurements()

    # Partition the problem
    partitioned_problem = partition_problem(
        circuit=qc, partition_labels=cut_name, observables=observable.paulis
    )
    result.subcircuits = partitioned_problem.subcircuits        
    result.subobservables = partitioned_problem.subobservables
    result.bases = partitioned_problem.bases
    result.overhead = np.prod([basis.overhead for basis in result.bases])
    result.subexperiments, result.coefficients = prepare_subexperiments(
    result.subcircuits, result.subobservables, num_samples=np.inf)
    
    
    return result

def greedy_cut(circuit: QuantumCircuit, max_width: int):
    num_qubits = circuit.num_qubits
    num_of_part = math.ceil(num_qubits / max_width)
    alphabet = [chr(i) for i in range(65, 65 + num_of_part)]
    cutname = ""
    for i in range(num_qubits):
        cutname += alphabet[i // max_width]
    
    # Create Observables
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
    # Remove duplicates string in observables
    
    unique_observables = list(dict.fromkeys(observables))
    observable = SparsePauliOp(unique_observables)
    return cutname, observable


def prepare_subexperiments(subcircuits, subobservables, num_samples=np.inf):
    """
    Generate subexperiments and their coefficients.
    """
    return generate_cutting_experiments(
        circuits=subcircuits, observables=subobservables, num_samples=num_samples
    )


def run_subexperiments(subexperiments, backend, optimization_level=1, shots=4096 * 3):
    """
    Execute subexperiments on the backend and retrieve results.
    """
    pass_manager = generate_preset_pass_manager(
        optimization_level=optimization_level, backend=backend
    )

    isa_subexperiments = {
        label: pass_manager.run(partition_subexpts)
        for label, partition_subexpts in subexperiments.items()
    }

    with Batch(backend=backend) as batch:
        sampler = SamplerV2(mode=batch)
        jobs = {
            label: sampler.run(subsystem_subexpts, shots=shots)
            for label, subsystem_subexpts in isa_subexperiments.items()
        }

    # Retrieve results
    return {label: job.result() for label, job in jobs.items()}


def compute_expectation_value(
    results, coefficients, subobservables, observable, circuit
):
    """
    Reconstruct the expectation value and calculate the error estimation.
    """
    # Get expectation values for each observable term
    reconstructed_expval_terms = reconstruct_expectation_values(
        results, coefficients, subobservables
    )

    # Reconstruct final expectation value
    reconstructed_expval = np.dot(reconstructed_expval_terms, observable.coeffs)

    estimator = EstimatorV2()
    exact_expval = (
        estimator.run([(circuit, observable, [0.4] * len(circuit.parameters))])
        .result()[0]
        .data.evs
    )

    error_estimation = np.abs(reconstructed_expval - exact_expval)
    relative_error_estimation = np.abs(
        (reconstructed_expval - exact_expval) / exact_expval
    )

    return reconstructed_expval, exact_expval, error_estimation, relative_error_estimation


def print_results(reconstructed_expval, exact_expval, error_estimation, relative_error_estimation):
    """
    Print the reconstructed and exact expectation values, along with error estimations.
    """
    print(
        f"Reconstructed expectation value: {np.real(np.round(reconstructed_expval, 8))}"
    )
    print(f"Exact expectation value: {np.round(exact_expval, 8)}")
    print(
        f"Error in estimation: {np.real(np.round(error_estimation, 8))}"
    )
    print(
        f"Relative error in estimation: {np.real(np.round(relative_error_estimation, 8))}"
    )