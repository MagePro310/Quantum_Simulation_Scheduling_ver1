"""
Quantum State Assembly and Fidelity Analysis Module

This module provides utilities for quantum state analysis, including density matrix
computation and fidelity calculations from measurement counts.

Author: Quantum Simulation Scheduling Team
Date: June 23, 2025
"""

from typing import Dict, List, Tuple, Union
import numpy as np
from qiskit.quantum_info import DensityMatrix, state_fidelity


class QuantumStateAnalyzer:
    """
    A comprehensive analyzer for quantum states and fidelity calculations.
    
    This class provides methods to compute density matrices from probability
    distributions and calculate fidelities between quantum states based on
    measurement counts.
    """
    
    @staticmethod
    def generate_basis_states(num_bits: int) -> List[str]:
        """
        Generate all computational basis states for a given number of qubits.
        
        Args:
            num_bits (int): Number of qubits (bits) in the quantum system.
            
        Returns:
            List[str]: List of all possible binary basis states.
            
        Raises:
            ValueError: If num_bits is negative or exceeds practical limits.
            
        Example:
            >>> analyzer = QuantumStateAnalyzer()
            >>> analyzer.generate_basis_states(2)
            ['00', '01', '10', '11']
        """
        if num_bits < 0:
            raise ValueError("Number of bits must be non-negative")
        if num_bits > 20:  # Practical limit to prevent memory issues
            raise ValueError("Number of bits exceeds practical limit (20)")
            
        return [format(i, f'0{num_bits}b') for i in range(2**num_bits)]

    @staticmethod
    def compute_density_matrix(
        prob_dict: Dict[str, float], 
        basis_states: List[str]
    ) -> DensityMatrix:
        """
        Create a density matrix from a probability distribution.
        
        This method assumes a diagonal density matrix where each basis state
        has a probability but no coherence between states.
        
        Args:
            prob_dict (Dict[str, float]): Probability distribution over basis states.
            basis_states (List[str]): List of all possible basis states.
            
        Returns:
            DensityMatrix: Qiskit DensityMatrix object representing the quantum state.
            
        Raises:
            ValueError: If probabilities don't sum to 1 or contain invalid values.
            KeyError: If prob_dict contains states not in basis_states.
        """
        # Validate probability distribution
        total_prob = sum(prob_dict.values())
        if not np.isclose(total_prob, 1.0, rtol=1e-10):
            raise ValueError(f"Probabilities must sum to 1, got {total_prob}")
            
        if any(prob < 0 for prob in prob_dict.values()):
            raise ValueError("Probabilities must be non-negative")
        
        # Validate that all states in prob_dict exist in basis_states
        invalid_states = set(prob_dict.keys()) - set(basis_states)
        if invalid_states:
            raise KeyError(f"Invalid states found: {invalid_states}")
        
        size = len(basis_states)
        rho_matrix = np.zeros((size, size), dtype=complex)
        
        # Create state-to-index mapping for efficiency
        state_to_idx = {state: idx for idx, state in enumerate(basis_states)}
        
        for state, prob in prob_dict.items():
            idx = state_to_idx[state]
            rho_matrix[idx, idx] = prob
            
        return DensityMatrix(rho_matrix)

    @staticmethod
    def compute_probabilities(counts_dict: Dict[str, int]) -> Dict[str, float]:
        """
        Convert measurement counts to probability distribution.
        
        Args:
            counts_dict (Dict[str, int]): Dictionary mapping basis states to counts.
            
        Returns:
            Dict[str, float]: Normalized probability distribution.
            
        Raises:
            ValueError: If counts are negative or total count is zero.
        """
        if not counts_dict:
            raise ValueError("Counts dictionary cannot be empty")
            
        if any(count < 0 for count in counts_dict.values()):
            raise ValueError("Counts must be non-negative")
            
        total_count = sum(counts_dict.values())
        if total_count == 0:
            raise ValueError("Total count cannot be zero")
            
        return {state: count / total_count for state, count in counts_dict.items()}

    @classmethod
    def calculate_fidelity_from_counts(
        cls,
        counts_ideal: Dict[str, int],
        counts_simulation: Dict[str, int],
        verbose: bool = False
    ) -> Tuple[float, DensityMatrix, DensityMatrix]:
        """
        Calculate quantum state fidelity between ideal and simulated results.
        
        This method computes the fidelity between two quantum states represented
        by their measurement count distributions.
        
        Args:
            counts_ideal (Dict[str, int]): Measurement counts from ideal computation.
            counts_simulation (Dict[str, int]): Measurement counts from simulation.
            verbose (bool): If True, print intermediate results for debugging.
            
        Returns:
            Tuple[float, DensityMatrix, DensityMatrix]: A tuple containing:
                - fidelity_value: Quantum state fidelity (0 to 1)
                - rho_ideal: Density matrix of the ideal state
                - rho_simulation: Density matrix of the simulated state
                
        Raises:
            ValueError: If input dictionaries are empty or have inconsistent bit lengths.
            
        Example:
            >>> ideal = {'00': 500, '11': 500}
            >>> sim = {'00': 480, '01': 10, '10': 10, '11': 500}
            >>> fidelity, rho_i, rho_s = QuantumStateAnalyzer.calculate_fidelity_from_counts(ideal, sim)
            >>> print(f"Fidelity: {fidelity:.4f}")
        """
        # Input validation
        if not counts_ideal or not counts_simulation:
            raise ValueError("Both count dictionaries must be non-empty")
        
        # Convert counts to probabilities
        prob_ideal = cls.compute_probabilities(counts_ideal)
        prob_simulation = cls.compute_probabilities(counts_simulation)
        
        if verbose:
            print(f"Ideal probabilities: {prob_ideal}")
            print(f"Simulation probabilities: {prob_simulation}")

        # Determine the number of qubits from the state strings
        sample_state = next(iter(counts_ideal))
        num_qubits = len(sample_state)
        
        # Validate consistency
        all_states = set(counts_ideal.keys()) | set(counts_simulation.keys())
        if not all(len(state) == num_qubits for state in all_states):
            raise ValueError("All quantum states must have the same number of qubits")
        
        # Generate complete basis
        basis_states = cls.generate_basis_states(num_qubits)
        
        if verbose:
            print(f"Number of qubits: {num_qubits}")
            print(f"Basis states: {basis_states}")

        # Ensure both probability distributions include all basis states
        complete_prob_ideal = {state: prob_ideal.get(state, 0.0) for state in basis_states}
        complete_prob_simulation = {state: prob_simulation.get(state, 0.0) for state in basis_states}

        # Create density matrices
        rho_ideal = cls.compute_density_matrix(complete_prob_ideal, basis_states)
        rho_simulation = cls.compute_density_matrix(complete_prob_simulation, basis_states)
        
        if verbose:
            print(f"Ideal density matrix shape: {rho_ideal.data.shape}")
            print(f"Simulation density matrix shape: {rho_simulation.data.shape}")

        # Calculate quantum state fidelity
        fidelity_value = state_fidelity(rho_ideal, rho_simulation)
        
        return fidelity_value, rho_ideal, rho_simulation


# Legacy function aliases for backward compatibility
def generate_basis_states(num_bits: int) -> List[str]:
    """Legacy wrapper for QuantumStateAnalyzer.generate_basis_states()."""
    return QuantumStateAnalyzer.generate_basis_states(num_bits)


def compute_density_matrix(prob_dict: Dict[str, float], basis_states: List[str]) -> DensityMatrix:
    """Legacy wrapper for QuantumStateAnalyzer.compute_density_matrix()."""
    return QuantumStateAnalyzer.compute_density_matrix(prob_dict, basis_states)


def compute_probabilities(counts_dict: Dict[str, int]) -> Dict[str, float]:
    """Legacy wrapper for QuantumStateAnalyzer.compute_probabilities()."""
    return QuantumStateAnalyzer.compute_probabilities(counts_dict)


def fidelity_from_counts(
    counts_ideal: Dict[str, int], 
    counts_sim: Dict[str, int]
) -> Tuple[float, DensityMatrix, DensityMatrix]:
    """Legacy wrapper for QuantumStateAnalyzer.calculate_fidelity_from_counts()."""
    return QuantumStateAnalyzer.calculate_fidelity_from_counts(counts_ideal, counts_sim)