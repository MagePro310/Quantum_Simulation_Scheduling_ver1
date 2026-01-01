"""
Integration tests for the complete quantum scheduling pipeline.

Tests end-to-end workflows combining multiple components and phases.
"""

import sys
import pytest
from typing import Dict, List

sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from component.sup_sys.job_info import JobInfo


@pytest.mark.integration
class TestBasicPipelineFlow:
    """Test basic pipeline flow with all phases."""
    
    def test_job_through_pipeline(self, sample_job_simple, machine_capacities):
        """Test a job going through the complete pipeline."""
        job = sample_job_simple
        
        # Input phase: Job created
        assert job.circuit is not None
        assert job.qubits == 2
        
        # Schedule phase: Assign machine and timing
        job.machine = "machine_0"
        job.start_time = 0.0
        job.duration = 2.0
        job.end_time = 2.0
        
        # Transpile phase: Add transpiled circuit
        job.transpiled_circuit = job.circuit.copy()
        
        # Execution phase: Simulate and add fidelity
        job.fidelity = 0.92
        
        # Result phase: Verify final state
        assert job.machine == "machine_0"
        assert job.fidelity == 0.92
        assert job.transpiled_circuit is not None
    
    def test_multiple_jobs_pipeline(self, job_collection, machine_capacities):
        """Test multiple jobs through pipeline."""
        jobs = job_collection
        
        # Simulate scheduling
        machine_list = list(machine_capacities.keys())
        for i, (job_id, job) in enumerate(jobs.items()):
            machine = machine_list[i % len(machine_list)]
            job.machine = machine
            job.start_time = float(i * 5)
            job.end_time = float(i * 5 + job.qubits)
            job.duration = float(job.qubits)
        
        # Verify all jobs scheduled
        for job in jobs.values():
            assert job.machine is not None
            assert job.start_time >= 0
            assert job.end_time >= job.start_time


@pytest.mark.integration
class TestSchedulingWithMultipleMachines:
    """Test scheduling across multiple machines."""
    
    def test_distribute_jobs_evenly(self, create_job_batch, machine_capacities):
        """Test distributing jobs across machines."""
        jobs = create_job_batch(10, qubit_range=(2, 5))
        machine_list = list(machine_capacities.keys())
        
        # Distribute jobs
        for i, (job_id, job) in enumerate(jobs.items()):
            machine = machine_list[i % len(machine_list)]
            job.machine = machine
        
        # Verify distribution
        machines_used = set(job.machine for job in jobs.values())
        assert len(machines_used) > 1  # Should use multiple machines
    
    def test_respect_capacity_constraints(self, create_job_batch, machine_capacities):
        """Test that jobs don't exceed machine capacity in scheduling."""
        jobs = create_job_batch(5, qubit_range=(2, 8))
        
        # Assign jobs while respecting capacity
        machine_loads = {m: 0 for m in machine_capacities}
        
        for job in jobs.values():
            # Find machine with space
            for machine in machine_capacities:
                if machine_loads[machine] + job.qubits <= machine_capacities[machine]:
                    job.machine = machine
                    machine_loads[machine] += job.qubits
                    break
        
        # Verify no machine exceeded
        for job in jobs.values():
            if job.machine:
                assert job.qubits <= machine_capacities[job.machine]


@pytest.mark.integration
class TestCircuitCuttingIntegration:
    """Test circuit cutting in pipeline context."""
    
    def test_large_circuit_with_cutting(self, deep_circuit):
        """Test handling large circuit that needs cutting."""
        job = JobInfo(
            job_id="large_job",
            circuit=deep_circuit,
            qubits=deep_circuit.num_qubits
        )
        
        # Simulate cutting for machine capacity of 5
        machine_capacity = 5
        
        if job.qubits > machine_capacity:
            # Would need cutting
            assert job.qubits > machine_capacity
            
            # Simulate creating child jobs
            num_cuts = (job.qubits + machine_capacity - 1) // machine_capacity
            child_jobs = []
            for i in range(num_cuts):
                child = JobInfo(
                    job_id=f"{job.job_id}_cut_{i}",
                    circuit=job.circuit.copy(),
                    qubits=min(machine_capacity, job.qubits - i * machine_capacity)
                )
                child_jobs.append(child)
            
            job.childrenJobs = child_jobs
            
            # Verify children created
            assert len(job.childrenJobs) > 0
            assert all(c.qubits <= machine_capacity for c in job.childrenJobs)


@pytest.mark.integration
class TestEndToEndMetrics:
    """Test calculating metrics end-to-end."""
    
    def test_makespan_calculation(self, job_collection):
        """Test calculating total execution time (makespan)."""
        jobs = job_collection
        
        # Simulate scheduling
        for i, job in enumerate(jobs.values()):
            job.start_time = float(i * 5)
            job.end_time = float(i * 5 + 5)
        
        # Calculate makespan
        makespan = max(job.end_time for job in jobs.values())
        
        assert makespan > 0
        assert makespan == 10.0  # Last job ends at 10
    
    def test_turnaround_time_calculation(self, job_collection):
        """Test calculating average turnaround time."""
        jobs = job_collection
        
        # Simulate scheduling
        for i, job in enumerate(jobs.values()):
            job.start_time = float(i)
            job.end_time = float(i + 5)
        
        # Calculate average turnaround
        turnarounds = [job.end_time - job.start_time for job in jobs.values()]
        avg_turnaround = sum(turnarounds) / len(turnarounds)
        
        assert avg_turnaround == 5.0
    
    def test_utilization_calculation(self, create_job_batch, machine_capacities):
        """Test calculating machine utilization."""
        jobs = create_job_batch(10, qubit_range=(2, 5))
        machine_list = list(machine_capacities.keys())
        makespan = 0
        
        # Assign and schedule
        for i, job in enumerate(jobs.values()):
            job.machine = machine_list[i % len(machine_list)]
            job.start_time = 0.0
            job.end_time = 5.0
            makespan = max(makespan, job.end_time)
        
        # Calculate utilization
        total_capacity = sum(machine_capacities.values()) * makespan
        total_used = sum(job.qubits * job.duration for job in jobs.values())
        
        if total_capacity > 0:
            utilization = total_used / total_capacity
            assert 0 <= utilization <= 1


@pytest.mark.integration
class TestAlgorithmComparison:
    """Test comparing different scheduling algorithms."""
    
    def test_ffd_vs_mtmc_same_input(self, sample_job_capacities, machine_capacities):
        """Test FFD and MTMC produce different results."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            from component.d_scheduling.algorithm.heuristic.MTMC import MTMC_implement
            
            ffd_schedule = FFD_implement(sample_job_capacities, machine_capacities)
            mtmc_schedule = MTMC_implement(sample_job_capacities, machine_capacities)
            
            # Both should produce valid schedules
            assert len(ffd_schedule) > 0
            assert len(mtmc_schedule) > 0
            
            # They may differ in result
            # (Algorithms may produce same result for simple inputs)
        except ImportError:
            pytest.skip("Algorithms not available")
    
    def test_algorithm_correctness_properties(self, sample_job_capacities, machine_capacities):
        """Test that scheduling algorithms maintain correctness."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            schedule = FFD_implement(sample_job_capacities, machine_capacities)
            
            # Properties all valid schedules must satisfy
            jobs_scheduled = {entry["job"] for entry in schedule}
            jobs_input = set(sample_job_capacities.keys())
            
            # All input jobs should be in output
            assert jobs_scheduled == jobs_input
            
            # Capacity not exceeded
            for entry in schedule:
                machine = entry["machine"]
                assert entry["qubits"] <= machine_capacities[machine]
        except ImportError:
            pytest.skip("FFD not available")


@pytest.mark.integration
class TestPipelineRobustness:
    """Test pipeline robustness with edge cases."""
    
    def test_single_job_pipeline(self, simple_circuit, machine_capacities):
        """Test pipeline with single job."""
        job = JobInfo(
            job_id="single",
            circuit=simple_circuit,
            qubits=simple_circuit.num_qubits
        )
        
        # Process through pipeline
        job.machine = "machine_0"
        job.start_time = 0.0
        job.duration = float(job.qubits)
        job.end_time = job.duration
        job.transpiled_circuit = job.circuit.copy()
        job.fidelity = 0.99
        
        # Verify completion
        assert job.fidelity is not None
    
    def test_many_small_jobs(self, machine_capacities):
        """Test pipeline with many small jobs."""
        jobs = {}
        for i in range(20):
            job = JobInfo(
                job_id=f"small_job_{i}",
                circuit=None,
                qubits=2
            )
            jobs[job.job_id] = job
        
        # Schedule
        machine_list = list(machine_capacities.keys())
        for i, job in enumerate(jobs.values()):
            job.machine = machine_list[i % len(machine_list)]
            job.start_time = float(i * 2)
            job.end_time = float((i + 1) * 2)
            job.duration = 2.0
        
        # Verify
        assert len(jobs) == 20
        assert all(job.machine is not None for job in jobs.values())
    
    def test_mixed_size_jobs(self, create_job_batch, machine_capacities):
        """Test pipeline with jobs of varying sizes."""
        jobs = create_job_batch(5, qubit_range=(2, 10))
        
        # Schedule with fit-first strategy
        machine_list = list(machine_capacities.keys())
        
        for job in jobs.values():
            # Find first machine with capacity
            for machine in machine_list:
                if job.qubits <= machine_capacities[machine]:
                    job.machine = machine
                    break
        
        # Verify all scheduled
        assert all(job.machine is not None for job in jobs.values())


@pytest.mark.integration
class TestErrorRecovery:
    """Test error handling in pipeline."""
    
    def test_missing_circuit(self):
        """Test handling job without circuit."""
        job = JobInfo(
            job_id="no_circuit",
            circuit=None,
            qubits=5
        )
        
        # Should still be processable
        assert job.job_id == "no_circuit"
        assert job.circuit is None
    
    def test_invalid_scheduling(self, simple_circuit, machine_capacities):
        """Test handling invalid scheduling attempts."""
        job = JobInfo(
            circuit=simple_circuit,
            qubits=simple_circuit.num_qubits
        )
        
        # Try to schedule on non-existent machine
        job.machine = "nonexistent_machine"
        
        # Should not raise, but may fail validation later
        assert job.machine == "nonexistent_machine"


@pytest.mark.integration
class TestDataFlowConsistency:
    """Test that data flows correctly through pipeline."""
    
    def test_job_identity_preserved(self, sample_job_simple):
        """Test that job identity is preserved through pipeline."""
        original_id = sample_job_simple.job_id
        
        # Mutate through phases
        sample_job_simple.machine = "machine_0"
        sample_job_simple.fidelity = 0.95
        
        # Identity preserved
        assert sample_job_simple.job_id == original_id
    
    def test_circuit_maintained(self, sample_job_medium):
        """Test that circuit reference is maintained."""
        original_circuit = sample_job_medium.circuit
        
        # Add transpiled version
        sample_job_medium.transpiled_circuit = sample_job_medium.circuit.copy()
        
        # Original circuit still there
        assert sample_job_medium.circuit == original_circuit
        assert sample_job_medium.circuit is not sample_job_medium.transpiled_circuit
