from mqt.bench import get_benchmark
from qiskit import QuantumCircuit

def benchmark_circuit(name_algorithm:str, circuit_size: int) -> QuantumCircuit:
    
    return get_benchmark(benchmark_name="ghz", level="alg", circuit_size=circuit_size)