# Quantum Scheduling Data Analysis Pipeline

A professional, modular data analysis pipeline for quantum scheduling experiments that transforms JSON experiment results into comprehensive visualizations and statistical reports.

## 🚀 Features

### Professional Data Processing

- **Robust JSON extraction** with error handling and validation
- **Flexible configuration system** supporting multiple experiment types
- **Data normalization** for fair algorithm comparison
- **Statistical analysis** with comprehensive metrics

### Beautiful Visualizations

- **Enhanced line plots** with professional styling
- **Radar charts** for multi-dimensional algorithm comparison
- **Combined PDF reports** with all metrics
- **Customizable color schemes** and plot styling

### Comprehensive Reporting

- **Detailed performance rankings** for each metric
- **Overall algorithm recommendations** by use case
- **Statistical summaries** with confidence intervals
- **Executive summary reports** for stakeholders

### Modular Architecture

- **Configurable components** for different experiment types
- **Extensible design** for new metrics and algorithms
- **Clean separation** of concerns (processing, visualization, reporting)
- **Command-line interface** for automation

## 📁 Project Structure

```text
quantum_data_analyzer.py      # Main analysis pipeline
analysis_config.py           # Configuration management
examples_usage.py           # Usage examples
data_analyzer.py           # Legacy comprehensive version
export_json_to_csv.py      # Original extraction script
radarplot.py              # Original radar plot script
```

## 🛠 Installation

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

1. **Required Python packages:**

- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0
- scipy >= 1.7.0

## 🎯 Quick Start

### Basic Usage

```python
from quantum_data_analyzer import QuantumAnalysisPipeline
from analysis_config import load_config

# Load default configuration
config = load_config('5_5_ghz')

# Run analysis
pipeline = QuantumAnalysisPipeline(config)
df = pipeline.run_analysis()
```

### Command Line Usage

```bash
# Basic analysis with default settings
python quantum_data_analyzer.py

# Custom experiment path
python quantum_data_analyzer.py --experiment-path "component/finalResult/custom"

# Analyze specific algorithms only
python quantum_data_analyzer.py --algorithms FFD MILQ

# Skip visualizations (data processing only)
python quantum_data_analyzer.py --no-plots
```

## ⚙️ Configuration

### Predefined Configurations

The pipeline includes several predefined configurations:

```python
# Available presets
configs = {
    "5_5_ghz": "5 circuits, 5 qubits, GHZ states",
    "10_10_qft": "10 circuits, 10 qubits, QFT",
    "scalability_test": "Variable size scalability analysis"
}
```

### Custom Configuration

```python
from analysis_config import create_custom_config

config = create_custom_config(
    EXPERIMENT_NAME="My_Custom_Analysis",
    ALGORITHMS=["FFD", "MILQ", "NoTaDS"],
    METRICS=[
        "average_fidelity",
        "makespan", 
        "average_throughput"
    ],
    FIGURE_SIZE=(14, 10),
    GENERATE_RADAR_PLOTS=True
)
```

### Configuration Options

| Category | Parameter | Description | Default |
|----------|-----------|-------------|---------|
| **Experiment** | `ALGORITHMS` | List of algorithms to analyze | `["FFD", "MILQ", "NoTaDS", "MTMC"]` |
| | `METRICS` | Metrics to extract and analyze | 8 performance metrics |
| | `BASE_RESULT_PATH` | Path to experiment results | `"component/finalResult/5_5"` |
| **Visualization** | `FIGURE_SIZE` | Plot dimensions | `(12, 8)` |
| | `LINE_PLOT_PALETTE` | Color scheme for line plots | `"Set2"` |
| | `GENERATE_RADAR_PLOTS` | Create radar charts | `True` |
| **Output** | `SAVE_INTERMEDIATE_RESULTS` | Save normalized CSVs | `True` |
| | `GENERATE_SUMMARY_REPORT` | Create text report | `True` |

## 📊 Output Structure

The pipeline creates a comprehensive output structure:

```text
analyze/
├── all/
│   ├── csv/                    # Individual metric CSV files
│   │   ├── average_fidelity_data.csv
│   │   ├── makespan_data.csv
│   │   └── ...
│   └── plots/                  # Visualization files
│       ├── all_metrics_analysis.pdf
│       ├── average_fidelity_analysis.png
│       └── ...
├── calculation/                # Normalized metric data
│   ├── normalized_average_fidelity.csv
│   └── ...
└── reports/                    # Analysis reports
    └── analysis_summary.txt
radarplots/                     # Radar chart visualizations
├── all_algorithms_radar.png
├── FFD_radar.png
└── ...
```

## 📈 Supported Metrics

The pipeline analyzes the following performance metrics:

### Timing Metrics

- **Average Turnaround Time**: Total time from job submission to completion
- **Average Response Time**: Time from submission to first response
- **Makespan**: Total time to complete all jobs
- **Scheduler Latency**: Time spent in scheduling decisions

### Quality Metrics

- **Average Fidelity**: Circuit execution accuracy
- **Sampling Overhead**: Additional time for quantum sampling

### Efficiency Metrics

- **Average Throughput**: Jobs completed per unit time
- **Average Utilization**: Resource usage efficiency

## 🎨 Visualization Features

### Enhanced Line Plots

- Professional color schemes with consistent branding
- Multi-dimensional analysis (circuits × qubits × algorithms)
- Statistical error bars and confidence intervals
- Customizable styling and formatting

### Radar Charts

- **Individual algorithm profiles** showing strengths/weaknesses
- **Comparative analysis** with all algorithms overlay
- **Normalized scoring** for fair comparison across metrics
- **Professional color mapping** for clear differentiation

### Combined Reports

- **Multi-page PDF** with all metric analyses
- **High-resolution exports** suitable for publications
- **Consistent styling** across all visualizations

## 📋 Advanced Usage Examples

### 1. Performance Comparison Study

```python
# Compare multiple algorithm configurations
from quantum_data_analyzer import QuantumAnalysisPipeline
from analysis_config import create_custom_config

# Focus on performance-critical metrics
config = create_custom_config(
    EXPERIMENT_NAME="Performance_Comparison_Study",
    METRICS=[
        "average_responseTime",
        "makespan", 
        "average_throughput",
        "scheduler_latency"
    ],
    MINIMIZE_METRICS={
        'average_responseTime', 
        'makespan', 
        'scheduler_latency'
    }
)

pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

### 2. Quality-Focused Analysis

```python
# Analyze fidelity and accuracy metrics
config = create_custom_config(
    EXPERIMENT_NAME="Quality_Analysis",
    METRICS=[
        "average_fidelity",
        "sampling_overhead"
    ],
    FIGURE_SIZE=(16, 10),
    RADAR_FIGURE_SIZE=(12, 12)
)

pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

### 3. Scalability Study

```python
# Analyze how algorithms scale with problem size
config = create_custom_config(
    EXPERIMENT_NAME="Scalability_Study",
    BASE_RESULT_PATH="component/finalResult/scalability",
    ALGORITHMS=["FFD", "MILQ"],
    GENERATE_INDIVIDUAL_PLOTS=True,
    GENERATE_COMBINED_PDF=True
)

pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

## 🔧 Extending the Pipeline

### Adding New Metrics

1. **Update configuration:**

```python
# In analysis_config.py
METRICS = [
    # ... existing metrics ...
    "new_custom_metric"
]
```

1. **Handle metric normalization:**

```python
# Add to MINIMIZE_METRICS if lower values are better
MINIMIZE_METRICS = {
    # ... existing metrics ...
    'new_custom_metric'  # if lower is better
}
```

### Adding New Algorithms

1. **Update algorithm list:**

```python
ALGORITHMS = [
    # ... existing algorithms ...
    "NEW_ALGORITHM"
]
```

1. **Ensure data files follow naming convention:**

```text
component/finalResult/5_5/NEW_ALGORITHM/ghz/2_2.0_0.json
```

### Custom Visualization

```python
class CustomVisualizer(AdvancedVisualizer):
    def create_custom_plot(self, df):
        # Your custom visualization logic
        pass

# Use custom visualizer
pipeline = QuantumAnalysisPipeline(config)
pipeline.visualizer = CustomVisualizer(config)
results = pipeline.run_analysis()
```

## 🐛 Troubleshooting

### Common Issues

1. **Missing data files:**
   - Check file paths in configuration
   - Verify JSON file naming convention
   - Enable `SKIP_MISSING_FILES = True` for partial analysis

2. **Memory issues with large datasets:**
   - Process algorithms separately
   - Reduce figure sizes in configuration
   - Disable PDF generation for large datasets

3. **Import errors:**
   - Verify all dependencies are installed
   - Check Python version compatibility (3.8+)
   - Update matplotlib and seaborn to latest versions

### Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Run analysis with detailed logging
pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

## 📚 Migration from Legacy Scripts

### From export_json_to_csv.py

**Old approach:**

```python
# Manual file processing
for dataset_name, folder_path in folder_paths.items():
    for file in os.listdir(folder_path):
        # ... manual processing
```

**New approach:**

```python
# Automated pipeline
config = load_config('5_5_ghz')
pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

### From radarplot.py

**Old approach:**

```python
# Manual CSV reading and plotting
csv_files = glob.glob('analyze/calculation/normalized_*.csv')
# ... manual radar plot creation
```

**New approach:**

```python
# Integrated radar plots
config = create_custom_config(GENERATE_RADAR_PLOTS=True)
pipeline = QuantumAnalysisPipeline(config)
results = pipeline.run_analysis()
```

## 🤝 Contributing

1. **Code style:** Follow PEP 8 guidelines
2. **Documentation:** Update docstrings for new features
3. **Testing:** Add unit tests for new components
4. **Configuration:** Extend configuration system for new parameters

## 📄 License

This project is part of the Quantum Scheduling Simulation framework. See the main project license for details.

## 🙏 Acknowledgments

- Built upon the original analysis scripts by the Quantum Scheduling Team
- Visualization improvements inspired by modern data science best practices
- Configuration system designed for research reproducibility

---

For questions and support, please refer to the main project documentation or contact the development team.
