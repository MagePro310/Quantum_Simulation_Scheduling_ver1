#!/bin/bash
# Makefile-style commands for project management

case "$1" in
    install)
        echo "Installing Quantum Simulation Scheduling..."
        conda activate squan 2>/dev/null || echo "Please activate conda environment: conda activate squan"
        pip install -e .
        ;;
    install-dev)
        echo "Installing with development dependencies..."
        conda activate squan 2>/dev/null || echo "Please activate conda environment: conda activate squan"
        pip install -e ".[dev]"
        ;;
    test)
        echo "Running tests..."
        pytest tests/ -v
        ;;
    test-coverage)
        echo "Running tests with coverage..."
        pytest tests/ --cov=component --cov=flow --cov=benchmarks --cov-report=html
        echo "Coverage report generated in htmlcov/index.html"
        ;;
    lint)
        echo "Running linter..."
        flake8 component flow benchmarks tests
        ;;
    format)
        echo "Formatting code with black..."
        black component flow benchmarks tests
        ;;
    type-check)
        echo "Type checking with mypy..."
        mypy component flow benchmarks
        ;;
    clean)
        echo "Cleaning up..."
        find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
        find . -type f -name "*.pyc" -delete
        find . -type f -name "*.pyo" -delete
        find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null
        rm -rf build/ dist/ htmlcov/ .pytest_cache/ .mypy_cache/
        echo "Cleanup complete"
        ;;
    benchmark)
        echo "Running benchmarks..."
        cd benchmarks/comparison
        python comparison_runner.py
        ;;
    benchmark-ffd)
        echo "Running FFD benchmark..."
        cd benchmarks/comparison/config
        python runLoopTestFFD.py ${2:-5} ${3:-8}
        ;;
    visualize)
        echo "Generating algorithm comparison visualizations..."
        cd benchmarks/comparison
        python visualize_results.py
        ;;
    visualize-chart)
        echo "Generating specific chart: ${2:-all}"
        cd benchmarks/comparison/analysis
        python visualize_comparison.py --chart ${2:-all}
        ;;
    help)
        echo "Usage: ./run.sh [command]"
        echo ""
        echo "Commands:"
        echo "  install        Install package"
        echo "  install-dev    Install with development dependencies"
        echo "  test           Run tests"
        echo "  test-coverage  Run tests with coverage report"
        echo "  lint           Run linter"
        echo "  format         Format code with black"
        echo "  type-check     Type check with mypy"
        echo "  clean          Clean up cache and build files"
        echo "  benchmark      Run all algorithm benchmarks"
        echo "  benchmark-ffd  Run FFD benchmark (args: num_jobs num_qubits)"
        echo "  visualize      Generate all comparison charts from results"
        echo "  visualize-chart Generate specific chart (args: all|metrics|makespan|scatter|radar|gantt|report)"
        echo "  help           Show this help message"
        ;;
    *)
        echo "Unknown command: $1"
        echo "Run './run.sh help' for available commands"
        exit 1
        ;;
esac
