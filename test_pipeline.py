#!/usr/bin/env python3
"""
Test script for the Quantum Scheduling Pipeline.

This script runs basic functionality tests to ensure the pipeline works correctly.
"""

import sys
import os
import tempfile
import json
from typing import Dict, Any

# Add the current directory to the path for imports
sys.path.append('.')

try:
    from quantum_scheduling_pipeline import QuantumSchedulingPipeline, SchedulingMetrics
    from config import PipelineConfig, SimulationMode, SchedulingAlgorithm
    from component.utils import setup_logging
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you're running this from the correct directory and all dependencies are installed.")
    sys.exit(1)


def test_configuration():
    """Test configuration creation and validation."""
    print("Testing configuration...")
    
    # Test default configuration
    config = PipelineConfig()
    assert config.num_qubits_per_job == 7
    assert config.num_jobs == 2
    assert config.simulation_mode == SimulationMode.MULTI_THREADED
    
    # Test custom configuration
    custom_config = PipelineConfig(
        num_qubits_per_job=5,
        num_jobs=3,
        simulation_mode=SimulationMode.SINGLE_THREADED,
        backend_names=['belem'],
        shots=512
    )
    assert custom_config.num_qubits_per_job == 5
    assert custom_config.shots == 512
    
    # Test validation
    try:
        custom_config.validate()
        print("✓ Configuration validation passed")
    except Exception as e:
        print(f"✗ Configuration validation failed: {e}")
        return False
    
    return True


def test_pipeline_initialization():
    """Test pipeline initialization."""
    print("Testing pipeline initialization...")
    
    try:
        config = PipelineConfig(
            num_qubits_per_job=3,
            num_jobs=1,
            log_level="ERROR"  # Suppress logs for testing
        )
        pipeline = QuantumSchedulingPipeline(config)
        
        assert pipeline.num_qubits_per_job == 3
        assert pipeline.num_jobs == 1
        assert len(pipeline.machines) == 0  # Not set up yet
        
        print("✓ Pipeline initialization passed")
        return True
    except Exception as e:
        print(f"✗ Pipeline initialization failed: {e}")
        return False


def test_metrics_dataclass():
    """Test metrics data structure."""
    print("Testing metrics data structure...")
    
    try:
        metrics = SchedulingMetrics()
        assert metrics.num_circuits == 0
        assert metrics.average_fidelity == 0.0
        
        # Test setting values
        metrics.num_circuits = 5
        metrics.average_fidelity = 0.95
        
        assert metrics.num_circuits == 5
        assert metrics.average_fidelity == 0.95
        
        print("✓ Metrics data structure passed")
        return True
    except Exception as e:
        print(f"✗ Metrics data structure failed: {e}")
        return False


def test_configuration_serialization():
    """Test configuration save/load functionality."""
    print("Testing configuration serialization...")
    
    try:
        # Create a test configuration
        config = PipelineConfig(
            num_qubits_per_job=10,
            num_jobs=4,
            simulation_mode=SimulationMode.SINGLE_THREADED,
            backend_names=['belem', 'manila'],
            experiment_id="test_experiment"
        )
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name
            
            # Convert to dict for JSON serialization
            config_dict = config.__dict__.copy()
            config_dict['simulation_mode'] = config_dict['simulation_mode'].value
            config_dict['scheduling_algorithm'] = config_dict['scheduling_algorithm'].value
            
            json.dump(config_dict, f, indent=2)
        
        # Load the configuration back
        with open(temp_path, 'r') as f:
            loaded_dict = json.load(f)
            
        # Verify values
        assert loaded_dict['num_qubits_per_job'] == 10
        assert loaded_dict['num_jobs'] == 4
        assert loaded_dict['simulation_mode'] == 'single_threaded'
        
        # Clean up
        os.unlink(temp_path)
        
        print("✓ Configuration serialization passed")
        return True
    except Exception as e:
        print(f"✗ Configuration serialization failed: {e}")
        return False


def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    
    required_modules = [
        'qiskit',
        'qiskit_aer',
        'qiskit_ibm_runtime',
        'numpy',
        'matplotlib'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError as e:
            print(f"✗ Failed to import {module}: {e}")
            return False
    
    print("✓ All required modules imported successfully")
    return True


def run_all_tests():
    """Run all tests and report results."""
    print("="*60)
    print("QUANTUM SCHEDULING PIPELINE TEST SUITE")
    print("="*60)
    
    tests = [
        test_imports,
        test_configuration,
        test_pipeline_initialization,
        test_metrics_dataclass,
        test_configuration_serialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Add spacing between tests
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
            print()
    
    print("="*60)
    print(f"TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed. Please check the output above.")
        return False


def main():
    """Main test execution."""
    success = run_all_tests()
    
    if not success:
        sys.exit(1)
    
    print("\n" + "="*60)
    print("READY TO RUN QUANTUM SCHEDULING PIPELINE")
    print("="*60)
    print("The pipeline is ready for use. You can now run:")
    print("  python main.py --help")
    print("  python main.py")
    print("  python quantum_scheduling_pipeline.py")


if __name__ == "__main__":
    main()
