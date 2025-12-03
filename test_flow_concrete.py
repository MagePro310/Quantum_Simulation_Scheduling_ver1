import sys
import os

# Add the project root to sys.path
sys.path.append('/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling')

from flow.input.phase_input import ConcreteInputPhase
from flow.schedule.phase_schedule import ConcreteSchedulePhase
from flow.transpile.phase_transpile import ConcreteTranspilePhase
from flow.execution.execution_phase import ConcreteExecutionPhase
from flow.result.result_phase import ConcreteResultPhase

def test_concrete_flow():
    num_jobs = 2
    num_qubits_per_job = 4
    
    print("Starting Input Phase...")
    input_phase = ConcreteInputPhase()
    origin_job_info, machines, result_Schedule = input_phase.execute(num_jobs, num_qubits_per_job)
    print("Input Phase Complete.")
    
    print("Starting Schedule Phase...")
    schedule_phase = ConcreteSchedulePhase()
    scheduler_job, data, result_Schedule = schedule_phase.execute(origin_job_info, machines, result_Schedule)
    print("Schedule Phase Complete.")
    
    print("Starting Transpile Phase...")
    transpile_phase = ConcreteTranspilePhase()
    scheduler_job = transpile_phase.execute(scheduler_job, machines)
    print("Transpile Phase Complete.")
    
    print("Starting Execution Phase...")
    execution_phase = ConcreteExecutionPhase()
    scheduler_job, utilization_permachine = execution_phase.execute(scheduler_job, machines, data)
    print("Execution Phase Complete.")
    
    print("Starting Result Phase...")
    result_phase = ConcreteResultPhase()
    final_result = result_phase.execute(scheduler_job, origin_job_info, data, utilization_permachine, result_Schedule)
    print("Result Phase Complete.")
    
    print("Final Result Summary:")
    print(f"Algorithm: {final_result.nameAlgorithm}")
    print(f"Schedule: {final_result.nameSchedule}")
    print(f"Average Fidelity: {final_result.average_fidelity}")

if __name__ == "__main__":
    test_concrete_flow()
