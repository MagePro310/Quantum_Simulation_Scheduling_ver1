"""
Test fixtures and utilities for Quantum Simulation Scheduling project.
Provides shared test data, mock objects, and helper functions.
"""

import sys
import pytest
from typing import Dict, List, Tuple
from unittest.mock import Mock, MagicMock, patch

# Add project root to path
sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy as np

from component.sup_sys.job_info import JobInfo

# Optional imports - backends may not be available
try:
    from component.a_backend.fake_backend import FakeBackend
    HAS_FAKE_BACKEND = True
except ImportError:
    HAS_FAKE_BACKEND = False
    FakeBackend = None


# ==================== Quantum Circuit Fixtures ====================

@pytest.fixture
def simple_circuit():
    """Create a simple 2-qubit test circuit."""
    qc = QuantumCircuit(2, 2, name="simple_2q")
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


@pytest.fixture
def medium_circuit():
    """Create a medium-complexity 5-qubit circuit."""
    qc = QuantumCircuit(5, 5, name="medium_5q")
    # Hadamard layer
    for i in range(5):
        qc.h(i)
    # CNOT ladder
    for i in range(4):
        qc.cx(i, i + 1)
    # RZ rotations
    for i in range(5):
        qc.rz(np.pi / 4, i)
    # Measurements
    qc.measure(range(5), range(5))
    return qc


@pytest.fixture
def deep_circuit():
    """Create a deeper 8-qubit circuit."""
    qc = QuantumCircuit(8, 8, name="deep_8q")
    # Multiple layers
    for layer in range(3):
        for i in range(8):
            qc.rx(np.pi / 8, i)
        for i in range(0, 7, 2):
            qc.cx(i, i + 1)
    qc.measure(range(8), range(8))
    return qc


# ==================== JobInfo Fixtures ====================

@pytest.fixture
def sample_job_simple(simple_circuit):
    """Create a sample JobInfo with a simple circuit."""
    return JobInfo(
        job_id="job_0",
        job_name="test_job_0",
        circuit=simple_circuit.copy(),
        qubits=2,
        machine="machine_0",
        capacity_machine=5,
        start_time=0.0,
        duration=2.0,
        end_time=2.0,
        childrenJobs=None,
        result_cut=None
    )


@pytest.fixture
def sample_job_medium(medium_circuit):
    """Create a sample JobInfo with a medium circuit."""
    return JobInfo(
        job_id="job_1",
        job_name="test_job_1",
        circuit=medium_circuit.copy(),
        qubits=5,
        machine="machine_1",
        capacity_machine=10,
        start_time=2.0,
        duration=5.0,
        end_time=7.0,
        childrenJobs=None,
        result_cut=None
    )


@pytest.fixture
def job_collection(sample_job_simple, sample_job_medium) -> Dict[str, JobInfo]:
    """Create a collection of sample jobs."""
    return {
        "job_0": sample_job_simple,
        "job_1": sample_job_medium
    }


# ==================== Machine/Backend Fixtures ====================

@pytest.fixture
def machine_capacities() -> Dict[str, int]:
    """Machine qubit capacity dictionary."""
    return {
        "machine_0": 5,
        "machine_1": 10,
        "machine_2": 7,
        "machine_3": 15
    }


@pytest.fixture
def fake_backend_5q():
    """Create a fake 5-qubit backend."""
    if not HAS_FAKE_BACKEND:
        pytest.skip("FakeBackend not available")
    return FakeBackend(num_qubits=5) if hasattr(FakeBackend, '__init__') else None


@pytest.fixture
def fake_backend_10q():
    """Create a fake 10-qubit backend."""
    if not HAS_FAKE_BACKEND:
        pytest.skip("FakeBackend not available")
    return FakeBackend(num_qubits=10) if hasattr(FakeBackend, '__init__') else None


# ==================== Data Fixtures ====================

@pytest.fixture
def sample_job_capacities() -> Dict[str, int]:
    """Sample job qubit requirements."""
    return {
        "job_0": 2,
        "job_1": 5,
        "job_2": 3,
        "job_3": 8,
        "job_4": 4
    }


@pytest.fixture
def scheduling_result():
    """Sample scheduling result."""
    return [
        {
            "job": "job_0",
            "machine": "machine_0",
            "start": 0.0,
            "end": 2.0,
            "qubits": 2
        },
        {
            "job": "job_1",
            "machine": "machine_1",
            "start": 0.0,
            "end": 5.0,
            "qubits": 5
        },
        {
            "job": "job_2",
            "machine": "machine_0",
            "start": 2.0,
            "end": 5.0,
            "qubits": 3
        }
    ]


# ==================== Mock Fixtures ====================

@pytest.fixture
def mock_algorithm():
    """Create a mock scheduling algorithm."""
    mock_algo = Mock()
    mock_algo.name = "MockAlgorithm"
    mock_algo.version = "1.0.0"
    mock_algo.schedule = Mock(return_value=[
        {"job": "job_0", "machine": "m0", "start": 0, "end": 2, "qubits": 2},
        {"job": "job_1", "machine": "m1", "start": 0, "end": 5, "qubits": 5}
    ])
    return mock_algo


@pytest.fixture
def mock_transpiler():
    """Create a mock transpiler."""
    mock_trans = Mock()
    mock_trans.transpile = Mock(side_effect=lambda circuit: circuit.copy())
    return mock_trans


# ==================== Helper Functions ====================

def create_circuit_batch(num_circuits: int, qubit_range: Tuple[int, int] = (2, 8)) -> List[QuantumCircuit]:
    """
    Create a batch of random test circuits.
    
    Args:
        num_circuits: Number of circuits to create
        qubit_range: (min_qubits, max_qubits) range
        
    Returns:
        List of QuantumCircuit objects
    """
    circuits = []
    for i in range(num_circuits):
        num_qubits = np.random.randint(qubit_range[0], qubit_range[1] + 1)
        qc = QuantumCircuit(num_qubits, name=f"circuit_{i}")
        
        # Add some gates
        for q in range(num_qubits):
            qc.h(q)
        for q in range(num_qubits - 1):
            qc.cx(q, q + 1)
        
        circuits.append(qc)
    return circuits


def create_job_batch(
    num_jobs: int,
    qubit_range: Tuple[int, int] = (2, 8)
) -> Dict[str, JobInfo]:
    """
    Create a batch of test JobInfo objects.
    
    Args:
        num_jobs: Number of jobs to create
        qubit_range: (min_qubits, max_qubits) range
        
    Returns:
        Dictionary mapping job_id to JobInfo
    """
    jobs = {}
    circuits = create_circuit_batch(num_jobs, qubit_range)
    
    for i, circuit in enumerate(circuits):
        job_id = f"job_{i}"
        jobs[job_id] = JobInfo(
            job_id=job_id,
            job_name=f"test_job_{i}",
            circuit=circuit,
            qubits=circuit.num_qubits,
            machine=f"machine_{i % 3}",
            capacity_machine=10,
            start_time=float(i),
            duration=float(circuit.num_qubits),
            end_time=float(i + circuit.num_qubits),
            childrenJobs=None,
            result_cut=None
        )
    
    return jobs


def assert_job_validity(job: JobInfo):
    """
    Validate a JobInfo object's consistency.
    
    Raises:
        AssertionError: If job is invalid
    """
    assert job.job_id is not None, "job_id must not be None"
    assert job.circuit is not None, "circuit must not be None"
    assert job.qubits > 0, "qubits must be positive"
    assert job.qubits == job.circuit.num_qubits, "qubits must match circuit.num_qubits"
    assert job.start_time >= 0, "start_time must be non-negative"
    assert job.end_time >= job.start_time, "end_time must be >= start_time"
    assert job.duration == job.end_time - job.start_time, "duration must equal end_time - start_time"


def assert_schedule_validity(schedule: List[Dict], machines: Dict[str, int]):
    """
    Validate a scheduling result.
    
    Args:
        schedule: List of scheduling dictionaries
        machines: Dictionary of machine capacities
        
    Raises:
        AssertionError: If schedule is invalid
    """
    assert isinstance(schedule, list), "schedule must be a list"
    
    for entry in schedule:
        assert "job" in entry, "schedule entry must have 'job' key"
        assert "machine" in entry, "schedule entry must have 'machine' key"
        assert "start" in entry, "schedule entry must have 'start' key"
        assert "end" in entry, "schedule entry must have 'end' key"
        assert "qubits" in entry, "schedule entry must have 'qubits' key"
        
        machine = entry["machine"]
        assert machine in machines, f"machine {machine} not in machines dictionary"
        assert entry["qubits"] <= machines[machine], "job qubits exceed machine capacity"
        assert entry["start"] >= 0, "start time must be non-negative"
        assert entry["end"] >= entry["start"], "end time must be >= start time"


# ==================== Context Managers ====================

class CaptureOutput:
    """Capture stdout and stderr for testing."""
    
    def __init__(self):
        self.stdout = ""
        self.stderr = ""
    
    def __enter__(self):
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        self.out_capture = io.StringIO()
        self.err_capture = io.StringIO()
        self.out_redirect = redirect_stdout(self.out_capture)
        self.err_redirect = redirect_stderr(self.err_capture)
        
        self.out_redirect.__enter__()
        self.err_redirect.__enter__()
        
        return self
    
    def __exit__(self, *args):
        self.stdout = self.out_capture.getvalue()
        self.stderr = self.err_capture.getvalue()
        self.out_redirect.__exit__(*args)
        self.err_redirect.__exit__(*args)


# ==================== Pytest Hooks ====================

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment before running tests."""
    # Suppress Qiskit warnings during tests
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=PendingDeprecationWarning)
    
    yield
    
    # Cleanup
    import shutil
    import os
    if os.path.exists("test_results"):
        shutil.rmtree("test_results")
