"""
Quantum Circuit Width Expansion Module

This module provides utilities for expanding quantum circuit width through
tensor product operations, enabling horizontal composition of quantum circuits.

Author: Quantum Simulation Scheduling Team
Date: June 23, 2025
"""

from typing import List, Optional, Dict, Any
from qiskit import QuantumCircuit
from qiskit.circuit import Instruction


class QuantumCircuitWidthExpander:
    """
    A professional utility class for quantum circuit width expansion operations.
    
    This class provides methods to horizontally compose quantum circuits using
    tensor products, expanding their width while maintaining circuit integrity
    and providing comprehensive validation and error handling.
    """
    
    @staticmethod
    def validate_circuit_input(circuit: Any, parameter_name: str = "circuit") -> None:
        """
        Validate that the input is a valid QuantumCircuit instance.
        
        Args:
            circuit (Any): The object to validate.
            parameter_name (str): Name of the parameter for error reporting.
            
        Raises:
            TypeError: If the input is not a QuantumCircuit instance.
            ValueError: If the circuit is empty or invalid.
        """
        if not isinstance(circuit, QuantumCircuit):
            raise TypeError(
                f"Parameter '{parameter_name}' must be a QuantumCircuit instance, "
                f"got {type(circuit).__name__}"
            )
        
        if circuit.num_qubits == 0:
            raise ValueError(f"Parameter '{parameter_name}' cannot be an empty circuit")
    
    @staticmethod
    def validate_circuit_list(circuit_list: List[QuantumCircuit]) -> None:
        """
        Validate a list of quantum circuits.
        
        Args:
            circuit_list (List[QuantumCircuit]): List of circuits to validate.
            
        Raises:
            TypeError: If input is not a list or contains non-QuantumCircuit elements.
            ValueError: If the list is empty or contains invalid circuits.
        """
        if not isinstance(circuit_list, list):
            raise TypeError(f"Expected list, got {type(circuit_list).__name__}")
        
        if not circuit_list:
            raise ValueError("Circuit list cannot be empty")
        
        for i, circuit in enumerate(circuit_list):
            QuantumCircuitWidthExpander.validate_circuit_input(
                circuit, f"circuit_list[{i}]"
            )
    
    @staticmethod
    def expand_circuit_width(
        first_circuit: QuantumCircuit, 
        second_circuit: QuantumCircuit,
        validate_inputs: bool = True
    ) -> QuantumCircuit:
        """
        Expand quantum circuit width by taking the tensor product of two circuits.
        
        This method horizontally combines two quantum circuits using the tensor
        product operation. The resulting circuit has a width equal to the sum
        of the input circuits' widths.
        
        Args:
            first_circuit (QuantumCircuit): The first quantum circuit (top register).
            second_circuit (QuantumCircuit): The second quantum circuit (bottom register).
            validate_inputs (bool): Whether to validate input circuits. Default is True.
        
        Returns:
            QuantumCircuit: A new quantum circuit representing the tensor product
                          of the input circuits, with width equal to the sum of
                          input widths.
            
        Raises:
            TypeError: If inputs are not QuantumCircuit instances.
            ValueError: If circuits are empty or invalid.
            
        Example:
            >>> from qiskit import QuantumCircuit
            >>> # Create first circuit (2 qubits)
            >>> qc1 = QuantumCircuit(2)
            >>> qc1.h(0)
            >>> qc1.cx(0, 1)
            >>> 
            >>> # Create second circuit (3 qubits)  
            >>> qc2 = QuantumCircuit(3)
            >>> qc2.x(0)
            >>> qc2.cz(0, 2)
            >>> 
            >>> # Expand width
            >>> expander = QuantumCircuitWidthExpander()
            >>> expanded = expander.expand_circuit_width(qc1, qc2)
            >>> print(f"Original widths: {qc1.num_qubits}, {qc2.num_qubits}")
            >>> print(f"Expanded width: {expanded.num_qubits}")  # Output: 5
        """
        if validate_inputs:
            QuantumCircuitWidthExpander.validate_circuit_input(first_circuit, "first_circuit")
            QuantumCircuitWidthExpander.validate_circuit_input(second_circuit, "second_circuit")
        
        # Tensor product: horizontal combination of circuits
        expanded_circuit = first_circuit.tensor(second_circuit)
        
        return expanded_circuit
    
    @staticmethod
    def merge_multiple_circuits(
        circuit_list: List[QuantumCircuit],
        validate_inputs: bool = True
    ) -> QuantumCircuit:
        """
        Merge multiple quantum circuits horizontally via tensor product.
        
        This method takes a list of quantum circuits and combines them
        horizontally using successive tensor products. The resulting circuit
        has a width equal to the sum of all input circuit widths.
        
        Args:
            circuit_list (List[QuantumCircuit]): List of quantum circuits to merge
                                               in order from top to bottom register.
            validate_inputs (bool): Whether to validate input circuits. Default is True.
        
        Returns:
            QuantumCircuit: A new quantum circuit representing the tensor product
                          of all input circuits.
            
        Raises:
            TypeError: If input is not a list or contains non-QuantumCircuit elements.
            ValueError: If the list is empty or contains invalid circuits.
            
        Example:
            >>> circuits = [qc1, qc2, qc3]  # Three circuits with 2, 3, 1 qubits
            >>> expander = QuantumCircuitWidthExpander()
            >>> merged = expander.merge_multiple_circuits(circuits)
            >>> print(f"Total width: {merged.num_qubits}")  # Output: 6
        """
        if validate_inputs:
            QuantumCircuitWidthExpander.validate_circuit_list(circuit_list)
        
        # Start with the first circuit
        merged_circuit = circuit_list[0].copy()
        
        # Successively apply tensor products
        for i, circuit in enumerate(circuit_list[1:], 1):
            if validate_inputs:
                QuantumCircuitWidthExpander.validate_circuit_input(
                    circuit, f"circuit_list[{i}]"
                )
            merged_circuit = merged_circuit.tensor(circuit)
        
        return merged_circuit
    
    @staticmethod
    def get_tensor_composition_info(circuit_list: List[QuantumCircuit]) -> Dict[str, Any]:
        """
        Get detailed information about tensor product composition.
        
        Args:
            circuit_list (List[QuantumCircuit]): List of circuits to analyze.
        
        Returns:
            Dict[str, Any]: Comprehensive information about the circuits and their
                          tensor product composition.
        """
        QuantumCircuitWidthExpander.validate_circuit_list(circuit_list)
        
        # Analyze individual circuits
        individual_info = []
        total_qubits = 0
        max_depth = 0
        total_gates = 0
        
        for i, circuit in enumerate(circuit_list):
            circuit_info = {
                'index': i,
                'qubits': circuit.num_qubits,
                'depth': circuit.depth(),
                'gates': len(circuit.data),
                'name': circuit.name if circuit.name else f"Circuit_{i}"
            }
            individual_info.append(circuit_info)
            total_qubits += circuit.num_qubits
            max_depth = max(max_depth, circuit.depth())
            total_gates += len(circuit.data)
        
        # Analyze composed circuit
        composed = QuantumCircuitWidthExpander.merge_multiple_circuits(
            circuit_list, validate_inputs=False
        )
        
        return {
            'individual_circuits': individual_info,
            'composition_summary': {
                'num_circuits': len(circuit_list),
                'total_qubits': total_qubits,
                'max_individual_depth': max_depth,
                'total_gates_count': total_gates
            },
            'composed_circuit': {
                'qubits': composed.num_qubits,
                'depth': composed.depth(),
                'gates': len(composed.data),
                'qubit_range_mapping': QuantumCircuitWidthExpander._get_qubit_mapping(circuit_list)
            }
        }
    
    @staticmethod
    def _get_qubit_mapping(circuit_list: List[QuantumCircuit]) -> List[Dict[str, int]]:
        """
        Get the qubit range mapping for each circuit in the tensor product.
        
        Args:
            circuit_list (List[QuantumCircuit]): List of circuits.
            
        Returns:
            List[Dict[str, int]]: Mapping of qubit ranges for each circuit.
        """
        mappings = []
        current_offset = 0
        
        for i, circuit in enumerate(circuit_list):
            mapping = {
                'circuit_index': i,
                'start_qubit': current_offset,
                'end_qubit': current_offset + circuit.num_qubits - 1,
                'qubit_count': circuit.num_qubits
            }
            mappings.append(mapping)
            current_offset += circuit.num_qubits
        
        return mappings
    
    @staticmethod
    def create_uniform_width_expansion(
        base_circuit: QuantumCircuit, 
        repetitions: int
    ) -> QuantumCircuit:
        """
        Create a uniform width expansion by repeating a base circuit.
        
        Args:
            base_circuit (QuantumCircuit): The circuit to repeat.
            repetitions (int): Number of times to repeat the circuit.
            
        Returns:
            QuantumCircuit: The expanded circuit with uniform repetitions.
            
        Raises:
            ValueError: If repetitions is less than 1.
        """
        if repetitions < 1:
            raise ValueError("Repetitions must be at least 1")
        
        QuantumCircuitWidthExpander.validate_circuit_input(base_circuit, "base_circuit")
        
        if repetitions == 1:
            return base_circuit.copy()
        
        # Create list of identical circuits
        circuit_list = [base_circuit.copy() for _ in range(repetitions)]
        
        return QuantumCircuitWidthExpander.merge_multiple_circuits(
            circuit_list, validate_inputs=False
        )


# Legacy functions for backward compatibility
def expand_circuit_width(
    top_circuit: QuantumCircuit, 
    bot_circuit: QuantumCircuit
) -> QuantumCircuit:
    """
    Legacy wrapper function for backward compatibility.
    
    Args:
        top_circuit (QuantumCircuit): The top quantum circuit.
        bot_circuit (QuantumCircuit): The bottom quantum circuit.
        
    Returns:
        QuantumCircuit: The tensor product of the two circuits.
        
    Note:
        This function is maintained for backward compatibility.
        New code should use QuantumCircuitWidthExpander.expand_circuit_width().
    """
    return QuantumCircuitWidthExpander.expand_circuit_width(top_circuit, bot_circuit)


def merge_multiple_circuits(circuit_list: List[QuantumCircuit]) -> QuantumCircuit:
    """
    Legacy wrapper function for backward compatibility.
    
    Args:
        circuit_list (List[QuantumCircuit]): List of circuits to merge.
        
    Returns:
        QuantumCircuit: The merged circuit.
        
    Note:
        This function is maintained for backward compatibility.
        New code should use QuantumCircuitWidthExpander.merge_multiple_circuits().
    """
    return QuantumCircuitWidthExpander.merge_multiple_circuits(circuit_list)