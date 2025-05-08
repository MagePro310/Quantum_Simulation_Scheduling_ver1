import numpy as np
from qiskit.quantum_info import DensityMatrix, state_fidelity

def generate_basis_states(num_bits):
    """Generate all binary basis states of length num_bits."""
    return [format(i, f'0{num_bits}b') for i in range(2**num_bits)]

def compute_density_matrix(prob_dict, basis_states):
    """Create a density matrix from a probability dictionary."""
    size = len(basis_states)
    rho_matrix = np.zeros((size, size), dtype=complex)
    for state, prob in prob_dict.items():
        idx = basis_states.index(state)
        rho_matrix[idx, idx] = prob
    return DensityMatrix(rho_matrix)

def compute_probabilities(counts_dict):
    """Convert counts to probabilities."""
    total_count = sum(counts_dict.values())
    return {state: count / total_count for state, count in counts_dict.items()}

def fidelity_from_counts(counts_ideal, counts_sim):
    """
    Calculate the fidelity between two density matrices from counts.
    """
    # Calculate probabilities from counts
    prob_ideal = compute_probabilities(counts_ideal)
    # print("prob_ideal")
    # print(prob_ideal)
    prob_sim = compute_probabilities(counts_sim)
    # print("prob_sim")
    # print(prob_sim)

    # Derive number of bits from the states in counts
    num_bits = len(next(iter(counts_ideal)))  # Length of one of the states (e.g., '0000')
    # print("num_bits")
    # print(num_bits)
    basis_states = generate_basis_states(num_bits)
    # print("basis_states")
    # print(basis_states)

    # Create density matrices
    rho_ideal = compute_density_matrix(prob_ideal, basis_states)
    # print("rho_ideal")
    # print(rho_ideal)
    rho_sim = compute_density_matrix(prob_sim, basis_states)
    # print("rho_sim")
    # print(rho_sim)
    # Calculate fidelity
    fidelity_val = state_fidelity(rho_ideal, rho_sim)

    return fidelity_val, rho_ideal, rho_sim