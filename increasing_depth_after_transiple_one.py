import sys
sys.path.append('./')
import json
import os
import qiskit
from qiskit import QuantumCircuit
import numpy as np
from dataclasses import dataclass
from enum import auto, Enum
import matplotlib.pyplot as plt
import math
import pandas as pd
from qiskit.visualization import plot_error_map
from component.a_backend.fake_backend import *
from mqt.bench.targets import get_available_gateset_names, get_available_device_names
from mqt.bench import BenchmarkLevel, get_benchmark
from mqt.bench.targets import get_device, get_target_for_gateset
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager
 
from qiskit.circuit import QuantumCircuit
from qiskit.visualization import plot_histogram
from component.sup_sys.backend_loader import load_backends
from qiskit.visualization import plot_error_map

benchmark_keys = [
    "ae",
    "bmw_quark_cardinality", 
    "bmw_quark_copula",
    "bv",
    "cdkm_ripple_carry_adder",
    "dj",
    "draper_qft_adder",
    "full_adder",
    "ghz",
    "graphstate",
    "grover",
    "half_adder",
    "hhl",
    "hrs_cumulative_multiplier",
    "modular_adder",
    "multiplier",
    "qaoa",
    "qft",
    "qftentangled",
    "qnn",
    "qpeexact",
    "qpeinexact",
    "qwalk",
    "randomcircuit",
    "rg_qft_multiplier",
    "shor",
    "vbe_ripple_carry_adder",
    "vqe_real_amp",
    "vqe_su2",
    "vqe_two_local",
    "wstate"
]

# Initialize backend and pass manager
backend0 = FakeAlgiers()

# Successful creation of quantum algorithm benchmarks
print("=== Successful Quantum Algorithm Creation ===")

# Create HHL algorithm at algorithmic level
try:
    qc_algorithmic_level = get_benchmark(benchmark="ae", level=BenchmarkLevel.ALG, circuit_size=18)
    print(f"HHL Algorithm created successfully:")
    print(f"- Qubits: {qc_algorithmic_level.num_qubits}")
    print(f"- Depth: {qc_algorithmic_level.depth()}")
    print(f"- Operations: {qc_algorithmic_level.count_ops()}")
    print()
except Exception as e:
    print(f"Failed to create HHL: {e}")

# Test multiple algorithms from your benchmark_keys list
results_data = []

for benchmark_name in benchmark_keys:
    try:
        print(f"Processing benchmark: {benchmark_name}")
        qc = get_benchmark(benchmark=benchmark_name, level=BenchmarkLevel.ALG, circuit_size=18)
        original_depth = qc.depth()
        
        # Apply transpilation
        try:
            isa_circuit = transpile(qc, backend=backend0, optimization_level=0)
            transpiled_depth = isa_circuit.depth()
        except Exception as transpile_error:
            print(f"Transpilation failed for {benchmark_name}: {transpile_error}")
            transpiled_depth = None
        
        results_data.append({
            'algorithm_name': benchmark_name,
            'original_depth': original_depth,
            'transpiled_depth': transpiled_depth
        })
        
        print(f"✓ {benchmark_name}: original depth {original_depth}, transpiled depth {transpiled_depth}")
        
    except Exception as e:
        results_data.append({
            'algorithm_name': benchmark_name,
            'original_depth': None,
            'transpiled_depth': None
        })
        print(f"✗ {benchmark_name}: {e}")

# Create DataFrame and save to CSV
df = pd.DataFrame(results_data)
csv_filename = 'quantum_algorithms_results.csv'
df.to_csv(csv_filename, index=False)

print(f"\n=== Results saved to {csv_filename} ===")
print(f"Total algorithms processed: {len(results_data)}")
print(f"Successfully created circuits: {len([r for r in results_data if r['original_depth'] is not None])}")
print(f"Successfully transpiled circuits: {len([r for r in results_data if r['transpiled_depth'] is not None])}")
