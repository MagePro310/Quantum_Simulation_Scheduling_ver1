# Algorithm Comparison Visualization

This directory contains tools for visualizing and comparing quantum scheduling algorithm results.

## Overview

After running benchmarks for different scheduling algorithms (FFD, MTMC, MILQ_extend, NoTaDS), use these visualization tools to generate comprehensive comparison charts and reports.

## Quick Start

### 1. Run Benchmarks First

```bash
# Run all algorithm benchmarks
cd ../..
./run.sh benchmark

# Or run individual algorithms
./run.sh benchmark-ffd 5 8
```

### 2. Generate Visualizations

```bash
# Generate all charts and reports
cd benchmarks/comparison
python visualize_results.py

# Or use the utility script
cd ../..
./run.sh visualize
```

### 3. View Results

Charts and reports will be saved in `benchmarks/comparison/reports/`

## Generated Visualizations

### 1. **Metrics Comparison Bar Chart**
- File: `metrics_comparison_<timestamp>.png`
- Shows all 8 metrics side-by-side for each algorithm
- Includes value labels on each bar
- Metrics: makespan, turnaround time, response time, utilization, throughput, fidelity, sampling overhead, scheduler latency

### 2. **Makespan Comparison**
- File: `makespan_comparison_<timestamp>.png`
- Two charts:
  - Absolute makespan values
  - Percentage difference from best performer
- Highlights the most efficient scheduling

### 3. **Utilization vs Fidelity Scatter Plot**
- File: `utilization_fidelity_<timestamp>.png`
- Shows trade-off between resource utilization and quantum fidelity
- Each algorithm is a labeled point
- Helps identify balanced algorithms

### 4. **Performance Radar Chart**
- File: `radar_chart_<timestamp>.png`
- Normalized comparison of 5 key metrics
- Spider/radar plot showing algorithm strengths
- Easy visual comparison of overall performance

### 5. **Gantt Charts**
- File: `gantt_chart_<timestamp>.png`
- Visual schedule timeline for each algorithm
- Shows job placement on machines over time
- Color-coded by qubit count
- Displays makespan for each algorithm

### 6. **Summary Report**
- File: `summary_report_<timestamp>.txt`
- Text-based comprehensive report
- Detailed metrics for each algorithm
- Best performers by metric
- Machine usage statistics

## Advanced Usage

### Generate Specific Charts

```bash
# Only metrics comparison
python analysis/visualize_comparison.py --chart metrics

# Only radar chart
python analysis/visualize_comparison.py --chart radar

# Only Gantt chart
python analysis/visualize_comparison.py --chart gantt

# Only text report
python analysis/visualize_comparison.py --chart report
```

### Custom Directories

```bash
# Specify custom results directory
python analysis/visualize_comparison.py --results-dir /path/to/results

# Specify custom output directory
python analysis/visualize_comparison.py --output-dir /path/to/output
```

### Using run.sh

```bash
# Generate all charts
./run.sh visualize

# Generate specific chart type
./run.sh visualize-chart radar
./run.sh visualize-chart makespan
./run.sh visualize-chart gantt
```

## Metrics Explained

### Performance Metrics

1. **Makespan** (Lower is Better)
   - Total time to complete all jobs
   - Most critical metric for overall efficiency

2. **Average Turnaround Time** (Lower is Better)
   - Average time from job submission to completion
   - Measures user-perceived latency

3. **Average Response Time** (Lower is Better)
   - Average time from submission to start
   - Measures scheduling delay

4. **Average Utilization** (Higher is Better)
   - Percentage of quantum resources used
   - Measures resource efficiency

5. **Average Throughput** (Higher is Better)
   - Jobs completed per time unit
   - Measures processing rate

### Quantum-Specific Metrics

6. **Average Fidelity** (Higher is Better)
   - Quantum state accuracy after execution
   - Measures quantum quality

7. **Sampling Overhead** (Lower is Better)
   - Extra sampling needed for circuit cutting
   - Measures cutting cost

8. **Scheduler Latency** (Lower is Better)
   - Time spent computing the schedule
   - Measures algorithm efficiency

## Result File Structure

Expected directory structure:

```
benchmarks/comparison/
├── results/
│   ├── FFD/
│   │   └── schedule.json
│   ├── MTMC/
│   │   └── schedule.json
│   ├── MILQ_extend/
│   │   └── schedule.json
│   └── NoTaDS/
│       └── schedule.json
├── reports/                          # Generated visualizations
│   ├── metrics_comparison_<timestamp>.png
│   ├── makespan_comparison_<timestamp>.png
│   ├── utilization_fidelity_<timestamp>.png
│   ├── radar_chart_<timestamp>.png
│   ├── gantt_chart_<timestamp>.png
│   └── summary_report_<timestamp>.txt
└── analysis/
    └── visualize_comparison.py       # Visualization engine
```

## JSON Format

Each algorithm's `schedule.json` should contain:

```json
[
    {
        "job": "1",
        "qubits": 4,
        "machine": "fake_belem",
        "capacity": 5,
        "start": 0.0,
        "end": 4.0,
        "duration": 4
    },
    ...
]
```

## Customization

### Adding New Metrics

Edit `visualize_comparison.py` to add new metrics:

```python
self.metrics = [
    'makespan',
    'average_turnaroundTime',
    # Add your metric here
    'your_new_metric'
]

self.metric_labels = {
    'makespan': 'Makespan (time units)',
    # Add label here
    'your_new_metric': 'Your Metric Label'
}
```

### Changing Colors

Modify the color scheme:

```python
self.colors = {
    'FFD': '#2E86AB',      # Blue
    'MTMC': '#A23B72',     # Purple
    'MILQ_extend': '#F18F01',  # Orange
    'NoTaDS': '#C73E1D'    # Red
}
```

### Chart Styling

Matplotlib style settings are in the `__init__` method:

```python
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
```

## Dependencies

Required Python packages:
- `matplotlib` - Chart generation
- `numpy` - Numerical computations
- `json` - JSON file parsing

Install dependencies:

```bash
pip install matplotlib numpy
```

Or use the project's requirements:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### No Data Found

**Error:** "No schedule data available"

**Solution:** Run benchmarks first to generate result files

```bash
cd benchmarks/comparison/config
python runLoopTestFFD.py 5 8
python runLoopTestMTMC.py 5 8
python runLoopTestMILQ.py 5 8
python runLoopTestNoTaDS.py 5 8
```

### Missing Metrics

**Issue:** Some metrics show 0 or missing values

**Solution:** The tool automatically calculates basic metrics from schedule data. For advanced metrics (fidelity, overhead), ensure your result files include these values.

### Chart Display Issues

**Issue:** Charts don't display properly

**Solution:** 
- Ensure matplotlib backend is configured: `export MPLBACKEND=Agg` for headless systems
- Use output files instead of interactive display
- Check display settings in `plt.show()` vs `plt.savefig()`

### Import Errors

**Error:** "ModuleNotFoundError: No module named 'component'"

**Solution:** Run from project root or ensure `sys.path` includes project directory

```bash
# Run from project root
cd /path/to/Quantum_Simulation_Scheduling
python benchmarks/comparison/visualize_results.py
```

## Examples

### Complete Workflow

```bash
# 1. Activate environment
conda activate squan

# 2. Run benchmarks for all algorithms
cd benchmarks/comparison/config
python runLoopTestFFD.py 10 8
python runLoopTestMTMC.py 10 8
python runLoopTestMILQ.py 10 8
python runLoopTestNoTaDS.py 10 8

# 3. Generate visualizations
cd ..
python visualize_results.py

# 4. View results
ls -lh reports/
```

### Automated Pipeline

```bash
#!/bin/bash
# Complete benchmark and visualization pipeline

echo "Running benchmarks..."
./run.sh benchmark

echo "Generating visualizations..."
./run.sh visualize

echo "Opening reports..."
cd benchmarks/comparison/reports
ls -lh
```

## Contributing

To add new visualization types:

1. Add method to `AlgorithmVisualizer` class in `visualize_comparison.py`
2. Follow existing pattern: `plot_<chart_name>(self, all_results, output_file)`
3. Add to `generate_all_visualizations()` method
4. Update this README with description

## License

Part of Quantum Simulation Scheduling project. See LICENSE file.
