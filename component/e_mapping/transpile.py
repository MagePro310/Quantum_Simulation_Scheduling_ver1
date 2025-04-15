from component.a_backend.fake_backend import *
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit import transpile

def transpile_circuit_pass(circuit, backend0):
    """
    Process a quantum circuit by applying transpiler optimization and visualizing it.

    Args:
        subcircuits (dict): A dictionary of subcircuits with keys as names and values as QuantumCircuit objects.
        backend0: The backend object containing target and coupling map information.

    Returns:
        The transpiled quantum circuit after optimization.
    """
    # Filter out "qpd_1q" operations
    circuit.data = [hasChange for hasChange in circuit.data if hasChange.operation.name != "qpd_1q"]

    # Build coupling map and transpile the circuit
    target = backend0.target
    coupling_map = target.build_coupling_map()
    pass_manager = generate_preset_pass_manager(
        optimization_level=3, coupling_map=coupling_map, seed_transpiler=12345
    )
    qc_t_cm_lv0 = pass_manager.run(circuit)

    # Draw and save the circuit visualization
    qc_t_cm_lv0.draw("mpl", idle_wires=False, fold=-1)
    plt.savefig("transpiled_circuit.png")  # Save the circuit drawing as a PNG file
    plt.close()

    return qc_t_cm_lv0



def transpile_circuit_trans(circuit, backend):
    """
    Transpile a quantum circuit for a specific backend and draw it.

    Args:
        subcircuits (dict): A dictionary of subcircuits with keys as names and values as QuantumCircuit objects.
        backend0: The backend object to transpile the circuit for.
        style (str): The style to use for drawing the transpiled circuit. Default is "iqp".

    Returns:
        The transpiled quantum circuit.
    """
    # Transpile the circuit
    transpiled_circuit = transpile(circuit, backend)

    # Draw and save the circuit visualization
    transpiled_circuit.draw('mpl')
    plt.savefig("transpiled_circuit_.jpg")  # Save the circuit drawing as a PNG file
    plt.close()

    return transpiled_circuit