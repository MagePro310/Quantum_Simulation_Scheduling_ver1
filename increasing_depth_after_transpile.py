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

# backend0 = FakeAlgiers()
# pm = generate_preset_pass_manager(backend=backend0, optimization_level=0)
qc_algorithmic_level = get_benchmark(benchmark="ae", level=BenchmarkLevel.ALG, circuit_size=6)
print(qc_algorithmic_level)
