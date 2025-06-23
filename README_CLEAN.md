# Quantum Scheduling Pipeline

A comprehensive, production-ready quantum circuit scheduling and simulation framework implementing the First Fit Decreasing (FFD) algorithm for quantum job scheduling across multiple quantum backends.

## 🚀 Features

- **Professional Architecture**: Clean, modular, and well-documented codebase
- **Multiple Scheduling Algorithms**: Support for FFD, MILQ, MTMC, and NoTaDS algorithms
- **Circuit Processing**: Automated circuit cutting and knitting for large quantum jobs
- **Performance Evaluation**: Comprehensive metrics calculation and analysis
- **Flexible Configuration**: Command-line interface and configuration file support
- **Robust Simulation**: Both single-threaded and multi-threaded execution modes
- **Visualization**: Automated generation of scheduling visualizations
- **Results Management**: Structured output with unique naming and JSON storage

## 📁 Project Structure

```text
quantum_scheduling_pipeline.py  # Main pipeline implementation
main.py                        # Command-line interface
config.py                      # Configuration classes and constants
utils.py                       # Utility functions and helpers
README.md                      # This documentation
requirements.txt               # Python dependencies
```

## 🛠️ Installation

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
   python main.py --help
   ```

## 📋 Requirements

- Python 3.8+
- Qiskit 0.45+
- Qiskit Aer
- Qiskit IBM Runtime
- NumPy
- Matplotlib
- Other dependencies listed in `requirements.txt`

## 🎯 Quick Start

### Basic Usage

Run with default settings (2 jobs, 7 qubits each, FFD algorithm):

```bash
python main.py
```

### Custom Parameters

```bash
# Run with custom job configuration
python main.py --qubits 10 --jobs 5 --algorithm FFD --mode multi_threaded

# Use specific backends
python main.py --backends belem manila quito --shots 2048

# Single-threaded execution with verbose output
python main.py --mode single_threaded --verbose
```

### Configuration Files

Create a configuration file:

```bash
python main.py --save-config my_config.json
```

Run with configuration file:

```bash
python main.py --config my_config.json
```

## 📊 Pipeline Stages

### 1. Backend Setup

- Initializes quantum backends (default: IBM Belem and Manila)
- Configures machine capacities and properties

### 2. Circuit Generation

- Creates benchmark quantum circuits using MQT tools
- Generates job information structures

### 3. Circuit Cutting

- Automatically cuts circuits that exceed backend capacity
- Implements width-based cutting with overhead tracking

### 4. Scheduling

- Executes FFD scheduling algorithm
- Assigns jobs to machines with timing optimization

### 5. Transpilation

- Transpiles circuits for target backends
- Optimizes for ALAP scheduling and trivial layout

### 6. Simulation

- Runs scheduling simulation (single or multi-threaded)
- Updates job timing and resource allocation

### 7. Circuit Knitting

- Merges circuits running simultaneously on same machine
- Handles concurrent execution optimization

### 8. Quantum Simulation

- Executes circuits on simulated backends
- Calculates fidelity between ideal and noisy simulations

### 9. Metrics Calculation

- Computes comprehensive performance metrics
- Generates detailed analysis reports

### 10. Results Storage

- Saves results in structured JSON format
- Generates unique filenames to prevent overwrites

## 📈 Metrics

The pipeline calculates the following performance metrics:

- **Scheduler Latency**: Time taken to compute the schedule
- **Makespan**: Total time to complete all jobs
- **Average Turnaround Time**: Average time from job submission to completion
- **Average Response Time**: Average time to first execution
- **Average Throughput**: Jobs completed per unit time
- **Average Utilization**: Resource utilization across all machines
- **Average Fidelity**: Circuit execution fidelity
- **Sampling Overhead**: Additional overhead from circuit cutting

## ⚙️ Configuration Options

### Pipeline Configuration

```python
@dataclass
class PipelineConfig:
    num_qubits_per_job: int = 7        # Qubits per job
    num_jobs: int = 2                  # Number of jobs
    backend_names: List[str] = None    # Quantum backends
    scheduling_algorithm: SchedulingAlgorithm = FFD
    simulation_mode: SimulationMode = MULTI_THREADED
    shots: int = 1024                  # Quantum simulation shots
    enable_circuit_cutting: bool = True
    enable_circuit_knitting: bool = True
    experiment_id: str = "5_5"
    save_visualizations: bool = True
    log_level: str = "INFO"
```

### Command Line Options

```text
--qubits, -q       Number of qubits per job (default: 7)
--jobs, -j         Number of jobs to schedule (default: 2)
--algorithm, -a    Scheduling algorithm [FFD, MILQ, MTMC, NoTaDS]
--mode, -m         Simulation mode [single_threaded, multi_threaded]
--backends, -b     Quantum backends to use
--shots, -s        Number of shots for simulation (default: 1024)
--experiment-id    Experiment identifier
--config, -c       Load configuration from JSON file
--verbose, -v      Enable verbose logging
--quiet            Suppress output except errors
```

## 📂 Output Structure

Results are saved in a structured directory hierarchy:

```text
component/finalResult/
├── {experiment_id}/
│   ├── {algorithm}/
│   │   ├── {benchmark}/
│   │   │   ├── {num_circuits}_{avg_qubits}_0.json
│   │   │   ├── {num_circuits}_{avg_qubits}_1.json
│   │   │   └── ...
```

Each result file contains:

- Job configuration parameters
- Machine specifications
- Complete performance metrics
- Execution metadata

## 🔬 Advanced Usage

### Programmatic Interface

```python
from quantum_scheduling_pipeline import QuantumSchedulingPipeline
from config import PipelineConfig, SimulationMode, SchedulingAlgorithm

# Create custom configuration
config = PipelineConfig(
    num_qubits_per_job=10,
    num_jobs=5,
    simulation_mode=SimulationMode.MULTI_THREADED,
    scheduling_algorithm=SchedulingAlgorithm.FFD
)

# Run pipeline
pipeline = QuantumSchedulingPipeline(
    num_qubits_per_job=config.num_qubits_per_job,
    num_jobs=config.num_jobs
)

result_path = pipeline.run_complete_pipeline(
    simulation_mode=config.simulation_mode.value,
    experiment_id="custom_experiment"
)
```

### Batch Experiments

```python
from config import ExperimentConfig

# Configure parameter sweep
experiment_config = ExperimentConfig(
    qubit_ranges=[5, 7, 10, 15],
    job_ranges=[2, 5, 10],
    algorithms=[SchedulingAlgorithm.FFD, SchedulingAlgorithm.MILQ]
)

# Run multiple experiments (implementation in development)
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed and the component modules are available
2. **Backend Errors**: Check that the required quantum backends are accessible
3. **Memory Issues**: Use single-threaded mode for large experiments
4. **Permission Errors**: Ensure write permissions for result directories

### Debug Mode

Enable verbose logging for detailed troubleshooting:

```bash
python main.py --verbose
```

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For questions, issues, or contributions:

- Open an issue on GitHub
- Contact the development team
- Check the documentation for detailed API reference

## 🏆 Acknowledgments

- IBM Qiskit team for quantum computing framework
- MQT Bench for quantum circuit benchmarks
- Research community for scheduling algorithm insights

---

**Note**: This is a research and educational tool. For production quantum computing applications, additional validation and optimization may be required.
