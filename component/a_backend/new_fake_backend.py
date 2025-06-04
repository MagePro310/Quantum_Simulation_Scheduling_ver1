# backend_loader.py

from qiskit_ibm_runtime.fake_provider import *

ALL_BACKENDS = {
    "FakeArmonkV2": FakeArmonkV2,
    "FakeAthensV2": FakeAthensV2,
    "FakeBelemV2": FakeBelemV2,
    "FakeBogotaV2": FakeBogotaV2,
    "FakeBurlingtonV2": FakeBurlingtonV2,
    "FakeEssexV2": FakeEssexV2,
    "FakeFractionalBackend": FakeFractionalBackend,
    "FakeLimaV2": FakeLimaV2,
    "FakeLondonV2": FakeLondonV2,
    "FakeManilaV2": FakeManilaV2,
    "FakeOurenseV2": FakeOurenseV2,
    "FakeQuitoV2": FakeQuitoV2,
    "FakeRomeV2": FakeRomeV2,
    "FakeValenciaV2": FakeValenciaV2,
    "FakeVigoV2": FakeVigoV2,
    "FakeYorktownV2": FakeYorktownV2,
    "FakeAlgiers": FakeAlgiers,
    "FakeAuckland": FakeAuckland,
    "FakeCairoV2": FakeCairoV2,
    "FakeGeneva": FakeGeneva,
    "FakeHanoiV2": FakeHanoiV2,
    "FakeKolkataV2": FakeKolkataV2,
    "FakeMontrealV2": FakeMontrealV2,
    "FakeMumbaiV2": FakeMumbaiV2,
    "FakePeekskill": FakePeekskill,
    "FakeSydneyV2": FakeSydneyV2,
    "FakeTorontoV2": FakeTorontoV2,
    "FakeBrisbane": FakeBrisbane,
    "FakeCusco": FakeCusco,
    "FakeKawasaki": FakeKawasaki,
    "FakeKyiv": FakeKyiv,
    "FakeKyoto": FakeKyoto,
    "FakeOsaka": FakeOsaka,
    "FakeQuebec": FakeQuebec,
    "FakeSherbrooke": FakeSherbrooke,
    "FakeWashingtonV2": FakeWashingtonV2,
    "FakeAlmadenV2": FakeAlmadenV2,
    "FakeBoeblingenV2": FakeBoeblingenV2,
    "FakeBrooklynV2": FakeBrooklynV2,
    "FakeCambridgeV2": FakeCambridgeV2,
    "FakeCasablancaV2": FakeCasablancaV2,
    "FakeGuadalupeV2": FakeGuadalupeV2,
    "FakeJakartaV2": FakeJakartaV2,
    "FakeJohannesburgV2": FakeJohannesburgV2,
    "FakeLagosV2": FakeLagosV2,
    "FakeManhattanV2": FakeManhattanV2,
    "FakeMarrakesh": FakeMarrakesh,
    "FakeMelbourneV2": FakeMelbourneV2,
    "FakeNairobiV2": FakeNairobiV2,
    "FakeOslo": FakeOslo,
    "FakeParisV2": FakeParisV2,
    "FakePerth": FakePerth,
    "FakePrague": FakePrague,
    "FakePoughkeepsieV2": FakePoughkeepsieV2,
    "FakeRochesterV2": FakeRochesterV2,
    "FakeSantiagoV2": FakeSantiagoV2,
    "FakeSingaporeV2": FakeSingaporeV2,
    "FakeTorino": FakeTorino,
}

def load_backends_from_config(backend_names: list[str]) -> dict:
    backends = {}
    for name in backend_names:
        if name in ALL_BACKENDS:
            instance = ALL_BACKENDS[name]()
            backends[instance.name] = instance
        else:
            raise ValueError(f"Backend '{name}' not recognized.")
    return backends