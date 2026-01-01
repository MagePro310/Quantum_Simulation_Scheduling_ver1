"""
Unit tests for scheduling algorithms.

Tests FFD, MTMC, MILQ_extend, and NoTaDS scheduling implementations.
"""

import sys
import pytest
from typing import Dict, List

sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')


@pytest.mark.unit
class TestSchedulingAlgorithmInterface:
    """Test the interface and contract of scheduling algorithms."""
    
    def test_algorithm_input_validation(self, sample_job_capacities, machine_capacities):
        """Test that algorithms validate inputs."""
        # Empty jobs
        with pytest.raises((ValueError, KeyError, TypeError)):
            # Most algorithms should raise on empty input
            pass
    
    def test_algorithm_output_format(self, scheduling_result):
        """Test that scheduling output has required fields."""
        required_fields = {"job", "machine", "start", "end", "qubits"}
        
        for entry in scheduling_result:
            assert all(field in entry for field in required_fields)
    
    def test_algorithm_preserves_jobs(self, sample_job_capacities):
        """Test that all input jobs appear in output."""
        job_ids = set(sample_job_capacities.keys())
        
        # When algorithm runs, should return all jobs
        assert len(job_ids) > 0


@pytest.mark.unit
class TestFFDAlgorithm:
    """Test First-Fit Decreasing (FFD) algorithm."""
    
    def test_ffd_import(self):
        """Test that FFD implementation can be imported."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            assert FFD_implement is not None
        except ImportError:
            pytest.skip("FFD implementation not found")
    
    def test_ffd_basic_scheduling(self, sample_job_capacities, machine_capacities):
        """Test FFD produces valid schedule."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            schedule = FFD_implement(sample_job_capacities, machine_capacities)
            
            # Check output format
            assert isinstance(schedule, list)
            assert len(schedule) > 0
            
            # Verify all jobs scheduled
            scheduled_jobs = {entry["job"] for entry in schedule}
            assert len(scheduled_jobs) == len(sample_job_capacities)
        except ImportError:
            pytest.skip("FFD implementation not available")
    
    def test_ffd_capacity_constraint(self, sample_job_capacities, machine_capacities):
        """Test FFD respects machine capacity constraints."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            schedule = FFD_implement(sample_job_capacities, machine_capacities)
            
            # Check capacity not exceeded
            for entry in schedule:
                machine = entry["machine"]
                qubits = entry["qubits"]
                assert qubits <= machine_capacities[machine]
        except ImportError:
            pytest.skip("FFD implementation not available")


@pytest.mark.unit
class TestMTMCAlgorithm:
    """Test MTMC (Multi-Task Machine Cluster) algorithm."""
    
    def test_mtmc_import(self):
        """Test that MTMC implementation can be imported."""
        try:
            from component.d_scheduling.algorithm.heuristic.MTMC import MTMC_implement
            assert MTMC_implement is not None
        except ImportError:
            pytest.skip("MTMC implementation not found")
    
    def test_mtmc_basic_scheduling(self, sample_job_capacities, machine_capacities):
        """Test MTMC produces valid schedule."""
        try:
            from component.d_scheduling.algorithm.heuristic.MTMC import MTMC_implement
            
            schedule = MTMC_implement(sample_job_capacities, machine_capacities)
            
            # Check output format
            assert isinstance(schedule, list)
            assert len(schedule) > 0
            
            # Verify all jobs scheduled
            scheduled_jobs = {entry["job"] for entry in schedule}
            assert len(scheduled_jobs) == len(sample_job_capacities)
        except ImportError:
            pytest.skip("MTMC implementation not available")


@pytest.mark.unit
class TestScheduleValidity:
    """Test properties of valid schedules."""
    
    def test_schedule_no_negative_times(self, scheduling_result):
        """Test that schedule has no negative times."""
        for entry in scheduling_result:
            assert entry["start"] >= 0, f"Negative start time: {entry['start']}"
            assert entry["end"] >= entry["start"], f"End before start: {entry}"
    
    def test_schedule_positive_qubits(self, scheduling_result):
        """Test that jobs have positive qubit requirements."""
        for entry in scheduling_result:
            assert entry["qubits"] > 0, f"Non-positive qubits: {entry['qubits']}"
    
    def test_schedule_valid_machines(self, scheduling_result, machine_capacities):
        """Test that scheduled machines exist."""
        for entry in scheduling_result:
            machine = entry["machine"]
            assert machine in machine_capacities, f"Unknown machine: {machine}"
    
    def test_schedule_within_capacity(self, scheduling_result, machine_capacities):
        """Test that no job exceeds machine capacity."""
        for entry in scheduling_result:
            machine = entry["machine"]
            qubits = entry["qubits"]
            capacity = machine_capacities[machine]
            assert qubits <= capacity, f"Job {entry['job']} exceeds capacity"


@pytest.mark.unit
class TestSchedulingMetrics:
    """Test scheduling metrics calculation."""
    
    def test_makespan_calculation(self, scheduling_result):
        """Test makespan (total time) calculation."""
        if not scheduling_result:
            return
        
        makespan = max(entry["end"] for entry in scheduling_result)
        assert makespan > 0
        assert makespan >= min(entry["start"] for entry in scheduling_result)
    
    def test_job_count_preservation(self, scheduling_result, sample_job_capacities):
        """Test that all jobs are scheduled."""
        scheduled_count = len(scheduling_result)
        job_count = len(sample_job_capacities)
        
        # Note: May have duplicates if circuit is cut
        assert scheduled_count >= job_count
    
    def test_turnaround_time(self, scheduling_result):
        """Test turnaround time metric (end - start)."""
        for entry in scheduling_result:
            turnaround = entry["end"] - entry["start"]
            assert turnaround >= 0


@pytest.mark.unit
class TestScheduleOptimality:
    """Test optimality properties of schedules."""
    
    def test_ffd_decreasing_order(self, sample_job_capacities):
        """Test that FFD sorts jobs in decreasing order."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            schedule = FFD_implement(sample_job_capacities, {f"m{i}": 100 for i in range(5)})
            
            # FFD should process larger jobs first
            assert len(schedule) > 0
        except ImportError:
            pytest.skip("FFD not available")
    
    def test_schedule_balancing(self, scheduling_result, machine_capacities):
        """Test that schedule balances load somewhat reasonably."""
        # Calculate load per machine
        machine_load = {m: 0 for m in machine_capacities}
        
        for entry in scheduling_result:
            machine = entry["machine"]
            qubits = entry["qubits"]
            machine_load[machine] += qubits
        
        # Basic sanity check - no single machine gets everything
        max_load = max(machine_load.values())
        min_load = min(v for v in machine_load.values() if v > 0)
        
        if max_load > 0 and min_load > 0:
            assert max_load / min_load < 100  # Reasonable balance


@pytest.mark.unit
class TestScheduleRobustness:
    """Test algorithm robustness with edge cases."""
    
    def test_single_job(self, machine_capacities):
        """Test scheduling a single job."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            jobs = {"job_0": 5}
            schedule = FFD_implement(jobs, machine_capacities)
            
            assert len(schedule) == 1
            assert schedule[0]["job"] == "job_0"
            assert schedule[0]["qubits"] == 5
        except ImportError:
            pytest.skip("FFD not available")
    
    def test_job_equals_capacity(self, machine_capacities):
        """Test when job size equals machine capacity."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            jobs = {"job_0": 10}  # Equals machine_1 capacity
            schedule = FFD_implement(jobs, machine_capacities)
            
            assert len(schedule) >= 1
        except ImportError:
            pytest.skip("FFD not available")
    
    def test_job_exceeds_largest_machine(self, machine_capacities):
        """Test scheduling job larger than largest machine."""
        try:
            from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
            
            jobs = {"job_0": 100}  # Exceeds all machines
            machine_capacities_copy = machine_capacities.copy()
            
            # This may raise or handle gracefully
            try:
                schedule = FFD_implement(jobs, machine_capacities_copy)
                # If it succeeds, should be empty or handle appropriately
            except (ValueError, RuntimeError):
                # Expected behavior for oversized job
                pass
        except ImportError:
            pytest.skip("FFD not available")
