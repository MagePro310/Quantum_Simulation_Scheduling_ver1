import numpy as np
from qiskit.quantum_info import DensityMatrix, state_fidelity

def generate_basis_states(num_bits):
    """Tạo tất cả các trạng thái cơ bản nhị phân với độ dài num_bits."""
    return [format(i, f'0{num_bits}b') for i in range(2**num_bits)]

def compute_density_matrix(prob_dict, basis_states):
    """Tạo ma trận mật độ từ từ điển xác suất."""
    size = len(basis_states)
    rho_matrix = np.zeros((size, size), dtype=complex)
    for state, prob in prob_dict.items():
        idx = basis_states.index(state)
        rho_matrix[idx, idx] = prob
    return DensityMatrix(rho_matrix)

def compute_probabilities(counts_dict):
    """Chuyển counts sang xác suất."""
    total_count = sum(counts_dict.values())
    return {state: count / total_count for state, count in counts_dict.items()}

def fidelity_from_counts(counts_ideal, counts_sim):
    """
    Tính độ trung thực (fidelity) giữa hai ma trận mật độ từ counts.
    """
    # Xác suất
    prob_ideal = compute_probabilities(counts_ideal)
    prob_sim = compute_probabilities(counts_sim)

    # Suy ra số bit từ khóa trạng thái
    num_bits = len(next(iter(counts_ideal)))
    basis_states = generate_basis_states(num_bits)

    # Tạo ma trận mật độ
    rho_ideal = compute_density_matrix(prob_ideal, basis_states)
    rho_sim = compute_density_matrix(prob_sim, basis_states)

    # Tính độ trung thực
    fidelity_val = state_fidelity(rho_ideal, rho_sim)

    return fidelity_val, rho_ideal, rho_sim
