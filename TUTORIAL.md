# Quantum Scheduling Pipeline Tutorial

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [Understanding the Output](#understanding-the-output)
4. [Advanced Configuration](#advanced-configuration)
5. [Running Experiments](#running-experiments)
6. [Analyzing Results](#analyzing-results)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Getting Started

### Prerequisites

Before starting, ensure you have:

- Python 3.8 or higher
- All dependencies installed (see installation steps below)
- Basic understanding of quantum computing concepts

### Installation

1. **Clone and navigate to the repository**:

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

   You should see:

   ```text
   ============================================================
   QUANTUM SCHEDULING PIPELINE TEST SUITE
   ============================================================
   Testing imports...
   ✓ All required modules imported successfully
   
   Testing configuration...
   ✓ Configuration validation passed
   
   Testing pipeline initialization...
   ✓ Pipeline initialization passed
   
   Testing metrics data structure...
   ✓ Metrics data structure passed
   
   Testing configuration serialization...
   ✓ Configuration serialization passed
   
   ============================================================
   TEST RESULTS: 5/5 tests passed
   🎉 All tests passed!
   ```

---

## Basic Usage

### Your First Run

Let's start with the simplest possible execution:

```bash
python main.py
```

This command runs the pipeline with default settings:

- **2 quantum circuits** to schedule
- **7 qubits per circuit**
- **FFD (First Fit Decreasing)** scheduling algorithm
- **Multi-threaded** simulation mode
- **IBM Belem and Manila** fake backends

### Understanding the Command Line Interface

View all available options:

```bash
python main.py --help
```

Key parameters you'll use most often:

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `--qubits` | Qubits per circuit | 7 | `--qubits 10` |
| `--jobs` | Number of circuits | 2 | `--jobs 5` |
| `--algorithm` | Scheduling algorithm | FFD | `--algorithm MILQ` |
| `--mode` | Execution mode | multi_threaded | `--mode single_threaded` |
| `--verbose` | Detailed output | False | `--verbose` |
| `--show-plots` | Display charts | False | `--show-plots` |

### Example: Custom Parameters

```bash
python main.py --qubits 10 --jobs 3 --algorithm MILQ --verbose
```

This runs:

- 3 circuits with 10 qubits each
- MILQ scheduling algorithm
- Verbose logging enabled

---

## Understanding the Output

### Console Output Explained

When you run the pipeline, you'll see several sections:

#### 1. Configuration Summary

```text
============================================================
QUANTUM SCHEDULING PIPELINE
============================================================
Jobs: 2
Qubits per job: 7
Algorithm: FFD
Mode: multi_threaded
Backends: belem, manila
Shots: 1024
Save Visualizations: True
Show Plots: False
Experiment ID: 5_5
============================================================
```

#### 2. Pipeline Execution Stages

```text
INFO: Setting up quantum backends...
INFO: Generating benchmark quantum circuits...
INFO: Performing circuit cutting...
INFO: Executing FFD scheduling algorithm...
INFO: Transpiling circuits for assigned backends...
INFO: Running scheduling simulation in multi_threaded mode...
INFO: Performing circuit knitting...
INFO: Running quantum simulations...
INFO: Calculating performance metrics...
```

#### 3. Performance Metrics

```text
============================================================
QUANTUM SCHEDULING PERFORMANCE METRICS
============================================================
Algorithm: FFD
Benchmark: ghz
Circuits: 2
Average Qubits: 7.0
Machines: ['fake_belem', 'fake_manila']
------------------------------------------------------------
Scheduler Latency: 0.000s
Makespan: 18848.000s
Average Turnaround Time: 14920.000s
Average Response Time: 7600.000s
Average Throughput: 0.000 jobs/s
Average Utilization: 0.981
Average Fidelity: 0.8742
Sampling Overhead: 18.000
============================================================
```

#### 4. Results Location

```text
✅ Experiment completed successfully!
📊 Results saved to: component/finalResult/5_5/FFD/ghz/2_7.0_10.json
```

### File Outputs

The pipeline generates several types of output files:

#### 1. Gantt Charts (PDF)

Located in: `component/finalResult/{experiment_id}/ganttCharts/`

Files follow this naming pattern:

```text
{Algorithm}_{Benchmark}_{JobCount}jobs_{AvgQubits}qubits_{Stage}_{Timestamp}.pdf
```

Example:

```text
FFD_ghz_2jobs_7qubits_scheduling_20250623_154046.pdf
FFD_ghz_2jobs_7qubits_simulation_20250623_154046.pdf
```

#### 2. Results Data (JSON)

Located in: `component/finalResult/{experiment_id}/{algorithm}/{benchmark}/`

Example: `2_7.0_10.json`

Contains comprehensive metrics:

```json
{
  "num_circuits": 2,
  "algorithm_name": "ghz",
  "average_qubits": 7.0,
  "schedule_name": "FFD",
  "average_turnaround_time": 14920.0,
  "average_fidelity": 0.8742,
  "makespan": 18848.0
}
```

---

## Advanced Configuration

### Using Configuration Files

Create reusable experiment configurations:

#### 1. Save Configuration

```bash
python main.py --qubits 12 --jobs 6 --algorithm MTMC --save-config large_experiment.json
```

#### 2. Load Configuration

```bash
python main.py --config large_experiment.json
```

### Configuration File Format

Example `my_experiment.json`:

```json
{
  "num_qubits_per_job": 10,
  "num_jobs": 5,
  "backend_names": ["belem", "manila"],
  "scheduling_algorithm": "MILQ",
  "simulation_mode": "single_threaded",
  "shots": 2048,
  "enable_circuit_cutting": true,
  "enable_circuit_knitting": true,
  "save_visualizations": true,
  "show_plots": false,
  "experiment_id": "my_study"
}
```

### Programmatic Usage

For more complex workflows, use Python directly:

```python
from quantum_scheduling_pipeline import QuantumSchedulingPipeline
from config import PipelineConfig, SchedulingAlgorithm, SimulationMode

# Create configuration
config = PipelineConfig(
    num_qubits_per_job=8,
    num_jobs=4,
    scheduling_algorithm=SchedulingAlgorithm.MILQ,
    simulation_mode=SimulationMode.MULTI_THREADED,
    experiment_id="custom_experiment",
    show_plots=True
)

# Run pipeline
pipeline = QuantumSchedulingPipeline(config)
result_path = pipeline.run_complete_pipeline()

# Access results
print(f"Results saved to: {result_path}")
print(f"Final makespan: {pipeline.metrics.makespan}")
print(f"Average fidelity: {pipeline.metrics.average_fidelity}")
```

---

## Running Experiments

### Single Algorithm Evaluation

Test one algorithm with different parameters:

```bash
# Small scale
python main.py --qubits 5 --jobs 2 --algorithm FFD --experiment-id "small_FFD"

# Medium scale
python main.py --qubits 8 --jobs 4 --algorithm FFD --experiment-id "medium_FFD"

# Large scale
python main.py --qubits 12 --jobs 8 --algorithm FFD --experiment-id "large_FFD"
```

### Algorithm Comparison Study

Compare all available algorithms:

```bash
# Set common parameters
QUBITS=10
JOBS=5
EXPERIMENT="comparison_study"

# Run each algorithm
python main.py --qubits $QUBITS --jobs $JOBS --algorithm FFD --experiment-id "${EXPERIMENT}_FFD"
python main.py --qubits $QUBITS --jobs $JOBS --algorithm MILQ --experiment-id "${EXPERIMENT}_MILQ"
python main.py --qubits $QUBITS --jobs $JOBS --algorithm MTMC --experiment-id "${EXPERIMENT}_MTMC"
python main.py --qubits $QUBITS --jobs $JOBS --algorithm NoTaDS --experiment-id "${EXPERIMENT}_NoTaDS"
```

### Scalability Analysis

Test how algorithms perform with increasing workload:

```bash
# Bash script for scalability study
#!/bin/bash

for qubits in 5 7 10 12 15; do
    for jobs in 2 4 6 8 10; do
        echo "Running: $qubits qubits, $jobs jobs"
        python main.py \
            --qubits $qubits \
            --jobs $jobs \
            --algorithm FFD \
            --experiment-id "scalability_${qubits}q_${jobs}j" \
            --quiet
    done
done
```

### Circuit Processing Impact Study

Compare performance with and without circuit processing:

```bash
# With circuit cutting and knitting (default)
python main.py --qubits 15 --jobs 4 --experiment-id "with_processing"

# Without circuit cutting
python main.py --qubits 15 --jobs 4 --no-cutting --experiment-id "no_cutting"

# Without circuit knitting
python main.py --qubits 15 --jobs 4 --no-knitting --experiment-id "no_knitting"

# Without both
python main.py --qubits 15 --jobs 4 --no-cutting --no-knitting --experiment-id "no_processing"
```

---

## Analyzing Results

### Viewing Gantt Charts

Generated charts show:

- **Scheduling Charts**: Initial algorithm decisions
- **Simulation Charts**: Actual execution timeline

Open charts with any PDF viewer:

```bash
# Linux
evince component/finalResult/5_5/ganttCharts/FFD_ghz_2jobs_7qubits_scheduling_*.pdf

# macOS
open component/finalResult/5_5/ganttCharts/FFD_ghz_2jobs_7qubits_scheduling_*.pdf

# Windows
start component/finalResult/5_5/ganttCharts/FFD_ghz_2jobs_7qubits_scheduling_*.pdf
```

### Reading JSON Results

Use command line tools or Python to analyze results:

#### Command Line Analysis

```bash
# Pretty print JSON
cat component/finalResult/5_5/FFD/ghz/2_7.0_10.json | python -m json.tool

# Extract specific metrics
grep "makespan" component/finalResult/5_5/FFD/ghz/2_7.0_10.json
```

#### Python Analysis

```python
import json
import glob

# Load all results for comparison
results = []
for file_path in glob.glob("component/finalResult/*/FFD/*/*.json"):
    with open(file_path, 'r') as f:
        data = json.load(f)
        results.append(data)

# Compare makespans
for result in results:
    print(f"Algorithm: {result['schedule_name']}, Makespan: {result['makespan']}")

# Find best performing configuration
best = min(results, key=lambda x: x['makespan'])
print(f"Best configuration: {best['experiment_id']} with makespan {best['makespan']}")
```

### Comparative Analysis

Compare multiple experiment results:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load results into DataFrame
data = []
for algorithm in ['FFD', 'MILQ', 'MTMC', 'NoTaDS']:
    try:
        with open(f"component/finalResult/comparison_{algorithm}/{algorithm}/ghz/5_10.0_0.json", 'r') as f:
            result = json.load(f)
            result['algorithm'] = algorithm
            data.append(result)
    except FileNotFoundError:
        print(f"Results not found for {algorithm}")

df = pd.DataFrame(data)

# Create comparison plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

metrics = ['makespan', 'average_utilization', 'average_fidelity', 'scheduler_latency']
for i, metric in enumerate(metrics):
    ax = axes[i//2, i%2]
    df.plot(x='algorithm', y=metric, kind='bar', ax=ax)
    ax.set_title(f'{metric.replace("_", " ").title()}')

plt.tight_layout()
plt.savefig('algorithm_comparison.png')
plt.show()
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors

**Problem**: `ImportError: No module named 'component.utils'`

**Solution**:

```bash
# Ensure you're in the correct directory
pwd
# Should show: /path/to/Quantum_Simulation_Scheduling

# Add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python main.py
```

#### 2. Backend Loading Failures

**Problem**: `No backends could be loaded`

**Solution**:

```bash
# Check available backends
python -c "from component.a_backend.fake_backend import get_available_backends; print(len(get_available_backends()))"

# Try with specific backends
python main.py --backends belem --qubits 5 --jobs 2
```

#### 3. Memory Issues

**Problem**: System runs out of memory during execution

**Solutions**:

```bash
# Use single-threaded mode
python main.py --mode single_threaded

# Reduce problem size
python main.py --qubits 5 --jobs 2

# Disable visualizations
python main.py --no-visualizations

# Reduce simulation shots
python main.py --shots 512
```

#### 4. Permission Errors

**Problem**: Cannot write output files

**Solution**:

```bash
# Check and fix permissions
chmod -R 755 component/finalResult/
mkdir -p component/finalResult/test/
```

### Debug Mode

For detailed troubleshooting:

```bash
# Maximum verbosity
python main.py --verbose --show-plots --experiment-id "debug_session"

# Minimal test for isolation
python main.py --qubits 3 --jobs 1 --no-visualizations --experiment-id "minimal_test"
```

### Getting Help

1. **Check test suite**:

   ```bash
   python test_pipeline.py
   python test_gantt_naming.py
   ```

2. **Verify system components**:

   ```bash
   python -c "from quantum_scheduling_pipeline import QuantumSchedulingPipeline; print('✓ Pipeline ready')"
   python -c "from component.utils import setup_logging; print('✓ Utils working')"
   ```

3. **Check dependencies**:

   ```bash
   pip list | grep qiskit
   pip list | grep numpy
   pip list | grep matplotlib
   ```

---

## Best Practices

### Experiment Design

1. **Start Small**: Begin with small problems (2-3 jobs, 5-7 qubits) to verify setup
2. **Use Consistent IDs**: Use descriptive experiment IDs like `scalability_10q_5j`
3. **Save Configurations**: Save working configurations for reproducibility
4. **Document Changes**: Keep notes of parameter modifications and their effects

### Performance Optimization

1. **Choose Appropriate Mode**:
   - Use `single_threaded` for debugging and small experiments
   - Use `multi_threaded` for production runs and large parameter sweeps

2. **Manage Visualizations**:
   - Use `--no-visualizations` for batch processing
   - Use `--show-plots` only for interactive analysis

3. **Resource Management**:
   - Monitor system memory during large experiments
   - Use `--shots 512` for faster preliminary testing
   - Increase to `--shots 4096` for publication-quality results

### Reproducible Research

1. **Version Control**: Keep track of code versions used for experiments
2. **Configuration Files**: Save all experiment configurations
3. **Result Organization**: Use systematic experiment IDs and folder structures
4. **Documentation**: Record experimental hypotheses and findings

### Batch Processing

For large-scale studies, create organized batch scripts:

```bash
#!/bin/bash
# experiment_batch.sh

# Set common parameters
SHOTS=1024
BASE_ID="publication_study"

# Algorithm comparison
for algo in FFD MILQ MTMC NoTaDS; do
    echo "Testing algorithm: $algo"
    python main.py \
        --qubits 10 \
        --jobs 5 \
        --algorithm $algo \
        --shots $SHOTS \
        --experiment-id "${BASE_ID}_${algo}" \
        --quiet
done

# Scalability analysis
for size in 5 10 15; do
    echo "Testing size: $size qubits"
    python main.py \
        --qubits $size \
        --jobs 4 \
        --algorithm FFD \
        --shots $SHOTS \
        --experiment-id "${BASE_ID}_scale_${size}q" \
        --quiet
done

echo "Batch processing complete!"
```

Make it executable and run:

```bash
chmod +x experiment_batch.sh
./experiment_batch.sh
```

---

## Advanced Topics

### Custom Backend Configuration

You can modify backend configurations by editing:

```python
# In component/a_backend/fake_backend.py
# Add custom backend implementations
```

### Algorithm Extension

To add new scheduling algorithms:

1. Implement algorithm in `component/d_scheduling/algorithm/`
2. Register in `config.py` SchedulingAlgorithm enum
3. Update algorithm loader in `component/sup_sys/algorithm_loader.py`

### Result Processing Automation

Create automated analysis scripts:

```python
# analysis_automation.py
import json
import glob
import pandas as pd

def analyze_experiment_batch(experiment_prefix):
    """Analyze all results with given prefix."""
    pattern = f"component/finalResult/{experiment_prefix}*/*/*/*json"
    results = []
    
    for file_path in glob.glob(pattern):
        with open(file_path, 'r') as f:
            data = json.load(f)
            results.append(data)
    
    df = pd.DataFrame(results)
    
    # Generate summary statistics
    summary = df.groupby('schedule_name').agg({
        'makespan': ['mean', 'std', 'min', 'max'],
        'average_fidelity': ['mean', 'std'],
        'average_utilization': ['mean', 'std']
    }).round(4)
    
    print("Experiment Summary:")
    print("=" * 80)
    print(summary)
    
    return df

# Usage
results_df = analyze_experiment_batch("comparison_study")
```

---

## Conclusion

This tutorial covers the essential aspects of using the Quantum Scheduling Pipeline. The system is designed to be:

- **Flexible**: Accommodates various experimental needs
- **Extensible**: Can be modified for custom requirements
- **Reproducible**: Ensures consistent results across runs
- **Professional**: Suitable for both research and production use

For additional questions or advanced usage scenarios, refer to:

- [README.md](README.md) - Complete system documentation
- [GANTT_CHART_GUIDE.md](GANTT_CHART_GUIDE.md) - Visualization details
- [TRANSFORMATION_SUMMARY.md](TRANSFORMATION_SUMMARY.md) - Development background

**Happy experimenting with quantum scheduling!** 🚀
