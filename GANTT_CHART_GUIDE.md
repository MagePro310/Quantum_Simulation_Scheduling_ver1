# Gantt Chart Visualization Guide

## Overview

The Quantum Scheduling Pipeline automatically generates Gantt charts to visualize quantum job scheduling and execution timelines. This guide explains the chart types, naming conventions, and customization options.

## Chart Types

### 1. Scheduling Gantt Charts

Shows the initial scheduling decisions made by the algorithm:

- **When generated**: After scheduling algorithm execution
- **Purpose**: Visualize job assignments and timing decisions
- **File suffix**: `_scheduling_`

### 2. Simulation Gantt Charts  

Shows the actual execution timeline after simulation:

- **When generated**: After scheduling simulation
- **Purpose**: Display refined timing and resource utilization
- **File suffix**: `_simulation_`

## Naming Convention

Gantt charts follow a structured naming pattern:

```text
{Algorithm}_{Benchmark}_{JobCount}jobs_{AvgQubits}qubits_{Stage}_{Timestamp}.pdf
```

### Components Breakdown

| Component | Description | Example |
|-----------|-------------|---------|
| **Algorithm** | Scheduling algorithm used | `FFD`, `MILQ`, `MTMC`, `NoTaDS` |
| **Benchmark** | Circuit benchmark type | `ae`, `qft`, `grover` |
| **JobCount** | Number of jobs scheduled | `2jobs`, `5jobs` |
| **AvgQubits** | Average qubits per job | `7qubits`, `10qubits` |
| **Stage** | Generation stage | `scheduling`, `simulation` |
| **Timestamp** | Generation time | `20250623_143022` |

### Example Filenames

```text
FFD_ghz_2jobs_7qubits_scheduling_20250623_143022.pdf
FFD_ghz_2jobs_7qubits_simulation_20250623_143045.pdf
MILQ_qft_5jobs_10qubits_scheduling_20250623_144512.pdf
```

## Directory Structure

Charts are organized in experiment-specific directories:

```text
component/finalResult/
├── {experiment_id}/
│   ├── ganttCharts/
│   │   ├── FFD_ghz_2jobs_7qubits_scheduling_20250623_143022.pdf
│   │   ├── FFD_ghz_2jobs_7qubits_simulation_20250623_143045.pdf
│   │   └── ...
│   └── {algorithm}/
│       └── ...
```

## Configuration Options

### Enabling/Disabling Chart Generation

```python
config = PipelineConfig(
    save_visualizations=True,    # Enable chart saving
    show_plots=False,           # Don't display during execution
    gantt_chart_dir="myCharts"  # Custom directory name
)
```

### Command Line Control

```bash
# Generate charts but don't display
python main.py --save-charts

# Generate and display charts
python main.py --save-charts --show-plots

# Custom chart directory
python main.py --gantt-dir "experiment_charts"
```

## Chart Features

### Visual Elements

1. **Job Bars**: Each job shown as horizontal bar
2. **Machine Assignment**: Different colors per backend
3. **Timeline**: X-axis shows time progression
4. **Resource Labels**: Y-axis shows quantum machines
5. **Grid Lines**: Help read exact timing values

### Color Coding

- **IBM Belem**: Blue tones
- **IBM Manila**: Green tones  
- **Other Backends**: Distinct color palette
- **Failed Jobs**: Red indicators

### Timeline Information

- **Start Time**: When job begins execution
- **Duration**: Length of job execution
- **End Time**: When job completes
- **Dependencies**: Visual connection lines (if applicable)

## Advanced Usage

### Batch Chart Generation

For parameter sweeps or multiple experiments:

```bash
# Generate charts for multiple configurations
for algo in FFD MILQ MTMC; do
    python main.py --algorithm $algo --experiment-id "comparison_$algo"
done
```

### Chart Comparison

Charts can be compared across:

- **Algorithms**: Same jobs, different scheduling
- **Parameters**: Different job/qubit configurations  
- **Backends**: Same schedule, different machines
- **Time**: Before/after optimization

### Custom Analysis

Charts provide insights into:

- **Load Balancing**: Even distribution across machines
- **Utilization**: Percentage of machine usage
- **Idle Time**: Gaps in machine scheduling
- **Bottlenecks**: Overloaded resources
- **Optimization**: Scheduling efficiency

## File Management

### Automatic Cleanup

- Old charts with same pattern are automatically replaced
- No manual cleanup required
- Timestamp ensures uniqueness within experiment

### Manual Organization

```bash
# Archive old experiments
mkdir archived_experiments
mv component/finalResult/old_experiment_* archived_experiments/

# Clean all charts
rm -rf component/finalResult/*/ganttCharts/
```

## Troubleshooting

### Common Issues

**Charts not generating**:

- Verify `save_visualizations=True` in configuration
- Check write permissions for output directory
- Ensure matplotlib is properly installed

**Charts appear blank**:

- Verify job scheduling completed successfully
- Check for empty job lists
- Review pipeline execution logs

**File conflicts**:

- Charts automatically replace files with same base name
- Use unique experiment IDs to avoid conflicts
- Check disk space availability

### Debug Mode

Enable verbose output to trace chart generation:

```bash
python main.py --verbose --show-plots
```

This will show detailed logging during chart creation and display charts for immediate inspection.

## Best Practices

1. **Consistent Naming**: Use descriptive experiment IDs
2. **Regular Cleanup**: Archive old experiments periodically
3. **Comparison Studies**: Use same parameters across algorithms
4. **Documentation**: Record chart generation settings
5. **Version Control**: Track chart-generating code changes

---

This guide covers the complete Gantt chart functionality in the Quantum Scheduling Pipeline. For additional questions, refer to the main README.md or system documentation.
