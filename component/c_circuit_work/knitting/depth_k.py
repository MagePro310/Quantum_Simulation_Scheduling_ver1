from qiskit import QuantumCircuit

def expand_circuit_depth(left_circuit: QuantumCircuit, right_circuit: QuantumCircuit) -> QuantumCircuit:
    """
        Expand the width of a quantum circuit by adding a second circuit below it.
    
    Args:
        top_circuit (QuantumCircuit): The top quantum circuit to expand.
        bot_circuit (QuantumCircuit): The bottom quantum circuit to expand.
        
    Returns:
        QuantumCircuit: The expanded quantum circuit.
    """
    #!!! in the future need to add the qubit have dif width with the indicate the wire expand
    # With the syntax example
    # qcplus1 = QuantumCircuit(3)
    # qcplus1.h(0)
    # qcplus1.cx(0, 1)

    # qcplus2 = QuantumCircuit(3)
    # qcplus2.x(0)
    # qcplus2.cz(0, 2)

    # # Tạo mạch mới với đủ qubits để chứa cả qcplus1 và qcplus2
    # qctotal = QuantumCircuit(6)  # 3 qubits cho qcplus1 và 3 qubits cho qcplus2

    # # Ghép qcplus1 và qcplus2
    # qctotal = qcplus1.compose(qcplus2, qubits=[0, 1, 2], clbits=[], inplace=False)
    
    
    # Get the number of qubits of the left and right circuits
    lef_qubits = left_circuit.num_qubits
    right_qubits = right_circuit.num_qubits
    
    # Compare the number of qubits in the left and right circuits
    if lef_qubits != right_qubits:
        raise ValueError("The number of qubits in the left and right circuits must be equal.")
    # Create a new quantum circuit with the combined depth
    expanded_circuit = QuantumCircuit(lef_qubits)
    # Add the left circuit to the expanded circuit
    expanded_circuit = left_circuit.compose(right_circuit, inplace=False)
    return expanded_circuit