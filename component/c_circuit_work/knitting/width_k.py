from qiskit import QuantumCircuit

def expand_circuit_width(top_circuit: QuantumCircuit, bot_circuit: QuantumCircuit) -> QuantumCircuit:
    """
    Expand the width of a quantum circuit by adding a second circuit below it.
    
    Args:
        top_circuit (QuantumCircuit): The top quantum circuit to expand.
        bot_circuit (QuantumCircuit): The bottom quantum circuit to expand.
        
    Returns:
        QuantumCircuit: The expanded quantum circuit.
    """
    
    
    # Get the number of qubits in the top and bottom circuits
    top_qubits = top_circuit.num_qubits
    bot_qubits = bot_circuit.num_qubits
    
    
    # Create a new quantum circuit with the combined width
    expanded_circuit = QuantumCircuit(top_qubits + bot_qubits)
    expanded_circuit = top_circuit.tensor(bot_circuit)
    
    return expanded_circuit