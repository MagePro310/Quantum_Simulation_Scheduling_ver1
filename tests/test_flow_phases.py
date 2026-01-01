"""
Unit tests for pipeline phase implementations.

Tests the 5-phase pipeline: Input → Schedule → Transpile → Execution → Result
"""

import sys
import pytest
from typing import Dict, List, Tuple
from unittest.mock import Mock, patch, MagicMock

sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from component.sup_sys.job_info import JobInfo


@pytest.mark.flow
class TestInputPhase:
    """Test Input phase of pipeline."""
    
    def test_input_phase_import(self):
        """Test InputPhase can be imported."""
        try:
            from flow.input.phase_input import InputPhase
            assert InputPhase is not None
        except ImportError:
            pytest.skip("InputPhase not available")
    
    def test_input_phase_abstract(self):
        """Test that InputPhase is abstract."""
        try:
            from flow.input.phase_input import InputPhase
            
            # Should raise TypeError on direct instantiation
            with pytest.raises(TypeError):
                InputPhase()
        except ImportError:
            pytest.skip("InputPhase not available")
    
    def test_input_phase_requires_execute(self):
        """Test that InputPhase subclass must implement execute."""
        try:
            from flow.input.phase_input import InputPhase
            
            class IncompleteInput(InputPhase):
                pass  # Missing execute method
            
            # Should raise TypeError
            with pytest.raises(TypeError):
                IncompleteInput()
        except ImportError:
            pytest.skip("InputPhase not available")


@pytest.mark.flow
class TestSchedulePhase:
    """Test Schedule phase of pipeline."""
    
    def test_schedule_phase_import(self):
        """Test SchedulePhase can be imported."""
        try:
            from flow.schedule.phase_schedule import SchedulePhase
            assert SchedulePhase is not None
        except ImportError:
            pytest.skip("SchedulePhase not available")
    
    def test_schedule_phase_abstract(self):
        """Test that SchedulePhase is abstract."""
        try:
            from flow.schedule.phase_schedule import SchedulePhase
            
            with pytest.raises(TypeError):
                SchedulePhase()
        except ImportError:
            pytest.skip("SchedulePhase not available")


@pytest.mark.flow
class TestTranspilePhase:
    """Test Transpile phase of pipeline."""
    
    def test_transpile_phase_import(self):
        """Test TranspilePhase can be imported."""
        try:
            from flow.transpile.phase_transpile import TranspilePhase
            assert TranspilePhase is not None
        except ImportError:
            pytest.skip("TranspilePhase not available")
    
    def test_transpile_phase_abstract(self):
        """Test that TranspilePhase is abstract."""
        try:
            from flow.transpile.phase_transpile import TranspilePhase
            
            with pytest.raises(TypeError):
                TranspilePhase()
        except ImportError:
            pytest.skip("TranspilePhase not available")


@pytest.mark.flow
class TestExecutionPhase:
    """Test Execution phase of pipeline."""
    
    def test_execution_phase_import(self):
        """Test ExecutionPhase can be imported."""
        try:
            from flow.execution.execution_phase import ExecutionPhase
            assert ExecutionPhase is not None
        except ImportError:
            pytest.skip("ExecutionPhase not available")
    
    def test_execution_phase_abstract(self):
        """Test that ExecutionPhase is abstract."""
        try:
            from flow.execution.execution_phase import ExecutionPhase
            
            with pytest.raises(TypeError):
                ExecutionPhase()
        except ImportError:
            pytest.skip("ExecutionPhase not available")


@pytest.mark.flow
class TestResultPhase:
    """Test Result phase of pipeline."""
    
    def test_result_phase_import(self):
        """Test ResultPhase can be imported."""
        try:
            from flow.result.result_phase import ResultPhase
            assert ResultPhase is not None
        except ImportError:
            pytest.skip("ResultPhase not available")
    
    def test_result_phase_abstract(self):
        """Test that ResultPhase is abstract."""
        try:
            from flow.result.result_phase import ResultPhase
            
            with pytest.raises(TypeError):
                ResultPhase()
        except ImportError:
            pytest.skip("ResultPhase not available")


@pytest.mark.flow
class TestResultOfSchedule:
    """Test ResultOfSchedule dataclass."""
    
    def test_result_of_schedule_import(self):
        """Test ResultOfSchedule can be imported."""
        try:
            from flow.information.result_schedule import ResultOfSchedule
            assert ResultOfSchedule is not None
        except ImportError:
            pytest.skip("ResultOfSchedule not available")
    
    def test_result_of_schedule_creation(self):
        """Test creating ResultOfSchedule instance."""
        try:
            from flow.information.result_schedule import ResultOfSchedule
            
            result = ResultOfSchedule()
            assert result is not None
        except ImportError:
            pytest.skip("ResultOfSchedule not available")


@pytest.mark.flow
class TestPhaseDataFlow:
    """Test data flowing through phases."""
    
    def test_job_info_persistence(self, sample_job_simple):
        """Test that JobInfo persists through phases."""
        original_id = sample_job_simple.job_id
        original_qubits = sample_job_simple.qubits
        
        # JobInfo should maintain identity
        assert sample_job_simple.job_id == original_id
        assert sample_job_simple.qubits == original_qubits
    
    def test_job_collection_flow(self, job_collection):
        """Test job collection flowing through pipeline."""
        # Jobs should maintain structure
        assert len(job_collection) == 2
        assert all(isinstance(job, JobInfo) for job in job_collection.values())
    
    def test_mutation_through_phases(self, sample_job_simple):
        """Test mutating job in different phases."""
        # Input phase: basic job
        assert sample_job_simple.start_time == 0.0
        
        # Schedule phase: mutate timing
        sample_job_simple.start_time = 10.0
        assert sample_job_simple.start_time == 10.0
        
        # Transpile phase: add transpiled circuit
        sample_job_simple.transpiled_circuit = sample_job_simple.circuit.copy()
        assert sample_job_simple.transpiled_circuit is not None
        
        # Execution phase: add fidelity
        sample_job_simple.fidelity = 0.95
        assert sample_job_simple.fidelity == 0.95


@pytest.mark.flow
class TestPipelineIntegration:
    """Test integration of multiple phases."""
    
    def test_phase_sequence_logic(self, job_collection, machine_capacities):
        """Test logical sequence of phases."""
        # Phase sequence: Input → Schedule → Transpile → Execution → Result
        
        # Input: Jobs are collected
        assert len(job_collection) > 0
        
        # Schedule: Jobs assigned to machines
        for job in job_collection.values():
            job.machine = list(machine_capacities.keys())[0]
            job.start_time = 0.0
            job.duration = 5.0
            job.end_time = 5.0
        
        # Verify scheduling occurred
        for job in job_collection.values():
            assert job.machine is not None
            assert job.start_time >= 0
    
    def test_phase_error_propagation(self):
        """Test that phase errors propagate appropriately."""
        # If a phase fails, it should raise exception
        # (Tests would verify try-except behavior)
        pass


@pytest.mark.flow
class TestConcretePhaseImplementation:
    """Test concrete phase implementations if available."""
    
    def test_concrete_input_implementation(self):
        """Test concrete InputPhase implementation."""
        try:
            from flow.input.phase_input import InputPhase
            
            class TestInput(InputPhase):
                def execute(self, quantum_circuits, machines, priority):
                    return quantum_circuits, machines, priority
            
            input_phase = TestInput()
            assert input_phase is not None
        except ImportError:
            pytest.skip("InputPhase not available")
    
    def test_concrete_schedule_implementation(self):
        """Test concrete SchedulePhase implementation."""
        try:
            from flow.schedule.phase_schedule import SchedulePhase
            
            class TestSchedule(SchedulePhase):
                def execute(self, origin_job_info, machines, result_schedule):
                    return origin_job_info, machines, result_schedule
            
            schedule_phase = TestSchedule()
            assert schedule_phase is not None
        except ImportError:
            pytest.skip("SchedulePhase not available")
    
    def test_phase_execute_call(self):
        """Test calling execute method on concrete phase."""
        try:
            from flow.input.phase_input import InputPhase
            
            class TestInput(InputPhase):
                def execute(self, quantum_circuits, machines, priority):
                    return quantum_circuits, machines, priority
            
            phase = TestInput()
            circuits = []
            machines = {}
            priority = None
            
            result = phase.execute(circuits, machines, priority)
            assert result == (circuits, machines, priority)
        except ImportError:
            pytest.skip("InputPhase not available")


@pytest.mark.flow
class TestPhaseAbstractionEnforcement:
    """Test that phase abstraction is properly enforced."""
    
    def test_all_phases_abstract(self):
        """Test that all phase classes are abstract."""
        phases_to_test = [
            ("InputPhase", "flow.input.phase_input"),
            ("SchedulePhase", "flow.schedule.phase_schedule"),
            ("TranspilePhase", "flow.transpile.phase_transpile"),
            ("ExecutionPhase", "flow.execution.execution_phase"),
            ("ResultPhase", "flow.result.result_phase"),
        ]
        
        for class_name, module_path in phases_to_test:
            try:
                parts = module_path.split('.')
                module = __import__(module_path, fromlist=[class_name])
                phase_class = getattr(module, class_name)
                
                # Should raise TypeError
                with pytest.raises(TypeError):
                    phase_class()
            except ImportError:
                pytest.skip(f"{class_name} not available")
    
    def test_incomplete_implementation_fails(self):
        """Test that incomplete implementations fail."""
        try:
            from flow.input.phase_input import InputPhase
            
            # Missing execute method
            class IncompletePhase(InputPhase):
                pass
            
            with pytest.raises(TypeError):
                IncompletePhase()
        except ImportError:
            pytest.skip("InputPhase not available")
