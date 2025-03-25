import json

from qiskit import QuantumCircuit
import numpy as np

np.random.seed(42)

def _generate_problem():
    pass

def generate_schedule(problem):
    pass

def example_problem(big_m: int, timesteps: int , jobs: dict, machines: dict, filename: str = "scheduling"): 
    """Runs the example problem and saves the LP file and JSON file.
    TODO should also run the solution explorer and produce the output pdf.

    Args:
        big_m (int): LP metavariable.
        timesteps (int): LP metavariable.
        filename (str, optional): Filename for .lp, .json and .pdf. Defaults to "scheduling".
    """
    _problem, job_capacities = _generate_problem(jobs, machines, big_m, timesteps)
    print("Problem:")
    print(_problem.base_jobs)
    print("Job Capacities:")
    print(job_capacities)
    _, _, lp_instance = generate_schedule(_problem)
    
    
    lp_instance.problem.writeLP(f"{filename}.lp")

    with open(f"{filename}.json", "w+", encoding="utf-8") as f:
        json.dump(
            {
                "params": {
                    "jobs": list(job_capacities.keys()),
                    "machines": list(_problem.accelerators.keys()),
                    "job_capcities": job_capacities,
                    "machine_capacities": _problem.accelerators,
                    "timesteps": timesteps,
                    "processing_times": _problem.process_times,
                    "setup_times": _problem.setup_times,
                },
                "variables": {
                    var.name: var.varValue
                    for var in lp_instance.problem.variables()
                    if var.name.startswith(("c_j", "s_j", "x_ik_", "z_ikt_"))
                },
            },
            f,
            indent=4,
        )