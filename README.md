# Quantum Simulation Scheduling

A quantum circuit scheduling and benchmarking framework that compares multiple scheduling algorithms for efficient execution across quantum machines.

## 🎯 Overview

This system implements and compares 4 quantum scheduling algorithms:
- **FFD** (First Fit Decreasing) - Heuristic
- **MTMC** (Multi-Task Multi-Constraint) - Heuristic  
- **MILQ_extend** (Mixed Integer Linear with Quantum cutting) - ILP
- **NoTaDS** (No Task Decomposition Scheduling) - ILP

The framework handles:
- Circuit cutting for large quantum circuits
- Multi-machine scheduling optimization
- Transpilation to target backends
- Execution simulation with fidelity analysis

## 📁 Project Structure

```
Quantum_Simulation_Scheduling/
├── benchmarks/          # Algorithm comparison and benchmarking
│   ├── algorithms/      # Implementation of 4 scheduling algorithms
│   ├── comparison/      # Comparison tools and results
│   └── reports/         # Generated benchmark reports
├── component/           # Reusable modules
│   ├── a_backend/       # Fake quantum backends
│   ├── b_benchmark/     # MQT benchmark circuits
│   ├── c_circuit_work/  # Circuit cutting and knitting
│   ├── d_scheduling/    # Scheduling algorithms core
│   ├── e_transpile/     # Circuit transpilation
│   ├── f_assemble/      # Fidelity calculation
│   └── h_analyze/       # Analysis tools
├── flow/                # Phase-based workflow orchestration
│   ├── input/           # Input phase (circuit loading)
│   ├── schedule/        # Schedule phase (job assignment)
│   ├── transpile/       # Transpile phase (circuit adaptation)
│   ├── execution/       # Execution phase (simulation)
│   └── result/          # Result phase (metrics calculation)
├── tests/               # Unit and integration tests
├── docs/                # Additional documentation
└── results/             # Execution results (gitignored)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Conda (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1.git
cd Quantum_Simulation_Scheduling

# Create and activate conda environment
conda create -n squan python=3.10
conda activate squan

# Install dependencies
pip install -r requirements.txt
```

### Running Benchmarks

```bash
# IMPORTANT: Always activate conda environment first
conda activate squan

# Run all 4 algorithms comparison
cd benchmarks/comparison
python comparison_runner.py

# Run single algorithm
cd benchmarks/comparison/config
python runLoopTestFFD.py 5 8  # 5 jobs, 8 qubits each
```

### Running Tests

```bash
conda activate squan

# Test phase implementations
python tests/test_flow_concrete.py

# Test with debug output
python tests/test_debug_output.py
```

## 📊 Performance Metrics

The framework calculates:
- **Makespan**: Total execution time
- **Turnaround Time**: Average job completion time
- **Response Time**: Average job start delay
- **Utilization**: Machine usage efficiency
- **Throughput**: Jobs completed per time unit
- **Fidelity**: Quantum state quality (0-1)

## 🔧 Key Features

### Circuit Cutting
Automatically splits large circuits that exceed machine capacity:
```python
from component.c_circuit_work.cutting.width_c import WidthCircuitCutter

cutter = WidthCircuitCutter(circuit, max_width=5)
result = cutter.gate_to_reduce_width()
```

### Scheduling Algorithms
Compare different algorithms:
```python
from benchmarks.algorithms.FFD.FFD_implement import schedule_jobs_ffd

schedule = schedule_jobs_ffd(job_capacities, machine_capacities)
```

### Phase-Based Pipeline
```python
# Input → Schedule → Transpile → Execution → Result
input_phase.execute() → schedule_phase.execute() → ...
```

## 📖 Documentation

- **[Benchmarking Guide](benchmarks/USAGE_GUIDE.md)** - How to run comparisons
- **[Algorithm Details](benchmarks/algorithms/ALGORITHM_DETAILS.md)** - Algorithm specifications
- **[AI Coding Instructions](.github/copilot-instructions.md)** - For AI assistants

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 Citation

If you use this framework in your research, please cite:

```bibtex
@software{quantum_scheduling_2025,
  title={Quantum Simulation Scheduling Framework},
  author={Your Name},
  year={2025},
  url={https://github.com/MagePro310/Quantum_Simulation_Scheduling_ver1}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Qiskit - Quantum computing framework
- MQT Bench - Quantum circuit benchmarks
- IBM Quantum - Backend simulations

## 📧 Contact

For questions or issues, please open an issue on GitHub or contact the maintainers.

---

**Last Updated**: December 31, 2025
