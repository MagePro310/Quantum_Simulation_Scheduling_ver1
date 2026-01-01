# Quantum Scheduling Simulation - AI Coding Instructions

## Project Overview
A quantum circuit scheduling and benchmarking framework that compares 4 algorithms (FFD, MTMC, MILQ_extend, NoTaDS) for scheduling quantum circuits across multiple quantum machines. The system handles circuit cutting, knitting, transpilation, execution simulation, and fidelity analysis.

## Architecture: Component-Flow Pattern

### Core Pattern
The project uses a **two-layer architecture**:
- **`component/`**: Reusable modules (backends, benchmarks, circuit operations, scheduling algorithms)
- **`flow/`**: Abstract phase-based workflow orchestration (input → schedule → transpile → execution → result)

Each phase in `flow/` inherits from an ABC and implements `execute()`:
```python
class SchedulePhase(ABC):
    @abstractmethod
    def execute(self, origin_job_info, machines, result_Schedule) -> Tuple[...]:
        pass
```

### Component Organization (Prefix System)
- `a_backend/`: Fake quantum backend implementations
- `b_benchmark/`: MQT benchmark tools for quantum circuits
- `c_circuit_work/`: Circuit cutting (width/depth) and knitting operations
- `d_scheduling/`: Core scheduling algorithms (heuristic: FFD/MTMC, ILP: MILQ_extend/NoTaDS)
- `e_transpile/`: Circuit transpilation to target backends
- `f_assemble/`: Fidelity calculation from execution counts
- `h_analyze/`: Analysis tools for scheduling results
- `sup_sys/`: Support systems (JobInfo dataclass, loaders)

### Data Flow
1. **Input Phase**: Quantum circuits → JobInfo objects with metadata
2. **Schedule Phase**: Applies algorithm → assigns jobs to machines with timing
3. **Transpile Phase**: Adapts circuits to backend topology
4. **Execution Phase**: Simulates on Qiskit Aer or IBM Runtime
5. **Result Phase**: Analyzes fidelity, turnaround time, utilization

## Critical Developer Workflows

### Running Benchmarks
The **NEW** benchmarking system (2025-12-31 reorganization) centralizes comparison:
```bash
# FIRST: Activate conda environment
conda activate squan

# Run all 4 algorithms with automated comparison
cd benchmarks/comparison
python comparison_runner.py

# Run single algorithm
cd benchmarks/comparison/config
python runLoopTestFFD.py <num_jobs> <num_qubits_per_job>
# Example: python runLoopTestFFD.py 5 8
```

### Testing Phases
Test abstract phase implementations:
```bash
conda activate squan  # Required!
python test_flow_abstraction.py  # Validates ABC enforcement
python test_flow_concrete.py     # Tests concrete implementations
```t abstract phase implementations:
```bash
python test_flow_abstraction.py  # Validates ABC enforcement
python test_flow_concrete.py     # Tests concrete implementations
```

### Path Management
**Critical**: All scripts use `sys.path.append('./')` to add project root. When creating new modules:
```python
import sys
sys.path.append('./')
from component.d_scheduling.algorithm.heuristic.FFD import FFD_implement
```

## JobInfo: The Central Data Structure

`component/sup_sys/job_info.py` is the **universal job container**:
```python
@dataclass
class JobInfo:
    job_id: str
    circuit: QuantumCircuit
    qubits: int
    machine: str
    start_time: float
    duration: float
    end_time: float
    
    # Circuit cutting results
    result_cut: SubCircuitInfo
    childrenJobs: list['JobInfo']  # For cut circuits
    
    # Transpiled variants
    transpiled_circuit: QuantumCircuit
    knitted_circuit: QuantumCircuit
    
    # Execution results
    fidelity: float
```

Jobs flow through the pipeline accumulating state. **Never recreate JobInfo** - mutate existing instances.

## Scheduling Algorithms: Implementation Pattern

### Heuristic Algorithms (FFD, MTMC)
Located in `component/d_scheduling/algorithm/heuristic/` and copied to `benchmarks/algorithms/`
```python
def schedule_jobs_ffd(job_capacities: dict, machine_capacities: dict):
    """FFD with dynamic time scheduling where duration = qubits"""
    jobs = sorted(job_capacities.items(), key=lambda x: -x[1])  # Decreasing order
    # Find earliest start time considering machine capacity and overlaps
    # Returns: schedule list with {job, machine, start, end, qubits}
```

### ILP Algorithms (MILQ_extend, NoTaDS)
Use PuLP for constraint optimization. Example constraint pattern:
```python
# Machine capacity constraint
for k, t in product(machines, timesteps):
    prob += pulp.lpSum(x[i,k] * qubits[i] for i in jobs) <= capacity[k]
```

**Key difference**: MILQ_extend allows task decomposition (circuit cutting), NoTaDS schedules whole circuits only.

## Circuit Cutting/Knitting

### Cutting (`component/c_circuit_work/cutting/width_c.py`)
When `circuit.qubits > max_machine_width`, use `WidthCircuitCutter`:
```python
cutter = WidthCircuitCutter(circuit, max_width=5)
result = cutter.gate_to_reduce_width()  # Returns SubCircuitInfo
# result.subcircuits: Dict of smaller circuits
# result.overhead: Sampling overhead factor
```

### Knitting (`component/c_circuit_work/knitting/width_k.py`)
Recombine subcircuits:
```python
from component.c_circuit_work.knitting.width_k import merge_multiple_circuits
merged = merge_multiple_circuits(subcircuits_list)
```

## Metrics & Analysis

Key metrics in `ResultOfSchedule` dataclass:
- **Makespan**: Max end time across all jobs
- **Turnaround Time**: job.end_time - job.submission_time (avg across jobs)
- **Response Time**: job.start_time - job.submission_time (avg)
- **Utilization**: (sum of job_qubits * duration) / (num_machines * makespan * capacity)
- **Throughput**: num_jobs / makespan
- **Fidelity**: Quantum state fidelity from counts comparison

Analyze with: `component/d_scheduling/analyze/analyze_cal.py`

## Benchmarking Configuration

Edit `benchmarks/comparison/config/benchmark_config.json` to modify:
```json
{
  "benchmark_parameters": {
    "num_qubits": [5, 10, 15, 20],
    "depth_range": [10, 50, 100],
    "num_runs": 10,
    "timeout_seconds": 300
  }
}
```

## Common Patterns

### 1. Creating New Scheduling Algorithm
Add to `component/d_scheduling/algorithm/{heuristic|ilp}/`:
```python
def schedule_jobs_newalgo(job_capacities, machine_capacities):
    # Must return list of dicts with keys: job, machine, start, end, qubits
    schedule = []
    for job_id, qubits in job_capacities.items():
        schedule.append({
            "job": job_id,
            "machine": selected_machine,
            "start": start_time,
            "end": end_time,
            "qubits": qubits
        })
    return schedule
```

### 2. Adding to Benchmark Comparison
1. Copy algorithm to `benchmarks/algorithms/NEWALGO/`
2. Add entry to `benchmarks/comparison/config/benchmark_config.json`
3. Create `runLoopTestNEWALGO.py` following FFD pattern
4. Runner will auto-discover it

### 3. Handling Circuit Collections
Use dictionaries with job names as keys:
```python
origin_job_info: Dict[str, JobInfo] = {
    "job_0": JobInfo(job_name="job_0", circuit=qc0, ...),
    "job_1": JobInfo(job_name="job_1", circuit=qc1, ...)
}
```

## Dependencies & Environment

**CRITICAL**: Always activate conda environment before running:
```bash
conda activate squan
```

Key dependencies:
- **Qiskit** 1.x: Core quantum circuit library
- **Qiskit Aer**: Local quantum simulator
- **Qiskit IBM Runtime**: Cloud execution primitives (SamplerV2)
- **qiskit-addon-cutting**: Circuit cutting/knitting
- **PuLP**: ILP solver for MILQ_extend/NoTaDS
- **MQT Bench**: Quantum benchmark circuits
- **NumPy**, **Matplotlib**: Data analysis and visualization

Install: (Check for requirements.txt or setup.py in repo)

## File Naming Conventions
- Test scripts: `runLoopTest{ALGORITHM}.py` (legacy root), `test_algorithm_{ALGORITHM}.ipynb` (notebooks)
- Results: Save to `benchmarks/comparison/results/{ALGORITHM}/` as JSON
- Implementations: `{ALGORITHM}_implement.py` or `{ALGORITHM}_implementation.py`

## Anti-Patterns to Avoid
- ❌ Don't import from `benchmarks/algorithms/` in core code - use `component/d_scheduling/algorithm/`
- ❌ Don't hardcode machine capacities - pass as dict parameters
- ❌ Don't assume circuits fit on machines - always check width and apply cutting if needed
- ❌ Don't modify circuits in-place during analysis - use `.copy()` first

## Documentation Hierarchy
1. **Quick Start**: `REORGANIZATION_START_HERE.md`
2. **Architecture**: This file + `REORGANIZATION_DETAILED.md`
3. **Usage**: `benchmarks/USAGE_GUIDE.md`
4. **Algorithm Details**: `benchmarks/algorithms/ALGORITHM_DETAILS.md`
