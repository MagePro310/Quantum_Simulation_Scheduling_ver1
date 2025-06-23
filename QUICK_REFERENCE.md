# Quick Reference Card

## 🚀 Essential Commands

### Basic Usage

```bash
# Default run (2 jobs, 7 qubits, FFD algorithm)
python main.py

# Custom parameters
python main.py --qubits 10 --jobs 5 --algorithm MILQ

# Show help
python main.py --help

# Verbose output with plots
python main.py --verbose --show-plots
```

### Testing & Verification

```bash
# Run test suite
python test_pipeline.py

# Test Gantt charts
python test_gantt_naming.py

# Quick system check
python -c "from quantum_scheduling_pipeline import QuantumSchedulingPipeline; print('✓ Ready')"
```

### Configuration Management

```bash
# Save configuration
python main.py --qubits 12 --jobs 6 --save-config my_config.json

# Load configuration
python main.py --config my_config.json
```

### Common Research Workflows

```bash
# Algorithm comparison
python main.py --algorithm FFD --experiment-id "comp_FFD"
python main.py --algorithm MILQ --experiment-id "comp_MILQ"
python main.py --algorithm MTMC --experiment-id "comp_MTMC"

# Scalability study
python main.py --qubits 5 --jobs 2 --experiment-id "scale_small"
python main.py --qubits 10 --jobs 5 --experiment-id "scale_medium"
python main.py --qubits 15 --jobs 8 --experiment-id "scale_large"

# Circuit processing impact
python main.py --qubits 12 --jobs 4 --experiment-id "with_processing"
python main.py --qubits 12 --jobs 4 --no-cutting --no-knitting --experiment-id "no_processing"
```

## 📊 Key Parameters

| Parameter | Options | Default | Purpose |
|-----------|---------|---------|---------|
| `--qubits` | 3-20 | 7 | Circuit size |
| `--jobs` | 1-20 | 2 | Workload size |
| `--algorithm` | FFD, MILQ, MTMC, NoTaDS | FFD | Scheduling method |
| `--mode` | single_threaded, multi_threaded | multi_threaded | Execution mode |
| `--shots` | 512-4096 | 1024 | Simulation precision |
| `--experiment-id` | string | "5_5" | Results organization |

## 📁 Output Locations

```text
component/finalResult/{experiment_id}/
├── ganttCharts/              # PDF visualizations
│   ├── *_scheduling_*.pdf   # Initial schedule
│   └── *_simulation_*.pdf   # Actual execution
└── {algorithm}/{benchmark}/ # JSON results
    └── {jobs}_{qubits}_*.json
```

## 🔧 Troubleshooting

### Common Issues

```bash
# Import errors
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Memory issues
python main.py --mode single_threaded --shots 512

# Permission errors
chmod -R 755 component/finalResult/

# Debug mode
python main.py --verbose --qubits 3 --jobs 1 --experiment-id "debug"
```

### Performance Tips

- Use `--quiet` for batch processing
- Use `--no-visualizations` for speed
- Use `single_threaded` for debugging
- Use `multi_threaded` for production

## 📚 Documentation Links

- **[TUTORIAL.md](TUTORIAL.md)** - Complete step-by-step guide
- **[README.md](README.md)** - Full system documentation  
- **[GANTT_CHART_GUIDE.md](GANTT_CHART_GUIDE.md)** - Visualization details

---
*For detailed explanations, see the full tutorial and documentation files.*
