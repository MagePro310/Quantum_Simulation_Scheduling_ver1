from abc import ABC, abstractmethod
from typing import Any, Dict
from qiskit import transpile
import sys

# Add the project root to sys.path if not already there
sys.path.append('./')

from component.sup_sys.job_info import JobInfo

class TranspilePhase(ABC):
    """
    Abstract base class for the Transpile Phase.
    
    Input: Output of schedule phase
    Output: Transpiled quantum circuit on quantum machine
    """
    
    @abstractmethod
    def execute(self, scheduler_job: Dict[str, JobInfo], machines: Dict[str, Any]) -> Dict[str, JobInfo]:
        """
        Executes the transpile phase.

        Args:
            scheduler_job: Dictionary of scheduled jobs.
            machines: Dictionary of available machines.

        Returns:
            Updated scheduler_job with transpiled circuits.
        """
        pass

class ConcreteTranspilePhase(TranspilePhase):
    def execute(self, scheduler_job: Dict[str, JobInfo], machines: Dict[str, Any]) -> Dict[str, JobInfo]:
        for job_id, job in scheduler_job.items():
            backend = machines.get(job.machine)
            if backend:
                # Perform transpilation
                # Remove qpd_1q operations if present (from original script logic)
                job.circuit.data = [hasChange for hasChange in job.circuit.data if hasChange.operation.name != "qpd_1q"]
                
                # Standard transpilation
                job.transpiled_circuit = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
                
                # Measured transpilation (as seen in original script, used for execution)
                # Note: Original script comments out measure_all but then uses transpiled_circuit_measured later?
                # Actually, line 256 in original script: job.circuit.measure_all()
                # line 257: job.transpiled_circuit_measured = transpile(...)
                # But line 189 was commented out.
                # However, line 274 uses job_info.transpiled_circuit_measured
                # So we should follow the logic around line 250 in original script.
                
                # We need to be careful not to modify the original circuit in place if we want to keep it pure, 
                # but qiskit circuits are mutable.
                # The script does: job.circuit.measure_all() then transpile.
                
                # Let's clone or just do it as script does.
                job.circuit.measure_all()
                job.transpiled_circuit_measured = transpile(job.circuit, backend, scheduling_method='alap', layout_method='trivial')
            else:
                print(f"No backend found for machine {job.machine}. Skipping job {job_id}.")
            
            # job.print() # Optional logging
            
        return scheduler_job