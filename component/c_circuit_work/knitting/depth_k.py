"""
Quantum Circuit Depth Expansion Module

This module provides utilities for expanding quantum circuit depth through
sequential composition of quantum circuits.

Author: Quantum Simulation Scheduling Team
Date: June 23, 2025
"""

from typing import Optional, List, Union
from qiskit import QuantumCircuit
from qiskit.circuit import Instruction


class QuantumCircuitDepthExpander:
    """
    A professional utility class for quantum circuit depth expansion operations.
    
    This class provides methods to sequentially compose quantum circuits,
    expanding their depth while maintaining circuit integrity and providing
    comprehensive validation and error handling.
    """
    
    @staticmethod
    def validate_circuit_compatibility(
        first_circuit: QuantumCircuit, 
        second_circuit: QuantumCircuit
    ) -> None:
        """
        Validate that two quantum circuits are compatible for composition.
        
        Args:
            first_circuit (QuantumCircuit): The first quantum circuit.
            second_circuit (QuantumCircuit): The second quantum circuit.
            
        Raises:
            TypeError: If inputs are not QuantumCircuit instances.
            ValueError: If circuits have incompatible qubit counts.
        """
        if not isinstance(first_circuit, QuantumCircuit):
            raise TypeError(f"Expected QuantumCircuit, got {type(first_circuit)}")
        if not isinstance(second_circuit, QuantumCircuit):
            raise TypeError(f"Expected QuantumCircuit, got {type(second_circuit)}")
            
        if first_circuit.num_qubits != second_circuit.num_qubits:
            raise ValueError(
                f"Circuit qubit count mismatch: first circuit has "
                f"{first_circuit.num_qubits} qubits, second circuit has "
                f"{second_circuit.num_qubits} qubits. Both circuits must have "
                f"the same number of qubits for sequential composition."
            )
    
    @staticmethod
    def expand_circuit_depth(
        first_circuit: QuantumCircuit, 
        second_circuit: QuantumCircuit,
        validate_inputs: bool = True
    ) -> QuantumCircuit:
        """
        Expand quantum circuit depth by sequentially composing two circuits.
        
        This method takes two quantum circuits with the same number of qubits
        and creates a new circuit where the second circuit is applied after
        the first circuit, effectively increasing the circuit depth.
        
        Args:
            first_circuit (QuantumCircuit): The first circuit to be executed.
            second_circuit (QuantumCircuit): The second circuit to be executed 
                                           after the first.
            validate_inputs (bool): Whether to validate input compatibility.
                                  Default is True.
        
        Returns:
            QuantumCircuit: A new quantum circuit with expanded depth containing
                          the sequential composition of both input circuits.
            
        Raises:
            TypeError: If inputs are not QuantumCircuit instances.
            ValueError: If circuits have different numbers of qubits.
            
        Example:
            >>> from qiskit import QuantumCircuit
            >>> # Create first circuit
            >>> qc1 = QuantumCircuit(2)
            >>> qc1.h(0)
            >>> qc1.cx(0, 1)
            >>> 
            >>> # Create second circuit  
            >>> qc2 = QuantumCircuit(2)
            >>> qc2.x(0)
            >>> qc2.cz(0, 1)
            >>> 
            >>> # Expand depth
            >>> expander = QuantumCircuitDepthExpander()
            >>> expanded = expander.expand_circuit_depth(qc1, qc2)
            >>> print(f"Original depths: {qc1.depth()}, {qc2.depth()}")
            >>> print(f"Expanded depth: {expanded.depth()}")
        """
        if validate_inputs:
            QuantumCircuitDepthExpander.validate_circuit_compatibility(
                first_circuit, second_circuit
            )
        
        # Sequential composition: second circuit applied after first circuit
        expanded_circuit = first_circuit.compose(second_circuit, inplace=False)
        
        return expanded_circuit
    
    @staticmethod
    def expand_multiple_circuits_depth(
        circuits: List[QuantumCircuit],
        validate_inputs: bool = True
    ) -> QuantumCircuit:
        """
        Expand depth by sequentially composing multiple quantum circuits.
        
        Args:
            circuits (List[QuantumCircuit]): List of quantum circuits to compose
                                           in sequential order.
            validate_inputs (bool): Whether to validate input compatibility.
                                  Default is True.
        
        Returns:
            QuantumCircuit: A new quantum circuit with all input circuits
                          composed sequentially.
            
        Raises:
            ValueError: If the circuits list is empty or contains incompatible circuits.
            TypeError: If any element is not a QuantumCircuit.
            
        Example:
            >>> circuits = [qc1, qc2, qc3]  # Three compatible circuits
            >>> expander = QuantumCircuitDepthExpander()
            >>> result = expander.expand_multiple_circuits_depth(circuits)
        """
        if not circuits:
            raise ValueError("Cannot compose an empty list of circuits")
        
        if len(circuits) == 1:
            return circuits[0].copy()
        
        # Start with the first circuit
        result_circuit = circuits[0].copy()
        
        # Sequentially compose remaining circuits
        for i, circuit in enumerate(circuits[1:], 1):
            if validate_inputs:
                QuantumCircuitDepthExpander.validate_circuit_compatibility(
                    result_circuit, circuit
                )
            result_circuit = result_circuit.compose(circuit, inplace=False)
        
        return result_circuit
    
    @staticmethod
    def get_composition_info(
        first_circuit: QuantumCircuit,
        second_circuit: QuantumCircuit
    ) -> dict:
        """
        Get detailed information about circuit composition.
        
        Args:
            first_circuit (QuantumCircuit): The first quantum circuit.
            second_circuit (QuantumCircuit): The second quantum circuit.
        
        Returns:
            dict: Information about the circuits and their composition.
        """
        QuantumCircuitDepthExpander.validate_circuit_compatibility(
            first_circuit, second_circuit
        )
        
        expanded = QuantumCircuitDepthExpander.expand_circuit_depth(
            first_circuit, second_circuit, validate_inputs=False
        )
        
        return {
            'first_circuit': {
                'qubits': first_circuit.num_qubits,
                'depth': first_circuit.depth(),
                'gates': len(first_circuit.data)
            },
            'second_circuit': {
                'qubits': second_circuit.num_qubits,
                'depth': second_circuit.depth(),
                'gates': len(second_circuit.data)
            },
            'composed_circuit': {
                'qubits': expanded.num_qubits,
                'depth': expanded.depth(),
                'gates': len(expanded.data),
                'total_depth_increase': expanded.depth() - max(
                    first_circuit.depth(), second_circuit.depth()
                )
            }
        }


# Legacy function for backward compatibility
def expand_circuit_depth(
    left_circuit: QuantumCircuit, 
    right_circuit: QuantumCircuit
) -> QuantumCircuit:
    """
    Legacy wrapper function for backward compatibility.
    
    Args:
        left_circuit (QuantumCircuit): The first quantum circuit.
        right_circuit (QuantumCircuit): The second quantum circuit.
        
    Returns:
        QuantumCircuit: The expanded quantum circuit.
        
    Note:
        This function is maintained for backward compatibility.
        New code should use QuantumCircuitDepthExpander.expand_circuit_depth().
    """
    return QuantumCircuitDepthExpander.expand_circuit_depth(
        left_circuit, right_circuit
    )