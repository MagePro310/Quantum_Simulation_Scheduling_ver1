
from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')

from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2
from component.d_scheduling.simulation.scheduling_multithread import simulate_scheduling as simulate_multithread
from component.d_scheduling.analyze import analyze_cal
from component.f_assemble.assemble_work import fidelity_from_counts
from component.sup_sys.job_info import JobInfo

class ExecutionPhase(ABC):
    """
    Abstract base class for the Execution Phase.
    
    Input: Output of transpile phase
    Output: Result of quantum circuit after transpiled on quantum machine
    """
    
    @abstractmethod
    def execute(self, scheduler_job: Dict[str, JobInfo], machines: Dict[str, Any], data: Any) -> Tuple[Dict[str, JobInfo], Any]:
        """
        Executes the execution phase.

        Args:
            scheduler_job: Dictionary of scheduled jobs.
            machines: Dictionary of available machines.
            data: Data loaded from schedule.json.

        Returns:
            A tuple containing:
            - Updated scheduler_job (with fidelity).
            - utilization_permachine.
        """
        pass

class ConcreteExecutionPhase(ExecutionPhase):
    def execute(self, scheduler_job: Dict[str, JobInfo], machines: Dict[str, Any], data: Any) -> Tuple[Dict[str, JobInfo], Any]:
        aer_simulator = AerSimulator()
        
        # Simulate multithread execution
        jobs_data = data.copy()
        updated_jobs = simulate_multithread(jobs_data, scheduler_job)
        
        for job_name, job_info in scheduler_job.items():
            backend = machines.get(job_info.machine)
            
            if backend:
                transpiled_circuit = job_info.transpiled_circuit_measured
                
                # Run the ideal simulation
                ideal_result = aer_simulator.run(transpiled_circuit, shots=1024).result()
                ideal_counts = ideal_result.get_counts(transpiled_circuit)
                
                # Run circuit on the simulated backend
                job = SamplerV2(backend).run([transpiled_circuit], shots=1024)
                sim_result = job.result()[0]
                sim_counts = sim_result.data.meas.get_counts()
                
                # Calculate fidelity
                fidelity_val, rho_ideal, rho_sim = fidelity_from_counts(ideal_counts, sim_counts)
                
                # Store the fidelity values
                job_info.fidelity = fidelity_val
                
        utilization_permachine = analyze_cal.calculate_utilization(data)
        print(utilization_permachine)
        
        return scheduler_job, utilization_permachine