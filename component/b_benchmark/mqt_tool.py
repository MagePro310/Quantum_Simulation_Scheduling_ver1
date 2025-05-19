from mqt.bench import get_benchmark
from qiskit import QuantumCircuit, QuantumRegister

def benchmark_circuit(name_algorithm:str, circuit_size: int) -> QuantumCircuit:
    
    return get_benchmark(benchmark_name="ghz", level="alg", circuit_size=circuit_size)



def create_circuit(num_qubits: int, nameRegister) -> QuantumCircuit:
    """Returns a quantum circuit implementing the GHZ state.

    Arguments:
        num_qubits: number of qubits of the returned quantum circuit
    """

    # nameq = "q" + nameRegister
    # q = QuantumRegister(num_qubits, nameq)
    # qc = QuantumCircuit(q, name="ghz")
    # qc.h(q[-1])
    # for i in range(1, num_qubits):
    #     qc.cx(q[num_qubits - i], q[num_qubits - i - 1])
    # qc.measure_all()

    # return qc

    q = QuantumRegister(num_qubits, "q")
    qc = QuantumCircuit(q, name="ghz")
    qc.h(q[-1])
    for i in range(1, num_qubits):
        qc.cx(q[num_qubits - i], q[num_qubits - i - 1])
    qc.measure_all()

    return qc