# Quantum Scheduling Data Analysis - Clean Version

## 📁 Essential Files

### Main Analysis Pipeline
- **`data_analyzer.py`** - Enhanced, professional analysis pipeline
  - Replaces the original `export_json_to_csv.py` and `radarplot.py`
  - Provides comprehensive data processing, visualization, and reporting
  - Ready-to-use with one command: `python data_analyzer.py`

### Original Files (Backup)
- **`export_json_to_csv.py`** - Original CSV export script
- **`radarplot.py`** - Original radar plot generation

### Core Project Files
- **`quantum_scheduling_pipeline.py`** - Main scheduling pipeline
- **`main.py`** - Project entry point
- **`config.py`** - Project configuration
- **`test_pipeline.py`** - Pipeline testing

## 🚀 Usage

### Run Enhanced Analysis
```bash
python data_analyzer.py
```

This will:
- Extract data from JSON experiment results
- Create professional visualizations
- Generate radar charts comparing algorithms
- Save CSV data for each metric
- Create comprehensive analysis reports

### Output Structure
```
analyze/
├── all/
│   ├── csv/                    # Individual metric CSV files
│   ├── plots/                  # Professional line plots + PDF report
│   └── analysis_summary.txt    # Comprehensive analysis report
└── calculation/                # Normalized metric scores

radarplots/                     # Algorithm comparison radar charts
├── all_algorithms_radar.png    # Combined comparison
└── [ALGORITHM]_radar.png       # Individual algorithm profiles
```

## ✨ Key Features

- **Professional visualizations** with consistent styling
- **Comprehensive reporting** with algorithm rankings
- **Error handling** and detailed logging
- **Modular architecture** for easy maintenance
- **Publication-ready outputs** with high-resolution plots

## 📊 Analysis Results

The enhanced pipeline processes your experiment data and provides:
- Algorithm performance rankings for each metric
- Overall performance summary with recommendations
- Beautiful visualizations suitable for research publications
- Statistical analysis with normalized scoring

---

Your quantum scheduling analysis pipeline is now clean, professional, and ready for production use!
