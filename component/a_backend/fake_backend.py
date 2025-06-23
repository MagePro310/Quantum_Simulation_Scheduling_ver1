"""
Fake Backend Module for Quantum Simulation Scheduling

This module provides access to IBM Qiskit fake backends for simulation purposes.
It organizes all available fake backends by categories and provides convenient
access methods for quantum circuit simulation and testing.

Categories:
- V2 Backends: Modern backends with improved calibration data
- Legacy Backends: Older generation backends
- Special Backends: Experimental or specialized backends
"""

from typing import Dict, List, Type, Any

# Import all fake backends in a more organized manner
from qiskit_ibm_runtime.fake_provider import (
    # V2 Backends - Alphabetically sorted
    FakeAlmadenV2,
    FakeArmonkV2,
    FakeAthensV2,
    FakeBelemV2,
    FakeBoeblingenV2,
    FakeBogotaV2,
    FakeBrooklynV2,
    FakeBurlingtonV2,
    FakeCairoV2,
    FakeCambridgeV2,
    FakeCasablancaV2,
    FakeEssexV2,
    FakeGuadalupeV2,
    FakeHanoiV2,
    FakeJakartaV2,
    FakeJohannesburgV2,
    FakeKolkataV2,
    FakeLagosV2,
    FakeLimaV2,
    FakeLondonV2,
    FakeManhattanV2,
    FakeManilaV2,
    FakeMelbourneV2,
    FakeMontrealV2,
    FakeMumbaiV2,
    FakeNairobiV2,
    FakeOurenseV2,
    FakeParisV2,
    FakePoughkeepsieV2,
    FakeQuitoV2,
    FakeRochesterV2,
    FakeRomeV2,
    FakeSantiagoV2,
    FakeSingaporeV2,
    FakeSydneyV2,
    FakeTorontoV2,
    FakeValenciaV2,
    FakeVigoV2,
    FakeWashingtonV2,
    FakeYorktownV2,
    
    # Latest Generation Backends
    FakeAlgiers,
    FakeAuckland,
    FakeBrisbane,
    FakeCusco,
    FakeGeneva,
    FakeKawasaki,
    FakeKyiv,
    FakeKyoto,
    FakeMarrakesh,
    FakeOsaka,
    FakeOslo,
    FakePeekskill,
    FakePerth,
    FakePrague,
    FakeQuebec,
    FakeSherbrooke,
    FakeTorino,
    
    # Special Backends
    FakeFractionalBackend,
)


# Organized backend collections
V2_BACKENDS: Dict[str, Type[Any]] = {
    'almaden': FakeAlmadenV2,
    'armonk': FakeArmonkV2,
    'athens': FakeAthensV2,
    'belem': FakeBelemV2,
    'boeblingen': FakeBoeblingenV2,
    'bogota': FakeBogotaV2,
    'brooklyn': FakeBrooklynV2,
    'burlington': FakeBurlingtonV2,
    'cairo': FakeCairoV2,
    'cambridge': FakeCambridgeV2,
    'casablanca': FakeCasablancaV2,
    'essex': FakeEssexV2,
    'guadalupe': FakeGuadalupeV2,
    'hanoi': FakeHanoiV2,
    'jakarta': FakeJakartaV2,
    'johannesburg': FakeJohannesburgV2,
    'kolkata': FakeKolkataV2,
    'lagos': FakeLagosV2,
    'lima': FakeLimaV2,
    'london': FakeLondonV2,
    'manhattan': FakeManhattanV2,
    'manila': FakeManilaV2,
    'melbourne': FakeMelbourneV2,
    'montreal': FakeMontrealV2,
    'mumbai': FakeMumbaiV2,
    'nairobi': FakeNairobiV2,
    'ourense': FakeOurenseV2,
    'paris': FakeParisV2,
    'poughkeepsie': FakePoughkeepsieV2,
    'quito': FakeQuitoV2,
    'rochester': FakeRochesterV2,
    'rome': FakeRomeV2,
    'santiago': FakeSantiagoV2,
    'singapore': FakeSingaporeV2,
    'sydney': FakeSydneyV2,
    'toronto': FakeTorontoV2,
    'valencia': FakeValenciaV2,
    'vigo': FakeVigoV2,
    'washington': FakeWashingtonV2,
    'yorktown': FakeYorktownV2,
}

LATEST_BACKENDS: Dict[str, Type[Any]] = {
    'algiers': FakeAlgiers,
    'auckland': FakeAuckland,
    'brisbane': FakeBrisbane,
    'cusco': FakeCusco,
    'geneva': FakeGeneva,
    'kawasaki': FakeKawasaki,
    'kyiv': FakeKyiv,
    'kyoto': FakeKyoto,
    'marrakesh': FakeMarrakesh,
    'osaka': FakeOsaka,
    'oslo': FakeOslo,
    'peekskill': FakePeekskill,
    'perth': FakePerth,
    'prague': FakePrague,
    'quebec': FakeQuebec,
    'sherbrooke': FakeSherbrooke,
    'torino': FakeTorino,
}

SPECIAL_BACKENDS: Dict[str, Type[Any]] = {
    'fractional': FakeFractionalBackend,
}

# Combined registry of all backends
ALL_BACKENDS: Dict[str, Type[Any]] = {
    **V2_BACKENDS,
    **LATEST_BACKENDS,
    **SPECIAL_BACKENDS,
}


def get_backend_by_name(name: str) -> Type[Any]:
    """
    Get a fake backend by name.
    
    Args:
        name (str): The name of the backend (case-insensitive)
        
    Returns:
        Type[Any]: The fake backend class
        
    Raises:
        ValueError: If the backend name is not found
    """
    name_lower = name.lower()
    if name_lower in ALL_BACKENDS:
        return ALL_BACKENDS[name_lower]
    
    raise ValueError(f"Backend '{name}' not found. Available backends: {list(ALL_BACKENDS.keys())}")


def get_available_backends() -> List[str]:
    """
    Get a list of all available backend names.
    
    Returns:
        List[str]: List of backend names
    """
    return list(ALL_BACKENDS.keys())


def get_v2_backends() -> List[str]:
    """
    Get a list of V2 backend names.
    
    Returns:
        List[str]: List of V2 backend names
    """
    return list(V2_BACKENDS.keys())


def get_latest_backends() -> List[str]:
    """
    Get a list of latest generation backend names.
    
    Returns:
        List[str]: List of latest backend names
    """
    return list(LATEST_BACKENDS.keys())


def get_special_backends() -> List[str]:
    """
    Get a list of special backend names.
    
    Returns:
        List[str]: List of special backend names
    """
    return list(SPECIAL_BACKENDS.keys())


# Export commonly used backends for direct access
__all__ = [
    # Main interface functions
    'get_backend_by_name',
    'get_available_backends',
    'get_v2_backends',
    'get_latest_backends',
    'get_special_backends',
    
    # Backend collections
    'ALL_BACKENDS',
    'V2_BACKENDS',
    'LATEST_BACKENDS',
    'SPECIAL_BACKENDS',
    
    # Individual backend classes (most commonly used ones)
    'FakeArmonkV2',
    'FakeBogotaV2',
    'FakeCairoV2',
    'FakeJakartaV2',
    'FakeManilaV2',
    'FakeQuitoV2',
    'FakeSantiagoV2',
    'FakePrague',
    'FakeKyoto',
    'FakeTorino',
]