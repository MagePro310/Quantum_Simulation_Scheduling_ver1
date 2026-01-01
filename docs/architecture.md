# System Architecture

## Component-Flow Pattern

The Quantum Simulation Scheduling framework uses a two-layer architecture:

### 1. Component Layer (Reusable Modules)

Located in `component/`, these are reusable building blocks:

#### `a_backend/` - Backend Management
- Fake quantum backend implementations
- Interface to Qiskit backends

#### `b_benchmark/` - Circuit Generation
- MQT benchmark integration
- Circuit generation utilities

#### `c_circuit_work/` - Circuit Operations
- **cutting/**: Circuit width and depth cutting
- **knitting/**: Result reconstruction

#### `d_scheduling/` - Scheduling Core
- **algorithm/**: Implementation of scheduling algorithms
  - `heuristic/`: FFD, MTMC
  - `ilp/`: MILQ_extend, NoTaDS
- **analyze/**: Metrics calculation
- **datawork/**: Data processing utilities

#### `e_transpile/` - Circuit Adaptation
- Transpilation to target backends

#### `f_assemble/` - Result Processing
- Fidelity calculation from execution counts

#### `h_analyze/` - Advanced Analysis
- ILP-specific analysis tools

#### `sup_sys/` - Support Systems
- JobInfo dataclass (universal job container)
- Algorithm and backend loaders

### 2. Flow Layer (Workflow Orchestration)

Located in `flow/`, these orchestrate the execution pipeline:

#### Phase 1: Input (`flow/input/`)
- Load quantum circuits
- Initialize JobInfo objects
- Define available machines

#### Phase 2: Schedule (`flow/schedule/`)
- Check circuit-machine compatibility
- Cut oversized circuits
- Run scheduling algorithm
- Assign jobs to machines with timing

#### Phase 3: Transpile (`flow/transpile/`)
- Adapt circuits to target backend topology
- Optimize gate sequences

#### Phase 4: Execution (`flow/execution/`)
- Simulate circuit execution
- Calculate quantum states

#### Phase 5: Result (`flow/result/`)
- Calculate fidelity
- Aggregate metrics (makespan, utilization, etc.)
- Generate reports

## Data Flow

```
Input Phase
    ↓ origin_job_info (Dict[str, JobInfo])
    ↓ machines (Dict[str, Backend])
    ↓
Schedule Phase
    ↓ scheduler_job (Dict[str, JobInfo]) - with assignments
    ↓ data (schedule results)
    ↓
Transpile Phase
    ↓ scheduler_job - with transpiled circuits
    ↓
Execution Phase
    ↓ scheduler_job - with execution results
    ↓ utilization_permachine
    ↓
Result Phase
    ↓ result_Schedule (final metrics)
```

## Key Design Patterns

### Abstract Base Class (ABC) Pattern
Each phase has an abstract base class enforcing the `execute()` interface:
```python
class SchedulePhase(ABC):
    @abstractmethod
    def execute(self, ...):
        pass
```

This allows swapping implementations without changing other phases.

### JobInfo Container Pattern
`JobInfo` is the universal data container that flows through all phases:
- Starts with circuit metadata
- Accumulates scheduling information
- Stores transpilation results
- Contains execution outcomes

### Component Prefix System
Components use alphabetic prefixes for clear organization:
- `a_` = backends
- `b_` = benchmarks
- `c_` = circuit operations
- `d_` = scheduling
- `e_` = transpile
- `f_` = assemble
- `h_` = analyze

## Extension Points

### Adding New Scheduling Algorithm
1. Create implementation in `component/d_scheduling/algorithm/`
2. Create concrete phase class in `flow/schedule/`
3. Add to benchmark configuration

### Adding New Circuit Operation
1. Add module to `component/c_circuit_work/`
2. Import in relevant phase

### Adding New Phase
1. Create ABC in `flow/new_phase/`
2. Implement concrete class
3. Update pipeline execution

---

For more details, see [AI Coding Instructions](../.github/copilot-instructions.md)
