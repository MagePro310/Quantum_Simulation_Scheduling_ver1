from component.a_backend import fake_backend
import pandas as pd

def load_backends():
    imported_names = dir(fake_backend)
    backends = [name for name in imported_names if not name.startswith('__')]
    backend_qubits = {name: getattr(fake_backend, name)().num_qubits for name in backends}
    return backend_qubits