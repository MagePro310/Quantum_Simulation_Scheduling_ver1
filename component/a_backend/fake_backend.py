"""
Fake Quantum Backends Organized by Qubit Count
===============================================
This module provides IBM fake quantum backends organized by their qubit capacity.

Usage Examples:
    # Import specific qubit group
    from component.a_backend import fake_backend
    
    # Access 5-qubit backends
    backend = fake_backend.machine5qubits.FakeBelemV2()
    print(backend.num_qubits)  # Output: 5
    
    # Access 27-qubit backends  
    backend = fake_backend.machine27qubits.FakeHanoiV2()
    
    # Access 127-qubit backends
    backend = fake_backend.machine127qubits.FakeKyoto()

Available modules:
    - machine1qubit: 1 backend (1 qubit)
    - machine5qubits: 15 backends (5 qubits)
    - machine7qubits: 6 backends (7 qubits)
    - machine15qubits: 1 backend (15 qubits)
    - machine16qubits: 1 backend (16 qubits)
    - machine20qubits: 5 backends (20 qubits)
    - machine27qubits: 12 backends (27 qubits)
    - machine28qubits: 1 backend (28 qubits)
    - machine33qubits: 1 backend (33 qubits)
    - machine53qubits: 1 backend (53 qubits)
    - machine65qubits: 2 backends (65 qubits)
    - machine127qubits: 9 backends (127 qubits)
    - machine133qubits: 1 backend (133 qubits)
    - machine156qubits: 1 backend (156 qubits)
    - special_backends: Special backends
"""

# Import all sub-modules
from . import machine1qubit
from . import machine5qubits
from . import machine7qubits
from . import machine15qubits
from . import machine16qubits
from . import machine20qubits
from . import machine27qubits
from . import machine28qubits
from . import machine33qubits
from . import machine53qubits
from . import machine65qubits
from . import machine127qubits
from . import machine133qubits
from . import machine156qubits
from . import special_backends

# For backward compatibility - import all backends directly
from .machine1qubit import *
from .machine5qubits import *
from .machine7qubits import *
from .machine15qubits import *
from .machine16qubits import *
from .machine20qubits import *
from .machine27qubits import *
from .machine28qubits import *
from .machine33qubits import *
from .machine53qubits import *
from .machine65qubits import *
from .machine127qubits import *
from .machine133qubits import *
from .machine156qubits import *
from .special_backends import *

__all__ = [
    'machine1qubit',
    'machine5qubits',
    'machine7qubits',
    'machine15qubits',
    'machine16qubits',
    'machine20qubits',
    'machine27qubits',
    'machine28qubits',
    'machine33qubits',
    'machine53qubits',
    'machine65qubits',
    'machine127qubits',
    'machine133qubits',
    'machine156qubits',
    'special_backends',
]