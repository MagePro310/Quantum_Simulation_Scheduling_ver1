"""
Configuration module for the Quantum Scheduling Pipeline.

This module contains configuration classes and constants used throughout
the quantum scheduling system.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class SimulationMode(Enum):
    """Enumeration for simulation execution modes."""
    SINGLE_THREADED = 'single_threaded'
    MULTI_THREADED = 'multi_threaded'


class SchedulingAlgorithm(Enum):
    """Enumeration for available scheduling algorithms."""
    FFD = 'FFD'  # First Fit Decreasing
    MILQ = 'MILQ'  # Mixed Integer Linear Programming for Quantum
    MTMC = 'MTMC'  # Multi-Threaded Monte Carlo
    NO_TADS = 'NoTaDS'  # No Task Decomposition Scheduling


@dataclass
class PipelineConfig:
    """Configuration class for the quantum scheduling pipeline."""
    
    # Job configuration
    num_qubits_per_job: int = 7
    num_jobs: int = 2
    
    # Backend configuration
    backend_names: List[str] = None
    
    # Scheduling configuration
    scheduling_algorithm: SchedulingAlgorithm = SchedulingAlgorithm.FFD
    
    # Simulation configuration
    simulation_mode: SimulationMode = SimulationMode.MULTI_THREADED
    shots: int = 1024
    
    # Cutting configuration
    enable_circuit_cutting: bool = True
    
    # Knitting configuration
    enable_circuit_knitting: bool = True
    
    # Output configuration
    experiment_id: str = "5_5"
    save_visualizations: bool = True
    save_intermediate_results: bool = False
    show_plots: bool = False
    gantt_chart_dir: str = "ganttCharts"
    
    # Logging configuration
    log_level: str = "INFO"
    
    def __post_init__(self):
        """Set default backend names if not provided."""
        if self.backend_names is None:
            self.backend_names = ["belem", "manila"]
    
    def validate(self) -> None:
        """Validate configuration parameters."""
        if self.num_qubits_per_job <= 0:
            raise ValueError("num_qubits_per_job must be positive")
        
        if self.num_jobs <= 0:
            raise ValueError("num_jobs must be positive")
        
        if self.shots <= 0:
            raise ValueError("shots must be positive")
        
        if not self.backend_names:
            raise ValueError("At least one backend must be specified")


@dataclass
class ExperimentConfig:
    """Configuration for running multiple experiments."""
    
    # Parameter sweeps
    qubit_ranges: List[int] = None
    job_ranges: List[int] = None
    algorithms: List[SchedulingAlgorithm] = None
    
    # Execution settings
    parallel_execution: bool = False
    max_workers: int = 4
    
    # Output settings
    base_experiment_id: str = "experiment"
    generate_comparison_plots: bool = True
    
    def __post_init__(self):
        """Set default values if not provided."""
        if self.qubit_ranges is None:
            self.qubit_ranges = [5, 7, 10]
        
        if self.job_ranges is None:
            self.job_ranges = [2, 5, 10]
        
        if self.algorithms is None:
            self.algorithms = [SchedulingAlgorithm.FFD]


# Default configurations
DEFAULT_PIPELINE_CONFIG = PipelineConfig()

DEFAULT_EXPERIMENT_CONFIG = ExperimentConfig()

# System constants
SUPPORTED_BACKENDS = [
    "belem", "manila", "quito", "lima", "bogota", 
    "santiago", "casablanca", "jakarta"
]

METRIC_NAMES = [
    "average_turnaround_time",
    "average_response_time", 
    "average_fidelity",
    "sampling_overhead",
    "average_throughput",
    "average_utilization",
    "scheduler_latency",
    "makespan"
]

# Output paths
RESULT_BASE_PATH = "component/finalResult"
SCHEDULING_RESULT_PATH = "component/d_scheduling/scheduleResult"
VISUALIZATION_PATH = "visualizations"
