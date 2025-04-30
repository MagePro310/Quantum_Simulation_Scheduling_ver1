import numpy as np
from qiskit import *
import time
import mapomatic as mm
from qiskit_ibm_runtime.fake_provider import FakeBelemV2, FakeManilaV2
from qiskit.circuit.library import *
from NoTODS import *


def create_circuit(num_qubits=8):
    """Create and return a quantum circuit."""
    circ_test = RealAmplitudes(num_qubits, reps=1)
    circ_test = circ_test.decompose()
    circ_test.remove_final_measurements(inplace=True)
    return circ_test


def get_backends():
    """Return a list of fake backends and a backend dictionary."""
    backendlist = [FakeBelemV2(), FakeManilaV2()]
    backenddict = {backend.name: backend for backend in backendlist}
    return backendlist, backenddict


def initialize_notods(circ_test, backendlist, Tau):
    """Initialize and return the NoTODS object."""
    return NoTODS(circ_test, backendlist, Tau)


def cut_and_schedule(obj):
    """Cut the circuit and schedule it."""
    cuts = obj._cut_circuit()
    model = obj.schedule()
    return cuts, model


def transpile_subcircuits(cuts, model, backenddict):
    """Transpile subcircuits and evaluate layouts."""
    tran_qc = []
    for i in range(len(cuts['subcircuits'])):
        tran_qc.append(transpile(cuts['subcircuits'][i], backenddict[model[i]], optimization_level=0))
        small_qc = mm.deflate_circuit(tran_qc[i])
        layouts = mm.matching_layouts(small_qc, backenddict[model[i]])
        scores = mm.evaluate_layouts(small_qc, layouts, backenddict[model[i]])
        layout = scores[0][0]
    return tran_qc


if __name__ == "__main__":
    # Define the quantum circuit
    num_qubits = 8
    circ_test = create_circuit(num_qubits)
    circ_test.draw('mpl')

    # Define the backends
    backendlist, backenddict = get_backends()
    print(backenddict)

    # Define Tau
    Tau = [200] * len(backendlist)
    print(Tau)

    # Initialize NoTODS object
    obj = initialize_notods(circ_test, backendlist, Tau)

    # Cut the circuit and schedule
    cuts, model = cut_and_schedule(obj)
    print(cuts)
    print(model)

    # Draw subcircuits
    cuts['subcircuits'][0].draw('mpl')
    cuts['subcircuits'][1].draw('mpl')

    # Transpile and evaluate layouts
    transpile_subcircuits(cuts, model, backenddict)