import sys
import os
from typing import List, Tuple, Any

# Add the project root to sys.path
sys.path.append('/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

try:
    from flow.input.phase_input import InputPhase
    from flow.schedule.phase_schedule import SchedulePhase
    from flow.transpile.phase_transpile import TranspilePhase
    from flow.execution.execution_phase import ExecutionPhase
    from flow.result.result_phase import ResultPhase
    print("Successfully imported all phase classes.")
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)

def test_abstract_instantiation():
    phases = [
        ("InputPhase", InputPhase),
        ("SchedulePhase", SchedulePhase),
        ("TranspilePhase", TranspilePhase),
        ("ExecutionPhase", ExecutionPhase),
        ("ResultPhase", ResultPhase)
    ]

    for name, cls in phases:
        try:
            cls()
            print(f"FAIL: {name} should not be instantiable.")
        except TypeError as e:
            print(f"PASS: {name} raised TypeError on instantiation: {e}")

def test_concrete_implementation():
    class ConcreteInput(InputPhase):
        def execute(self, quantum_circuits: List[Any], machines: List[Any], priority: Any) -> Tuple[List[Any], List[Any], Any]:
            return [], [], None

    try:
        ConcreteInput()
        print("PASS: ConcreteInput instantiated successfully.")
    except TypeError as e:
        print(f"FAIL: ConcreteInput failed to instantiate: {e}")

if __name__ == "__main__":
    test_abstract_instantiation()
    test_concrete_implementation()
