"""
Test Suite for Quantum Simulation Scheduling
=============================================

This package contains all unit and integration tests for the framework.

Test Organization:
    - test_flow_abstraction.py: Tests ABC pattern enforcement
    - test_flow_concrete.py: Tests concrete phase implementations
    - test_debug_output.py: Tests debug logging functionality

Running Tests:
    # Run all tests
    pytest tests/
    
    # Run specific test file
    pytest tests/test_flow_concrete.py
    
    # Run with coverage
    pytest tests/ --cov=component --cov=flow --cov=benchmarks
    
    # Run with verbose output
    pytest tests/ -v

Requirements:
    - Must activate conda environment: conda activate squan
    - All dependencies must be installed: pip install -r requirements.txt
"""

__version__ = "1.0.0"
