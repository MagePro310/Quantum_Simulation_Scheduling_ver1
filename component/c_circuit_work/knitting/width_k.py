from qiskit import QuantumCircuit

def expand_circuit_width(top_circuit: QuantumCircuit, bot_circuit: QuantumCircuit) -> QuantumCircuit:
    """Tensor product (horizontal merge) of two circuits."""
    return top_circuit.tensor(bot_circuit)

def merge_multiple_circuits(circuit_list):
    """Merge a list of circuits horizontally via tensor product."""
    if not circuit_list:
        raise ValueError("Empty circuit list")
    merged_circuit = circuit_list[0]
    for circuit in circuit_list[1:]:
        merged_circuit = expand_circuit_width(merged_circuit, circuit)
    return merged_circuit