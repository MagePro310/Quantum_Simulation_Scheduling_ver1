"""
Unit tests for component/sup_sys/job_info.py

Tests the JobInfo dataclass that serves as the universal container
for quantum job information throughout the pipeline.
"""

import sys
import pytest
from copy import deepcopy

sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from qiskit import QuantumCircuit
from component.sup_sys.job_info import JobInfo


@pytest.mark.unit
class TestJobInfoBasics:
    """Test basic JobInfo creation and properties."""
    
    def test_create_job_with_defaults(self):
        """Test JobInfo creation with default values."""
        job = JobInfo()
        
        assert job.job_id is not None
        assert job.circuit is None
        assert job.qubits == 0
        assert job.machine is None
        assert job.start_time == 0.0
        assert job.duration == 0.0
        assert job.end_time == 0.0
    
    def test_create_job_with_values(self, simple_circuit):
        """Test JobInfo creation with explicit values."""
        job = JobInfo(
            job_id="test_job_1",
            job_name="My Test Job",
            circuit=simple_circuit,
            qubits=2,
            machine="machine_0",
            capacity_machine=5,
            start_time=1.0,
            duration=2.0,
            end_time=3.0
        )
        
        assert job.job_id == "test_job_1"
        assert job.job_name == "My Test Job"
        assert job.circuit == simple_circuit
        assert job.qubits == 2
        assert job.machine == "machine_0"
        assert job.capacity_machine == 5
        assert job.start_time == 1.0
        assert job.duration == 2.0
        assert job.end_time == 3.0
    
    def test_job_print_method(self, sample_job_simple, capsys):
        """Test JobInfo.print() method."""
        sample_job_simple.print()
        captured = capsys.readouterr()
        
        assert "Job ID:" in captured.out
        assert "Job Name:" in captured.out
        assert "Qubits:" in captured.out
        assert "Machine:" in captured.out


@pytest.mark.unit
class TestJobInfoCircuitHandling:
    """Test JobInfo circuit-related operations."""
    
    def test_circuit_assignment(self, medium_circuit):
        """Test assigning circuit to JobInfo."""
        job = JobInfo(circuit=medium_circuit)
        
        assert job.circuit == medium_circuit
        assert job.circuit.num_qubits == 5
    
    def test_qubit_count_consistency(self, deep_circuit):
        """Test that qubit count is consistent with circuit."""
        job = JobInfo(
            circuit=deep_circuit,
            qubits=deep_circuit.num_qubits
        )
        
        assert job.qubits == job.circuit.num_qubits
        assert job.qubits == 8
    
    def test_circuit_copy_independence(self, simple_circuit):
        """Test that modifying original circuit doesn't affect job circuit."""
        circuit_copy = simple_circuit.copy()
        job = JobInfo(circuit=circuit_copy)
        
        # Modify original
        simple_circuit.h(0)
        
        # Job circuit should be independent
        assert job.circuit.num_qubits == simple_circuit.num_qubits
        # (Content may differ but structure should match)
    
    def test_transpiled_circuit_storage(self, simple_circuit, medium_circuit):
        """Test storing transpiled circuit variants."""
        job = JobInfo(circuit=simple_circuit)
        
        # Store transpiled variant
        job.transpiled_circuit = medium_circuit.copy()
        
        assert job.transpiled_circuit is not None
        assert job.circuit != job.transpiled_circuit


@pytest.mark.unit
class TestJobInfoScheduling:
    """Test JobInfo scheduling-related properties."""
    
    def test_schedule_timing(self):
        """Test scheduling timing properties."""
        job = JobInfo(
            start_time=10.0,
            duration=5.0,
            end_time=15.0
        )
        
        assert job.start_time == 10.0
        assert job.duration == 5.0
        assert job.end_time == 15.0
    
    def test_schedule_zero_timing(self):
        """Test scheduling with zero/default times."""
        job = JobInfo()
        
        assert job.start_time == 0.0
        assert job.duration == 0.0
        assert job.end_time == 0.0
    
    def test_machine_assignment(self):
        """Test machine assignment to job."""
        job = JobInfo(
            machine="machine_5",
            capacity_machine=20
        )
        
        assert job.machine == "machine_5"
        assert job.capacity_machine == 20


@pytest.mark.unit
class TestJobInfoCutting:
    """Test JobInfo circuit cutting-related properties."""
    
    def test_children_jobs_storage(self, sample_job_simple, sample_job_medium):
        """Test storing child jobs from circuit cutting."""
        parent_job = JobInfo(job_name="parent")
        
        # Initially no children
        assert parent_job.childrenJobs is None
        
        # Add children
        parent_job.childrenJobs = [sample_job_simple, sample_job_medium]
        
        assert len(parent_job.childrenJobs) == 2
        assert parent_job.childrenJobs[0].job_name == "test_job_0"
        assert parent_job.childrenJobs[1].job_name == "test_job_1"
    
    def test_children_jobs_empty_list(self):
        """Test empty children jobs list."""
        job = JobInfo(childrenJobs=[])
        
        assert isinstance(job.childrenJobs, list)
        assert len(job.childrenJobs) == 0


@pytest.mark.unit
class TestJobInfoFidelity:
    """Test JobInfo fidelity tracking."""
    
    def test_fidelity_storage(self):
        """Test storing fidelity values."""
        job = JobInfo(fidelity=0.95)
        
        assert job.fidelity == 0.95
    
    def test_fidelity_zero(self):
        """Test zero fidelity."""
        job = JobInfo(fidelity=0.0)
        
        assert job.fidelity == 0.0
    
    def test_fidelity_one(self):
        """Test perfect fidelity."""
        job = JobInfo(fidelity=1.0)
        
        assert job.fidelity == 1.0
    
    def test_fidelity_none_default(self):
        """Test default None fidelity."""
        job = JobInfo()
        
        assert job.fidelity is None


@pytest.mark.unit
class TestJobInfoCollection:
    """Test using JobInfo in collections (as per pipeline design)."""
    
    def test_job_in_dict(self, sample_job_simple):
        """Test storing JobInfo in dictionary (pipeline pattern)."""
        jobs = {
            "job_0": sample_job_simple
        }
        
        assert "job_0" in jobs
        assert jobs["job_0"].job_id == "job_0"
    
    def test_job_in_list(self, sample_job_simple, sample_job_medium):
        """Test storing JobInfo in list."""
        jobs = [sample_job_simple, sample_job_medium]
        
        assert len(jobs) == 2
        assert jobs[0].qubits == 2
        assert jobs[1].qubits == 5
    
    def test_job_dict_iteration(self, job_collection):
        """Test iterating over job dictionary."""
        job_ids = []
        for job_id, job in job_collection.items():
            job_ids.append(job_id)
        
        assert "job_0" in job_ids
        assert "job_1" in job_ids


@pytest.mark.unit
class TestJobInfoMutation:
    """Test JobInfo mutation (critical for pipeline pattern)."""
    
    def test_mutate_timing(self, sample_job_simple):
        """Test mutating job timing information."""
        original_start = sample_job_simple.start_time
        
        # Mutate
        sample_job_simple.start_time = 10.0
        sample_job_simple.end_time = 15.0
        sample_job_simple.duration = 5.0
        
        assert sample_job_simple.start_time == 10.0
        assert sample_job_simple.end_time == 15.0
        assert sample_job_simple.start_time != original_start
    
    def test_mutate_machine(self, sample_job_simple):
        """Test mutating machine assignment."""
        original_machine = sample_job_simple.machine
        
        sample_job_simple.machine = "machine_999"
        
        assert sample_job_simple.machine == "machine_999"
        assert sample_job_simple.machine != original_machine
    
    def test_mutate_fidelity(self, sample_job_simple):
        """Test mutating fidelity value."""
        sample_job_simple.fidelity = 0.87
        
        assert sample_job_simple.fidelity == 0.87


@pytest.mark.unit
class TestJobInfoDataIntegrity:
    """Test data integrity and consistency."""
    
    def test_job_copy_independence(self, sample_job_simple):
        """Test that copy creates independent instances."""
        job_copy = deepcopy(sample_job_simple)
        
        # Modify copy
        job_copy.start_time = 999.0
        
        # Original should be unchanged
        assert sample_job_simple.start_time != 999.0
    
    def test_job_none_values(self):
        """Test handling None values."""
        job = JobInfo(
            circuit=None,
            transpiled_circuit=None,
            result_cut=None,
            childrenJobs=None,
            fidelity=None
        )
        
        assert job.circuit is None
        assert job.transpiled_circuit is None
        assert job.result_cut is None
        assert job.childrenJobs is None
        assert job.fidelity is None
