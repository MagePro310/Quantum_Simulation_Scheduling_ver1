from component.a_backend import fake_backend

def load_backends():
    imported_names = dir(fake_backend)
    backends = {
        name: getattr(fake_backend, name).num_qubits
        for name in imported_names
        if not name.startswith('__') and hasattr(getattr(fake_backend, name), 'num_qubits')
    }
    return backends