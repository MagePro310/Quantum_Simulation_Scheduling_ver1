"""
Utility functions for the Quantum Scheduling Pipeline.

This module contains helper functions and utilities used across
the quantum scheduling system.
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import asdict
import matplotlib.pyplot as plt
import numpy as np

from config import METRIC_NAMES


def setup_logging(level: str = "INFO") -> logging.Logger:
    """
    Set up logging configuration.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        Configured logger instance
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('quantum_scheduling.log')
        ]
    )
    return logging.getLogger(__name__)


def ensure_directory(path: str) -> None:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        path: Directory path to create
    """
    os.makedirs(path, exist_ok=True)


def save_json(data: Any, filepath: str, indent: int = 4) -> None:
    """
    Save data to JSON file with proper formatting.
    
    Args:
        data: Data to save (must be JSON serializable)
        filepath: Output file path
        indent: JSON indentation level
    """
    ensure_directory(os.path.dirname(filepath))
    
    # Convert dataclasses to dict if needed
    if hasattr(data, '__dataclass_fields__'):
        data = asdict(data)
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)


def load_json(filepath: str) -> Any:
    """
    Load data from JSON file.
    
    Args:
        filepath: Input file path
        
    Returns:
        Loaded data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file is not valid JSON
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def generate_unique_filename(base_path: str, base_name: str, extension: str = ".json") -> str:
    """
    Generate a unique filename by appending a counter if file exists.
    
    Args:
        base_path: Directory path
        base_name: Base filename without extension
        extension: File extension
        
    Returns:
        Unique filename with full path
    """
    ensure_directory(base_path)
    
    existing_files = os.listdir(base_path)
    matching_files = [
        f for f in existing_files 
        if f.startswith(base_name) and f.endswith(extension)
    ]
    
    if not matching_files:
        return os.path.join(base_path, f"{base_name}_0{extension}")
    
    # Extract suffixes and find next available number
    suffixes = []
    for f in matching_files:
        suffix_str = f.replace(base_name, "").replace(extension, "").replace("_", "")
        if suffix_str.isdigit():
            suffixes.append(int(suffix_str))
    
    next_suffix = max(suffixes, default=0) + 1
    return os.path.join(base_path, f"{base_name}_{next_suffix}{extension}")


def format_metrics_table(metrics: Dict[str, float], title: str = "Metrics Summary") -> str:
    """
    Format metrics into a readable table string.
    
    Args:
        metrics: Dictionary of metric names to values
        title: Table title
        
    Returns:
        Formatted table string
    """
    lines = []
    lines.append("=" * 60)
    lines.append(f"{title:^60}")
    lines.append("=" * 60)
    
    for key, value in metrics.items():
        if isinstance(value, float):
            lines.append(f"{key:<35}: {value:>12.4f}")
        else:
            lines.append(f"{key:<35}: {value:>12}")
    
    lines.append("=" * 60)
    return "\n".join(lines)


def calculate_percentage_improvement(baseline: float, new_value: float) -> float:
    """
    Calculate percentage improvement between two values.
    
    Args:
        baseline: Baseline value
        new_value: New value to compare
        
    Returns:
        Percentage improvement (positive means improvement)
    """
    if baseline == 0:
        return 0.0
    return ((baseline - new_value) / baseline) * 100


def normalize_metrics(metrics_list: List[Dict[str, float]], 
                     metric_names: Optional[List[str]] = None) -> List[Dict[str, float]]:
    """
    Normalize metrics across multiple experiments for comparison.
    
    Args:
        metrics_list: List of metric dictionaries
        metric_names: Specific metrics to normalize (default: all)
        
    Returns:
        List of normalized metric dictionaries
    """
    if not metrics_list:
        return []
    
    if metric_names is None:
        metric_names = METRIC_NAMES
    
    # Find min/max for each metric
    min_values = {}
    max_values = {}
    
    for metric in metric_names:
        values = [m.get(metric, 0) for m in metrics_list if metric in m]
        if values:
            min_values[metric] = min(values)
            max_values[metric] = max(values)
    
    # Normalize each metric
    normalized_list = []
    for metrics in metrics_list:
        normalized = {}
        for metric in metric_names:
            if metric in metrics and metric in min_values:
                min_val = min_values[metric]
                max_val = max_values[metric]
                if max_val > min_val:
                    normalized[metric] = (metrics[metric] - min_val) / (max_val - min_val)
                else:
                    normalized[metric] = 0.0
        normalized_list.append(normalized)
    
    return normalized_list


def create_comparison_plot(results: List[Dict], 
                          x_param: str, 
                          y_metrics: List[str],
                          title: str = "Performance Comparison",
                          save_path: Optional[str] = None) -> plt.Figure:
    """
    Create a comparison plot for multiple metrics.
    
    Args:
        results: List of result dictionaries
        x_param: Parameter name for x-axis
        y_metrics: List of metric names for y-axis
        title: Plot title
        save_path: Optional path to save the plot
        
    Returns:
        matplotlib Figure object
    """
    fig, axes = plt.subplots(len(y_metrics), 1, figsize=(10, 6 * len(y_metrics)))
    if len(y_metrics) == 1:
        axes = [axes]
    
    for i, metric in enumerate(y_metrics):
        x_values = [r.get(x_param, 0) for r in results]
        y_values = [r.get(metric, 0) for r in results]
        
        axes[i].plot(x_values, y_values, 'o-', linewidth=2, markersize=8)
        axes[i].set_xlabel(x_param.replace('_', ' ').title())
        axes[i].set_ylabel(metric.replace('_', ' ').title())
        axes[i].grid(True, alpha=0.3)
        axes[i].set_title(f"{metric.replace('_', ' ').title()} vs {x_param.replace('_', ' ').title()}")
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    
    if save_path:
        ensure_directory(os.path.dirname(save_path))
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def validate_job_info(job_info: Any) -> bool:
    """
    Validate that job_info object has required attributes.
    
    Args:
        job_info: Job information object to validate
        
    Returns:
        True if valid, False otherwise
    """
    required_attrs = [
        'job_name', 'qubits', 'machine', 'start_time', 
        'duration', 'end_time', 'circuit'
    ]
    
    for attr in required_attrs:
        if not hasattr(job_info, attr):
            return False
    
    return True


def calculate_circuit_complexity(circuit) -> Dict[str, int]:
    """
    Calculate complexity metrics for a quantum circuit.
    
    Args:
        circuit: Qiskit QuantumCircuit object
        
    Returns:
        Dictionary with complexity metrics
    """
    if circuit is None:
        return {'depth': 0, 'gate_count': 0, 'qubit_count': 0}
    
    gate_count = len(circuit.data)
    gate_types = {}
    
    for instruction in circuit.data:
        gate_name = instruction.operation.name
        gate_types[gate_name] = gate_types.get(gate_name, 0) + 1
    
    return {
        'depth': circuit.depth(),
        'gate_count': gate_count,
        'qubit_count': circuit.num_qubits,
        'gate_types': gate_types
    }


def estimate_execution_time(circuit, backend) -> float:
    """
    Estimate execution time for a circuit on a given backend.
    
    Args:
        circuit: Qiskit QuantumCircuit object
        backend: Quantum backend
        
    Returns:
        Estimated execution time in seconds
    """
    if circuit is None or backend is None:
        return 0.0
    
    # Simple estimation based on circuit depth and backend properties
    base_time = 0.1  # Base execution time in seconds
    depth_factor = circuit.depth() * 0.01  # Time per depth level
    gate_factor = len(circuit.data) * 0.001  # Time per gate
    
    return base_time + depth_factor + gate_factor


def print_pipeline_summary(config: Any, results: Dict[str, Any]) -> None:
    """
    Print a comprehensive summary of pipeline execution.
    
    Args:
        config: Pipeline configuration
        results: Execution results
    """
    print("\n" + "="*80)
    print("QUANTUM SCHEDULING PIPELINE SUMMARY".center(80))
    print("="*80)
    
    print(f"Configuration:")
    print(f"  Jobs: {config.num_jobs}")
    print(f"  Qubits per job: {config.num_qubits_per_job}")
    print(f"  Scheduling algorithm: {config.scheduling_algorithm.value}")
    print(f"  Simulation mode: {config.simulation_mode.value}")
    print(f"  Backends: {', '.join(config.backend_names)}")
    
    print(f"\nResults:")
    for key, value in results.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    
    print("="*80)
