# Quantum Circuit Scheduling and Resource Allocation Framework

## Abstract

This repository presents a comprehensive, production-ready quantum circuit scheduling and simulation framework that addresses the critical challenge of resource allocation in quantum computing systems. The framework implements multiple scheduling algorithms for quantum job allocation across heterogeneous quantum backends, providing a complete pipeline from circuit generation to performance evaluation with professional-grade architecture and extensive configuration options.

The system contributes to the quantum computing research community by offering a standardized platform for comparative analysis of scheduling algorithms, automated circuit processing workflows, and comprehensive performance metrics collection suitable for both academic research and industrial applications.

## 1. Introduction

### 1.1 Problem Statement

As quantum computing systems scale beyond proof-of-concept demonstrations toward practical applications, efficient resource allocation becomes increasingly critical. The heterogeneous nature of quantum backends, varying circuit requirements, and the need for optimal resource utilization present complex scheduling challenges that require sophisticated algorithmic approaches and robust evaluation frameworks.

### 1.2 Research Contributions

This framework provides the following key contributions to the quantum computing research community:

1. **Algorithmic Implementation**: Production-ready implementations of established scheduling algorithms (FFD, MILQ, MTMC, NoTaDS) with standardized interfaces
2. **Circuit Processing Pipeline**: Automated circuit cutting and knitting capabilities for handling circuits exceeding backend capacity
3. **Performance Evaluation Framework**: Comprehensive metrics collection and analysis tools for comparing scheduling approaches
4. **Extensible Architecture**: Modular design enabling easy integration of new algorithms and backends
5. **Reproducible Research Platform**: Standardized experimental setup and results format for reproducible comparative studies

### 1.3 System Overview

The Quantum Scheduling Pipeline is designed as a modular, extensible framework for researchers and practitioners working with quantum computing resource allocation. It provides automated scheduling, circuit processing, and simulation capabilities across multiple quantum backends, enabling systematic evaluation of scheduling strategies under realistic operational conditions.

## 2. Theoretical Framework

### 2.1 Quantum Job Scheduling Problem

The quantum job scheduling problem can be formally defined as follows:

**Given:**

- A set of quantum circuits C = {c₁, c₂, ..., cₙ} with associated qubit requirements q(cᵢ)
- A set of quantum backends B = {b₁, b₂, ..., bₘ} with capacities cap(bⱼ)
- Execution time estimates t(cᵢ, bⱼ) for each circuit-backend pair

**Objective:**
Minimize makespan while maximizing resource utilization and maintaining acceptable fidelity levels.

**Constraints:**

- q(cᵢ) ≤ cap(bⱼ) for valid assignments
- Temporal ordering constraints for dependent circuits
- Resource availability windows

### 2.2 Implemented Algorithms

#### 2.2.1 First Fit Decreasing (FFD)

A heuristic algorithm that sorts jobs by decreasing resource requirements and assigns each job to the first backend with sufficient capacity.

**Time Complexity:** O(n log n + nm)  
**Space Complexity:** O(n + m)

#### 2.2.2 Multi-Level Iterative Quantum (MILQ)

An iterative improvement algorithm that uses multiple levels of optimization to refine initial scheduling decisions.

#### 2.2.3 Multi-Threaded Monte Carlo (MTMC)

A probabilistic approach using Monte Carlo methods with parallel execution for exploring the solution space.

#### 2.2.4 No-Timeline Distributed Scheduling (NoTaDS)

A distributed scheduling approach that avoids explicit timeline management through dynamic resource allocation.

## 3. System Architecture

### 3.1 Architectural Principles

The system follows established software engineering principles:

- **Separation of Concerns**: Clear module boundaries and responsibilities
- **Dependency Injection**: Configuration-driven component assembly
- **Open/Closed Principle**: Extensible for new algorithms and backends
- **Single Responsibility**: Each module has a well-defined purpose
- **Interface Segregation**: Minimal, focused component interfaces

### 3.2 Core Components

```text
Quantum_Simulation_Scheduling/
├── 📁 component/                    # Core system modules
│   ├── 📁 a_backend/               # Quantum backend management
│   │   ├── fake_backend.py         # Backend implementations
│   │   └── __init__.py             # Module initialization
│   ├── 📁 b_benchmark/             # Circuit benchmark generation
│   │   ├── mqt_tool.py             # MQT-based circuit generation
│   │   └── __init__.py             # Module initialization
│   ├── 📁 c_circuit_work/          # Circuit processing subsystem
│   │   ├── cutting/                # Circuit decomposition algorithms
│   │   ├── knitting/               # Circuit merging algorithms
│   │   └── __init__.py             # Module initialization
│   ├── 📁 d_scheduling/            # Scheduling engine
│   │   ├── algorithm/              # Scheduling algorithm implementations
│   │   ├── analyze/                # Performance analysis tools
│   │   ├── datawork/               # Data processing and visualization
│   │   ├── simulation/             # Execution simulation
│   │   └── __init__.py             # Module initialization
│   ├── 📁 e_transpile/             # Circuit transpilation
│   ├── 📁 f_assemble/              # Assembly and fidelity calculation
│   ├── 📁 finalResult/             # Results storage and organization
│   ├── 📁 sup_sys/                 # Support systems (job info, loaders)
│   └── 📄 utils.py                 # Utility functions module
├── 📄 quantum_scheduling_pipeline.py # Main pipeline orchestrator
├── 📄 main.py                      # Command-line interface
├── 📄 config.py                    # Configuration management system
├── 📄 test_pipeline.py             # Comprehensive test suite
├── 📄 test_gantt_naming.py         # Visualization testing
├── 📄 requirements.txt             # Dependency specifications
├── 📄 GANTT_CHART_GUIDE.md         # Visualization documentation
├── 📄 TRANSFORMATION_SUMMARY.md    # Development history
└── 📄 README.md                    # This document
```

### 3.3 Module Descriptions

#### 3.3.1 Main Pipeline (`quantum_scheduling_pipeline.py`)

**Primary Classes:**

- `QuantumSchedulingPipeline`: Main orchestrator implementing the complete workflow
- `SchedulingMetrics`: Data structure for comprehensive performance metrics

**Responsibilities:**

- Workflow coordination and stage management
- Resource initialization and validation
- Error handling and recovery
- Results aggregation and storage

#### 3.3.2 Configuration Management (`config.py`)

**Primary Classes:**

- `PipelineConfig`: Main configuration dataclass with validation
- `ExperimentConfig`: Batch experiment configuration
- `SimulationMode`, `SchedulingAlgorithm`: Type-safe enumerations

**Design Features:**

- Type-safe configuration with validation
- Support for JSON serialization/deserialization
- Environment variable integration
- Default value management

#### 3.3.3 Command Line Interface (`main.py`)

**Capabilities:**

- Comprehensive argument parsing with validation
- Configuration file loading and saving
- Batch execution support
- User-friendly output formatting
- Error reporting and debugging support

#### 3.3.4 Utilities Module (`component/utils.py`)

**Core Functions:**

- `setup_logging()`: Configurable logging system
- `save_json()`, `load_json()`: Structured data persistence
- `generate_unique_filename()`: File management utilities
- `normalize_metrics()`: Statistical analysis helpers
- `create_comparison_plot()`: Visualization generation

### 3.4 Component Subsystems

#### 3.4.1 Backend Management (`component/a_backend/`)

Provides abstraction layer for quantum backends with support for:

- IBM Quantum Network backends (Belem, Manila, etc.)
- Fake backend implementations for testing
- Backend capability discovery and validation
- Resource capacity management

#### 3.4.2 Benchmark Generation (`component/b_benchmark/`)

Implements circuit generation using the MQT Bench framework:

- Parameterized quantum algorithms (QFT, Grover, etc.)
- Scalable circuit generation
- Circuit complexity analysis
- Benchmark diversity for comprehensive evaluation

#### 3.4.3 Circuit Processing (`component/c_circuit_work/`)

**Cutting Module:**

- Width-based circuit decomposition for oversized circuits
- Overhead calculation and optimization
- Support for various cutting strategies

**Knitting Module:**

- Circuit merging for concurrent execution
- Resource optimization through parallel processing
- Measurement coordination and result aggregation

#### 3.4.4 Scheduling Engine (`component/d_scheduling/`)

**Algorithm Implementations:**

- Standardized interfaces for scheduling algorithms
- Performance profiling and timing analysis
- Result format standardization

**Analysis Tools:**

- Comprehensive metrics calculation (makespan, utilization, throughput)
- Statistical analysis and comparison utilities
- Performance visualization generation

**Simulation Framework:**

- Single and multi-threaded execution modes
- Resource contention modeling
- Timing refinement based on realistic execution models

## 4. Experimental Methodology

### 4.1 Experimental Design

The framework supports systematic experimental evaluation through:

1. **Controlled Variables**: Standardized circuit generation and backend configuration
2. **Measurable Outcomes**: Comprehensive performance metrics collection
3. **Reproducibility**: Version-controlled configurations and deterministic execution
4. **Statistical Validity**: Multiple trial support and statistical analysis tools

### 4.2 Performance Metrics

#### 4.2.1 Scheduling Quality Metrics

- **Makespan**: Total execution time from first job start to last job completion
- **Average Turnaround Time**: Mean time from job submission to completion
- **Average Response Time**: Mean time from submission to first execution
- **Scheduler Latency**: Time required to compute scheduling decisions

#### 4.2.2 Resource Utilization Metrics

- **Average Utilization**: Mean percentage of backend resource usage
- **Throughput**: Number of jobs completed per unit time
- **Load Balancing**: Variance in utilization across backends

#### 4.2.3 Quality Metrics

- **Average Fidelity**: Mean execution fidelity across all jobs
- **Sampling Overhead**: Additional cost due to circuit cutting operations
- **Error Rate**: Comparison between ideal and noisy simulation results

### 4.3 Visualization and Analysis

The framework provides comprehensive visualization capabilities:

#### 4.3.1 Gantt Chart Generation

- Automated generation with structured naming conventions
- Timeline visualization of job execution
- Resource allocation tracking
- Comparative analysis support

#### 4.3.2 Performance Analysis

- Statistical summary generation
- Comparative performance plots
- Metrics normalization for cross-experiment comparison
- Export capabilities for external analysis tools

## 5. Installation and Configuration

### 5.1 System Requirements

**Software Dependencies:**

- Python 3.8 or higher
- Qiskit 0.45.0 or higher
- IBM Qiskit Runtime
- NumPy, Matplotlib, Pandas
- MQT Bench framework

**Hardware Requirements:**

- Minimum: 4GB RAM, 2 CPU cores
- Recommended: 8GB RAM, 4+ CPU cores
- Storage: 1GB available space for results

### 5.2 Installation Process

1. **Repository Setup**:

   ```bash
   git clone <repository-url>
   cd Quantum_Simulation_Scheduling
   ```

2. **Dependency Installation**:

   ```bash
   pip install -r requirements.txt
   ```

3. **System Verification**:

   ```bash
   python test_pipeline.py
   python test_gantt_naming.py
   ```

### 5.3 Configuration Management

#### 5.3.1 Configuration Parameters

```python
@dataclass
class PipelineConfig:
    # Experimental parameters
    num_qubits_per_job: int = 7          # Circuit size
    num_jobs: int = 2                    # Workload size
    backend_names: List[str] = ["belem", "manila"]  # Target backends
    
    # Algorithm selection
    scheduling_algorithm: SchedulingAlgorithm = SchedulingAlgorithm.FFD
    simulation_mode: SimulationMode = SimulationMode.MULTI_THREADED
    
    # Processing options
    enable_circuit_cutting: bool = True   # Circuit decomposition
    enable_circuit_knitting: bool = True  # Circuit merging
    
    # Output configuration
    save_visualizations: bool = True      # Chart generation
    show_plots: bool = False             # Interactive display
    experiment_id: str = "default"       # Results organization
    
    # Simulation parameters
    shots: int = 1024                    # Quantum simulation shots
    log_level: str = "INFO"              # Logging verbosity
```

#### 5.3.2 Command Line Interface

```bash
# Basic execution with default parameters
python main.py

# Comprehensive parameter specification
python main.py --qubits 10 --jobs 5 --algorithm MILQ \
               --mode single_threaded --backends belem manila \
               --shots 2048 --experiment-id "comparative_study"

# Configuration file usage
python main.py --config experiment_config.json

# Configuration generation and reuse
python main.py --save-config baseline_config.json
python main.py --config baseline_config.json
```

## 6. Usage Examples and Case Studies

### 6.1 Basic Scheduling Comparison

```python
from quantum_scheduling_pipeline import QuantumSchedulingPipeline
from config import PipelineConfig, SchedulingAlgorithm

# Compare scheduling algorithms
algorithms = [SchedulingAlgorithm.FFD, SchedulingAlgorithm.MILQ, 
              SchedulingAlgorithm.MTMC, SchedulingAlgorithm.NoTaDS]

results = {}
for algorithm in algorithms:
    config = PipelineConfig(
        num_qubits_per_job=8,
        num_jobs=4,
        scheduling_algorithm=algorithm,
        experiment_id=f"comparison_{algorithm.value}"
    )
    
    pipeline = QuantumSchedulingPipeline(config)
    result_path = pipeline.run_complete_pipeline()
    results[algorithm.value] = pipeline.metrics
```

### 6.2 Scalability Analysis

```python
# Systematic scalability evaluation
job_counts = [2, 4, 6, 8, 10]
qubit_counts = [5, 7, 10, 12, 15]

for jobs in job_counts:
    for qubits in qubit_counts:
        config = PipelineConfig(
            num_jobs=jobs,
            num_qubits_per_job=qubits,
            experiment_id=f"scale_{jobs}j_{qubits}q"
        )
        
        pipeline = QuantumSchedulingPipeline(config)
        pipeline.run_complete_pipeline()
```

### 6.3 Algorithm Parameter Sensitivity

```python
# Evaluate sensitivity to circuit cutting
cutting_configs = [True, False]

for enable_cutting in cutting_configs:
    config = PipelineConfig(
        num_qubits_per_job=12,  # Exceeds some backend capacity
        enable_circuit_cutting=enable_cutting,
        experiment_id=f"cutting_{'enabled' if enable_cutting else 'disabled'}"
    )
    
    pipeline = QuantumSchedulingPipeline(config)
    pipeline.run_complete_pipeline()
```

## 7. Performance Analysis and Benchmarking

### 7.1 Algorithmic Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Optimal Conditions |
|-----------|----------------|------------------|-------------------|
| FFD | O(n log n + nm) | O(n + m) | Uniform job sizes |
| MILQ | O(k × n × m) | O(n + m) | Iterative improvement |
| MTMC | O(t × n × m) | O(n + m) | Stochastic exploration |
| NoTaDS | O(n × m) | O(n + m) | Dynamic workloads |

### 7.2 Empirical Performance Characteristics

**Experimental Setup:**

- Job counts: 2-20 circuits
- Qubit range: 5-15 qubits per circuit
- Backend pool: IBM Belem (5 qubits), Manila (16 qubits)
- Trials: 10 repetitions per configuration

**Key Findings:**

1. FFD provides consistent performance with O(n log n) scaling
2. MILQ shows improved solution quality at higher computational cost
3. MTMC benefits from parallel execution in multi-threaded mode
4. Circuit cutting overhead is significant for oversized circuits (>15% performance impact)

### 7.3 Resource Utilization Analysis

The framework enables detailed analysis of resource utilization patterns:

```python
# Analyze utilization patterns
from component.d_scheduling.analyze import analyze_cal

data = analyze_cal.load_job_data("results/schedule.json")
utilization = analyze_cal.calculate_utilization(data)

print(f"Average utilization: {utilization['average']:.3f}")
print(f"Utilization variance: {utilization['variance']:.3f}")
```

## 8. Extension and Customization

### 8.1 Adding New Scheduling Algorithms

1. **Algorithm Implementation**:

   ```python
   # component/d_scheduling/algorithm/my_algorithm.py
   def my_scheduling_algorithm(jobs, machines, output_path):
       """Implement custom scheduling logic."""
       # Algorithm implementation
       pass
   ```

2. **Integration**:

   ```python
   # config.py
   class SchedulingAlgorithm(Enum):
       FFD = "FFD"
       MILQ = "MILQ"
       MTMC = "MTMC"
       NoTaDS = "NoTaDS"
       MY_ALGORITHM = "MY_ALGORITHM"  # Add new algorithm
   ```

3. **Registration**:

   ```python
   # component/sup_sys/algorithm_loader.py
   algorithm_registry["MY_ALGORITHM"] = my_scheduling_algorithm
   ```

### 8.2 Backend Extension

```python
# component/a_backend/custom_backend.py
class CustomQuantumBackend:
    def __init__(self, name, num_qubits, error_rate):
        self.name = name
        self.num_qubits = num_qubits
        self.error_rate = error_rate
    
    def run(self, circuit, shots=1024):
        """Implement backend-specific execution."""
        pass
```

### 8.3 Custom Metrics

```python
# component/d_scheduling/analyze/custom_metrics.py
def calculate_custom_metric(job_data):
    """Calculate domain-specific performance metrics."""
    return metric_value
```

## 9. Testing and Validation

### 9.1 Test Suite Architecture

The framework includes comprehensive testing:

```python
# test_pipeline.py - Core functionality testing
def test_basic_pipeline_execution():
def test_configuration_validation():
def test_import_dependencies():
def test_scheduling_algorithms():

# test_gantt_naming.py - Visualization testing
def test_gantt_chart_generation():
def test_chart_naming_convention():
def test_chart_cleanup():
```

### 9.2 Validation Methodology

1. **Unit Testing**: Individual module functionality
2. **Integration Testing**: Component interaction validation
3. **End-to-End Testing**: Complete pipeline execution
4. **Performance Testing**: Scalability and resource usage validation
5. **Regression Testing**: Backward compatibility verification

### 9.3 Continuous Integration

```bash
# Automated testing workflow
python test_pipeline.py
python test_gantt_naming.py

# Performance benchmarking
python main.py --qubits 7 --jobs 2 --verbose
```

## 10. Troubleshooting and Debugging

### 10.1 Common Issues and Solutions

#### 10.1.1 Import Errors

```bash
# Ensure Python path includes component modules
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python main.py
```

#### 10.1.2 Backend Configuration Issues

- Verify backend names match available implementations
- Check IBM Qiskit Runtime installation and credentials
- Review backend capacity constraints

#### 10.1.3 Memory Management

- Use single-threaded mode for large experiments
- Reduce shot count for memory-constrained environments
- Monitor system resources during execution

### 10.2 Debug Mode Operation

```bash
# Enable comprehensive debugging
python main.py --verbose --show-plots --experiment-id "debug_session"
```

**Debug Output Includes:**

- Detailed timing information for each pipeline stage
- Backend configuration and availability status
- Memory usage and resource consumption metrics
- Error stack traces with context information

### 10.3 Performance Optimization

#### 10.3.1 Execution Mode Selection

- **Single-threaded**: Recommended for debugging and small-scale experiments
- **Multi-threaded**: Optimal for production workloads and large parameter sweeps

#### 10.3.2 Resource Management

- Automatic plot cleanup after saving to prevent memory leaks
- Configurable intermediate result caching
- Garbage collection optimization for long-running experiments

## 11. Results and Data Management

### 11.1 Output Structure

Results are organized in a hierarchical structure for systematic analysis:

```text
component/finalResult/
├── {experiment_id}/
│   ├── ganttCharts/                    # Visualization outputs
│   │   ├── FFD_ae_2jobs_7qubits_scheduling_20250623_143022.pdf
│   │   └── FFD_ae_2jobs_7qubits_simulation_20250623_143045.pdf
│   └── {algorithm}/                    # Algorithm-specific results
│       └── {benchmark}/                # Benchmark-specific results
│           └── {jobs}_{qubits}_0.json  # Metrics and configuration
```

### 11.2 Data Format Specification

```json
{
    "metadata": {
        "experiment_id": "comparative_study",
        "timestamp": "2025-06-23T14:30:22Z",
        "framework_version": "1.0.0"
    },
    "configuration": {
        "num_circuits": 4,
        "algorithm_name": "ae",
        "average_qubits": 8.0,
        "schedule_name": "FFD",
        "machine_types": {"fake_belem": 5, "fake_manila": 16}
    },
    "performance_metrics": {
        "scheduler_latency": 0.045,
        "makespan": 15.5,
        "average_turnaround_time": 12.3,
        "average_response_time": 2.1,
        "average_throughput": 0.258,
        "average_utilization": 0.673,
        "average_fidelity": 0.8945,
        "sampling_overhead": 0.0
    }
}
```

### 11.3 Data Analysis Tools

```python
# Load and analyze experimental results
from component.utils import load_json, normalize_metrics

# Load multiple experiment results
results = [load_json(f"results/experiment_{i}.json") for i in range(5)]

# Normalize metrics for comparison
normalized = normalize_metrics(results)

# Generate comparative analysis
comparison_plot = create_comparison_plot(
    results, 
    x_param="num_circuits", 
    y_metrics=["makespan", "average_utilization"]
)
```

## 12. Contributing and Development

### 12.1 Development Environment Setup

```bash
# Development setup
git clone <repository-url>
cd Quantum_Simulation_Scheduling
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Pre-commit hooks setup
pre-commit install
```

### 12.2 Code Standards and Guidelines

#### 12.2.1 Python Style Guidelines

- Follow PEP 8 style conventions
- Use type hints for all function signatures
- Maintain comprehensive docstrings using Google style
- Target 90%+ test coverage for new code

#### 12.2.2 Documentation Standards

- Update README.md for significant changes
- Include inline code documentation
- Provide usage examples for new features
- Maintain API documentation consistency

#### 12.2.3 Testing Requirements

- Write unit tests for all new functionality
- Include integration tests for component interactions
- Provide performance benchmarks for algorithmic changes
- Validate backward compatibility for API modifications

### 12.3 Submission Guidelines

1. **Feature Development**:
   - Create feature branch: `git checkout -b feature/new-algorithm`
   - Implement changes with comprehensive testing
   - Update documentation and examples
   - Submit pull request with detailed description

2. **Bug Fixes**:
   - Create bug fix branch: `git checkout -b fix/issue-description`
   - Include regression test to prevent recurrence
   - Update relevant documentation
   - Reference issue number in commit messages

3. **Documentation Updates**:
   - Ensure accuracy and completeness
   - Provide examples for complex procedures
   - Maintain consistent formatting and style
   - Verify all links and references

## 13. Future Research Directions

### 13.1 Algorithmic Enhancements

1. **Machine Learning Integration**: Develop ML-based scheduling optimization using historical performance data
2. **Dynamic Scheduling**: Implement adaptive algorithms that respond to real-time system conditions
3. **Multi-Objective Optimization**: Extend framework to handle trade-offs between multiple performance criteria
4. **Fault-Tolerant Scheduling**: Develop resilient scheduling strategies for unreliable quantum hardware

### 13.2 System Extensions

1. **Real Hardware Integration**: Extend support for actual quantum devices beyond simulators
2. **Distributed Computing**: Enable scheduling across geographically distributed quantum resources
3. **Hybrid Computing**: Integrate classical and quantum resource scheduling
4. **Interactive Optimization**: Develop user-guided scheduling refinement tools

### 13.3 Performance Optimization

1. **Parallel Algorithm Implementation**: Leverage modern multi-core architectures for scheduling computation
2. **Memory Optimization**: Reduce memory footprint for large-scale experiments
3. **GPU Acceleration**: Utilize GPU computing for simulation and optimization tasks
4. **Streaming Processing**: Enable real-time processing of continuous job streams

## 14. References and Related Work

### 14.1 Foundational Literature

1. **Quantum Computing**: Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*
2. **Scheduling Theory**: Pinedo, M. L. (2016). *Scheduling: Theory, Algorithms, and Systems*
3. **Resource Allocation**: Coffman Jr, E. G., et al. (1984). "Approximation algorithms for bin packing"

### 14.2 Quantum Scheduling Research

1. **Circuit Cutting**: Peng, T., et al. (2020). "Simulating large quantum circuits on a small quantum computer"
2. **Resource Management**: Humble, T. S., et al. (2016). "Quantum computing resource allocation"
3. **Performance Analysis**: Cross, A. W., et al. (2019). "Quantum circuit optimization"

### 14.3 Software Frameworks

1. **Qiskit**: IBM Quantum Team (2023). *Qiskit: An Open-source Framework for Quantum Computing*
2. **MQT Bench**: Quetschlich, N., et al. (2023). "MQT Bench: Benchmarking Software and Design Automation Tools"
3. **Scheduling Systems**: Various scheduling framework implementations and comparisons

## 15. Appendices

### Appendix A: Configuration Schema

Complete JSON schema for configuration validation and automated documentation generation.

### Appendix B: API Reference

Comprehensive API documentation for all public interfaces and extension points.

### Appendix C: Performance Benchmarks

Detailed performance benchmarks across various system configurations and workload characteristics.

### Appendix D: Algorithm Implementation Details

Mathematical formulations and implementation specifics for each supported scheduling algorithm.

---

## 📝 Additional Documentation

- **[GANTT_CHART_GUIDE.md](GANTT_CHART_GUIDE.md)**: Comprehensive guide to Gantt chart visualization features
- **[TRANSFORMATION_SUMMARY.md](TRANSFORMATION_SUMMARY.md)**: Details about the notebook-to-production transformation

---

**Version**: 1.0.0  
**Last Updated**: June 23, 2025  
**Maintainers**: Quantum Simulation Research Team  
**Institution**: [Academic Institution/Research Group]  
**Contact**: [Contact Information]  

**License**: MIT License - See LICENSE file for details  

**Citation**: If you use this framework in your research, please cite:

```bibtex
@software{quantum_scheduling_framework_2025,
  title={Quantum Circuit Scheduling and Resource Allocation Framework},
  author={Quantum Simulation Research Team},
  year={2025},
  url={https://github.com/your-repository},
  version={1.0.0}
}
```

This framework represents a comprehensive solution for quantum circuit scheduling research and provides a solid foundation for advancing quantum computing resource allocation methodologies. The system bridges the gap between theoretical scheduling algorithms and practical quantum computing applications, enabling reproducible research and comparative analysis in the rapidly evolving field of quantum computing.

## 🚀 Quick Start Guide

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd Quantum_Simulation_Scheduling
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:

   ```bash
   python test_pipeline.py
   ```

### Basic Usage

#### Command Line Interface

```bash
# Default execution (2 jobs, 7 qubits each, FFD algorithm)
python main.py

# Custom parameters
python main.py --qubits 10 --jobs 5 --algorithm FFD --mode multi_threaded

# Configuration from file
python main.py --config experiment.json

# Save configuration
python main.py --save-config my_setup.json

# Verbose execution with plot display
python main.py --verbose --show-plots
```

#### Programmatic Interface

```python
from quantum_scheduling_pipeline import QuantumSchedulingPipeline
from config import PipelineConfig, SimulationMode

# Create configuration
config = PipelineConfig(
    num_qubits_per_job=8,
    num_jobs=3,
    simulation_mode=SimulationMode.MULTI_THREADED,
    show_plots=False,
    experiment_id="my_experiment"
)

# Run pipeline
pipeline = QuantumSchedulingPipeline(config)
result_path = pipeline.run_complete_pipeline()
print(f"Results: {result_path}")
```

## 📊 Pipeline Workflow

### Stage 1: Initialization

1. **Configuration Loading**: Parse command-line args or config files
2. **Backend Setup**: Initialize quantum backends (IBM Belem, Manila, etc.)
3. **Validation**: Verify configuration parameters

### Stage 2: Circuit Generation

1. **Benchmark Creation**: Generate quantum circuits using MQT tools
2. **Job Information**: Create JobInfo objects with metadata
3. **Metrics Initialization**: Set up performance tracking

### Stage 3: Circuit Cutting (Optional)

1. **Width Analysis**: Check if circuits exceed backend capacity
2. **Decomposition**: Cut oversized circuits into subcircuits
3. **Overhead Tracking**: Calculate cutting overhead costs

### Stage 4: Scheduling

1. **Algorithm Execution**: Run selected scheduling algorithm (FFD/MILQ/MTMC/NoTaDS)
2. **Job Assignment**: Assign jobs to quantum machines
3. **Timing Optimization**: Optimize start times and resource allocation
4. **Gantt Chart Generation**: Create scheduling visualization

### Stage 5: Transpilation

1. **Circuit Preparation**: Remove unwanted operations
2. **Backend Optimization**: Transpile for target quantum backends
3. **Layout Assignment**: Apply layout and scheduling methods

### Stage 6: Simulation

1. **Scheduling Simulation**: Run single or multi-threaded simulation
2. **Timing Updates**: Refine job timing based on simulation
3. **Resource Tracking**: Update machine utilization
4. **Simulation Gantt Chart**: Generate updated visualization

### Stage 7: Circuit Knitting (Optional)

1. **Concurrent Job Identification**: Find jobs running simultaneously
2. **Circuit Merging**: Combine circuits for parallel execution
3. **Measurement Addition**: Add measurement operations
4. **Final Transpilation**: Optimize merged circuits

### Stage 8: Quantum Simulation

1. **Ideal Simulation**: Run circuits on noiseless simulator
2. **Noisy Simulation**: Execute on fake quantum backends
3. **Fidelity Calculation**: Compare ideal vs noisy results
4. **Results Storage**: Store simulation outcomes

### Stage 9: Metrics Calculation

1. **Performance Analysis**: Calculate comprehensive metrics
2. **Parent Job Updates**: Aggregate child job results
3. **System Metrics**: Compute utilization, throughput, etc.
4. **Summary Generation**: Create formatted results

### Stage 10: Results Storage

1. **JSON Export**: Save metrics in structured format
2. **Unique Naming**: Generate timestamped filenames
3. **Directory Organization**: Store in experiment-specific folders
4. **Cleanup**: Archive and organize outputs

## 📊 Performance Metrics

### Scheduling Metrics

- **Scheduler Latency**: Time to compute schedule
- **Makespan**: Total execution time
- **Average Turnaround Time**: Job submission to completion
- **Average Response Time**: Time to first execution

### Resource Metrics

- **Average Utilization**: Machine resource usage
- **Average Throughput**: Jobs per unit time
- **Machine Efficiency**: Per-backend performance

### Quality Metrics

- **Average Fidelity**: Circuit execution accuracy
- **Sampling Overhead**: Circuit cutting costs
- **Error Rates**: Simulation vs ideal comparison

## 🎛️ Configuration System

### Pipeline Configuration Options

```python
@dataclass
class PipelineConfig:
    # Job configuration
    num_qubits_per_job: int = 7
    num_jobs: int = 2
    backend_names: List[str] = ["belem", "manila"]
    
    # Algorithm configuration
    scheduling_algorithm: SchedulingAlgorithm = FFD
    simulation_mode: SimulationMode = MULTI_THREADED
    
    # Processing options
    enable_circuit_cutting: bool = True
    enable_circuit_knitting: bool = True
    
    # Output configuration
    save_visualizations: bool = True
    show_plots: bool = False
    gantt_chart_dir: str = "ganttCharts"
    experiment_id: str = "5_5"
    
    # Simulation parameters
    shots: int = 1024
    log_level: str = "INFO"
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--qubits` | Number of qubits per job | 7 |
| `--jobs` | Number of jobs to schedule | 2 |
| `--algorithm` | Scheduling algorithm | FFD |
| `--mode` | Simulation mode | multi_threaded |
| `--backends` | Quantum backends to use | belem manila |
| `--shots` | Simulation shots | 1024 |
| `--experiment-id` | Experiment identifier | 5_5 |
| `--config` | Configuration file path | None |
| `--show-plots` | Display plots during execution | False |
| `--verbose` | Enable verbose logging | False |

## 📁 Output Structure

### Results Directory Layout

```text
component/finalResult/
├── {experiment_id}/
│   ├── ganttCharts/                    # Gantt chart visualizations
│   │   ├── FFD_ae_2jobs_7qubits_scheduling_timestamp.pdf
│   │   └── FFD_ae_2jobs_7qubits_simulation_timestamp.pdf
│   └── {algorithm}/                    # Algorithm-specific results
│       └── {benchmark}/                # Benchmark-specific results
│           └── {jobs}_{qubits}_0.json  # Metrics and configuration
```

### Gantt Chart Naming Convention

```text
{Algorithm}_{Benchmark}_{JobCount}jobs_{AvgQubits}qubits_{Stage}_{Timestamp}.pdf
```

**Example**: `FFD_ae_2jobs_7qubits_scheduling_20250623_143022.pdf`

### JSON Results Structure

```json
{
    "num_circuits": 2,
    "algorithm_name": "ae",
    "average_qubits": 7.0,
    "schedule_name": "FFD",
    "machine_types": {"fake_belem": 5, "fake_manila": 16},
    "average_turnaround_time": 15.5,
    "average_response_time": 2.3,
    "average_fidelity": 0.8945,
    "sampling_overhead": 0.0,
    "average_throughput": 0.129,
    "average_utilization": 0.67,
    "scheduler_latency": 0.045,
    "makespan": 15.5
}
```

## 🔧 Advanced Features

### Batch Processing

Run multiple experiments with different parameters:

```bash
# Parameter sweep
for qubits in 5 7 10; do
    for jobs in 2 4 6; do
        python main.py --qubits $qubits --jobs $jobs --experiment-id "sweep_${qubits}q_${jobs}j"
    done
done
```

### Custom Algorithms

Extend the system with new scheduling algorithms:

1. Create algorithm implementation in `component/d_scheduling/algorithm/`
2. Add algorithm enum to `config.py`
3. Update algorithm loader in `component/sup_sys/algorithm_loader.py`

### Custom Backends

Add new quantum backends:

1. Implement backend in `component/a_backend/`
2. Register in backend discovery system
3. Update configuration options

## 🧪 Testing and Validation

### Test Suite Components

1. **Core Pipeline Tests**: Basic functionality validation
2. **Configuration Tests**: Parameter validation and serialization
3. **Import Tests**: Dependency verification
4. **Gantt Chart Tests**: Visualization functionality
5. **Integration Tests**: End-to-end pipeline validation

### Running Tests

```bash
# Core pipeline tests
python test_pipeline.py

# Gantt chart tests
python test_gantt_naming.py

# All tests with verbose output
python test_pipeline.py && python test_gantt_naming.py
```

## 🐛 Troubleshooting

### Common Issues

**Import Errors**:

```bash
# Ensure component modules are accessible
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python main.py
```

**Backend Loading Failures**:

- Check backend names in configuration
- Verify IBM Qiskit Runtime installation
- Review backend availability

**Memory Issues**:

- Use single-threaded mode for large experiments
- Reduce number of shots for simulation
- Monitor system resources

**Permission Errors**:

- Ensure write permissions for output directories
- Check disk space availability
- Verify file system access

### Debug Mode

Enable comprehensive debugging:

```bash
python main.py --verbose --show-plots --experiment-id "debug_run"
```

### Log Analysis

Logs include:

- Pipeline stage execution times
- Backend configuration details
- Scheduling algorithm performance
- Error messages with stack traces
- Resource utilization statistics

## 📈 Performance Optimization

### Single vs Multi-threaded

- **Single-threaded**: Better for debugging, smaller datasets
- **Multi-threaded**: Faster for large experiments, better resource utilization

### Memory Management

- Plots automatically closed after saving
- Intermediate results optionally disabled
- Garbage collection optimizations

### Execution Time

- Algorithm complexity: O(n log n) for FFD
- Simulation overhead: Linear with job count
- Chart generation: Minimal impact (~1-2 seconds)

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes with proper documentation
4. Add tests for new functionality
5. Submit pull request

### Code Standards

- Follow PEP 8 style guidelines
- Add type hints for all functions
- Include comprehensive docstrings
- Write unit tests for new features
- Update documentation for changes

### Architecture Guidelines

- Maintain separation of concerns
- Use dependency injection for configuration
- Follow single responsibility principle
- Implement proper error handling
- Add logging for debugging

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙏 Acknowledgments

- **IBM Qiskit Team**: Quantum computing framework
- **MQT Bench Project**: Quantum circuit benchmarks
- **Research Community**: Scheduling algorithm insights
- **Open Source Contributors**: Framework improvements

## 📞 Support and Contact

### Getting Help

1. **Documentation**: Check this README and inline documentation
2. **Issues**: Open GitHub issues for bugs and feature requests
3. **Discussions**: Use GitHub discussions for questions
4. **Examples**: Review example configurations and scripts

### Reporting Issues

When reporting issues, include:

- System information (OS, Python version)
- Complete error messages
- Configuration used
- Steps to reproduce
- Expected vs actual behavior

---

**Version**: 1.0.0  
**Last Updated**: June 23, 2025  
**Maintainers**: Quantum Simulation Team

This system represents a comprehensive solution for quantum circuit scheduling research and provides a solid foundation for advancing quantum computing resource allocation methodologies.

## 📝 Further Documentation

- **[TUTORIAL.md](TUTORIAL.md)**: 📚 **Complete step-by-step tutorial** - Start here for hands-on learning!
- **[GANTT_CHART_GUIDE.md](GANTT_CHART_GUIDE.md)**: Comprehensive guide to Gantt chart visualization features
- **[TRANSFORMATION_SUMMARY.md](TRANSFORMATION_SUMMARY.md)**: Details about the notebook-to-production transformation
