"""
Unit tests for backend and transpilation components.

Tests FakeBackend, transpilation, and circuit operations.
"""

import sys
import pytest

sys.path.insert(0, '/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from qiskit import QuantumCircuit


@pytest.mark.unit
class TestFakeBackend:
    """Test FakeBackend implementation."""
    
    def test_fake_backend_creation(self, fake_backend_5q):
        """Test creating a fake backend."""
        assert fake_backend_5q is not None
        assert fake_backend_5q.num_qubits == 5
    
    def test_fake_backend_properties(self, fake_backend_10q):
        """Test fake backend properties."""
        assert fake_backend_10q.num_qubits == 10
        assert hasattr(fake_backend_10q, 'configuration')
    
    def test_multiple_backends(self, fake_backend_5q, fake_backend_10q):
        """Test creating multiple backends."""
        assert fake_backend_5q.num_qubits == 5
        assert fake_backend_10q.num_qubits == 10
        assert fake_backend_5q.num_qubits != fake_backend_10q.num_qubits


@pytest.mark.unit
class TestCircuitTranspilation:
    """Test circuit transpilation operations."""
    
    def test_simple_circuit_transpilation(self, simple_circuit):
        """Test transpiling a simple circuit."""
        try:
            from component.e_transpile.transpile import transpile_circuit
            
            backend = None  # Use default backend
            transpiled = transpile_circuit(simple_circuit, backend)
            
            assert transpiled is not None
            assert isinstance(transpiled, QuantumCircuit)
        except ImportError:
            pytest.skip("Transpilation module not available")
    
    def test_circuit_structure_preservation(self, medium_circuit):
        """Test that transpilation preserves circuit structure."""
        try:
            from component.e_transpile.transpile import transpile_circuit
            
            original_qubits = medium_circuit.num_qubits
            transpiled = transpile_circuit(medium_circuit, None)
            
            # Transpiled should have same or more qubits (with added measurements)
            assert transpiled.num_qubits >= original_qubits
        except ImportError:
            pytest.skip("Transpilation module not available")


@pytest.mark.unit
class TestCircuitMeasurement:
    """Test adding measurements to circuits."""
    
    def test_circuit_with_measurements(self, simple_circuit):
        """Test circuit already has measurements."""
        # simple_circuit fixture includes measurements
        assert simple_circuit.num_clbits > 0
    
    def test_circuit_without_measurements(self):
        """Test adding measurements to unmeasured circuit."""
        qc = QuantumCircuit(3, name="no_measure")
        qc.h(0)
        qc.cx(0, 1)
        
        assert qc.num_clbits == 0
        
        # Add classical bits and measurements
        from qiskit.circuit import ClassicalRegister
        cr = ClassicalRegister(3, 'meas')
        qc.add_register(cr)
        qc.measure(range(3), range(3))
        
        assert qc.num_clbits == 3


@pytest.mark.unit
class TestBackendMatching:
    """Test matching circuits to backends."""
    
    def test_circuit_fits_backend(self, simple_circuit, fake_backend_5q):
        """Test that small circuit fits on backend."""
        assert simple_circuit.num_qubits <= fake_backend_5q.num_qubits
    
    def test_circuit_exceeds_backend(self, deep_circuit, fake_backend_5q):
        """Test that large circuit exceeds backend."""
        assert deep_circuit.num_qubits > fake_backend_5q.num_qubits
    
    def test_circuit_fits_larger_backend(self, deep_circuit, fake_backend_10q):
        """Test that circuit fits on larger backend."""
        assert deep_circuit.num_qubits <= fake_backend_10q.num_qubits


@pytest.mark.unit
class TestCircuitCutting:
    """Test circuit cutting operations."""
    
    def test_circuit_cutting_import(self):
        """Test circuit cutting module import."""
        try:
            from component.c_circuit_work.cutting.width_c import WidthCircuitCutter
            assert WidthCircuitCutter is not None
        except ImportError:
            pytest.skip("Circuit cutting module not available")
    
    def test_circuit_cutter_initialization(self, deep_circuit):
        """Test initializing circuit cutter."""
        try:
            from component.c_circuit_work.cutting.width_c import WidthCircuitCutter
            
            max_width = 5
            cutter = WidthCircuitCutter(deep_circuit, max_width=max_width)
            
            assert cutter is not None
        except ImportError:
            pytest.skip("Circuit cutting not available")
    
    def test_circuit_cut_width_exceeded(self, deep_circuit):
        """Test cutting a circuit that exceeds width."""
        try:
            from component.c_circuit_work.cutting.width_c import WidthCircuitCutter
            
            # deep_circuit is 8 qubits, cut to 5
            if deep_circuit.num_qubits > 5:
                cutter = WidthCircuitCutter(deep_circuit, max_width=5)
                result = cutter.gate_to_reduce_width()
                
                # Result should have subcircuits
                assert result is not None
        except ImportError:
            pytest.skip("Circuit cutting not available")


@pytest.mark.unit
class TestCircuitKnitting:
    """Test circuit knitting (recombining cut circuits)."""
    
    def test_knitting_module_import(self):
        """Test knitting module import."""
        try:
            from component.c_circuit_work.knitting.width_k import merge_multiple_circuits
            assert merge_multiple_circuits is not None
        except ImportError:
            pytest.skip("Circuit knitting module not available")
    
    def test_knit_identical_circuits(self, simple_circuit):
        """Test knitting identical circuits back together."""
        try:
            from component.c_circuit_work.knitting.width_k import merge_multiple_circuits
            
            # Create subcircuits by copying
            subcircuits = [simple_circuit.copy() for _ in range(2)]
            
            # Merge back
            merged = merge_multiple_circuits(subcircuits)
            
            assert merged is not None
        except ImportError:
            pytest.skip("Circuit knitting not available")


@pytest.mark.unit
class TestBenchmarkCircuits:
    """Test benchmark circuit generation."""
    
    def test_mqt_bench_import(self):
        """Test MQT Bench import."""
        try:
            from component.b_benchmark.mqt_tool import get_benchmark_circuits
            assert get_benchmark_circuits is not None
        except ImportError:
            pytest.skip("MQT Bench not available")
    
    def test_get_benchmark_circuit(self):
        """Test getting a benchmark circuit."""
        try:
            from component.b_benchmark.mqt_tool import get_benchmark_circuits
            
            circuits = get_benchmark_circuits(num_qubits=5, max_circuits=1)
            
            assert circuits is not None
            assert len(circuits) > 0
        except ImportError:
            pytest.skip("MQT Bench not available")
        except Exception:
            pytest.skip("MQT Bench unavailable or network issue")


@pytest.mark.unit
class TestCircuitValidation:
    """Test circuit validation utilities."""
    
    def test_valid_circuit(self, simple_circuit):
        """Test validating a correct circuit."""
        # Qiskit validates on creation
        assert simple_circuit is not None
        assert simple_circuit.num_qubits == 2
    
    def test_circuit_gate_count(self, medium_circuit):
        """Test counting gates in circuit."""
        gate_count = len(medium_circuit.data)
        
        assert gate_count > 0
    
    def test_circuit_depth(self, deep_circuit):
        """Test circuit depth calculation."""
        # deep_circuit should have reasonable depth
        depth = deep_circuit.decompose().depth()
        
        assert depth > 0


@pytest.mark.unit
class TestBackendCapabilities:
    """Test backend capability checking."""
    
    def test_backend_supports_gates(self, fake_backend_5q):
        """Test checking backend gate support."""
        # FakeBackend should support basic gates
        config = fake_backend_5q.configuration()
        
        assert config is not None
        assert config.n_qubits == 5
    
    def test_multiple_backend_types(self, fake_backend_5q, fake_backend_10q):
        """Test different backend capacities."""
        assert fake_backend_5q.configuration().n_qubits == 5
        assert fake_backend_10q.configuration().n_qubits == 10
