"""Modlue for the example problem."""
import json
from qiskit import QuantumCircuit, transpile
import numpy as np
from dataclasses import dataclass, field
from enum import auto, Enum
np.random.seed(42)
import pulp
from typing import Callable
from collections import defaultdict
from copy import deepcopy
from .....h_analyze.analyze_ilp.implement import JobResultInfo

class SchedulerType(Enum):
    """The type of scheduler to use."""

    BASELINE = auto()
    SIMPLE = auto()
    EXTENDED = auto()

PTimes = list[list[float]]
STimes = list[list[list[float]]]
@dataclass
class InfoProblem:
    """Defines an "InfoProblem" whis is used for evaluation purposes.

    This requires setup and process times to be defined as they are
    not calculated from the accelerators.
    """

    base_jobs: list[QuantumCircuit]
    accelerators: dict[str, int]
    big_m: int
    timesteps: int
    process_times: PTimes
    setup_times: STimes

@dataclass
class JobHelper:
    """Helper to keep track of job names."""

    name: str
    circuit: QuantumCircuit | None  # TODO optional necessary?

@dataclass
class LPInstance:
    """Helper to keep track of LP problem."""

    problem: pulp.LpProblem
    jobs: list[str]
    machines: list[str]
    x_ik: dict[str, dict[str, pulp.LpVariable]]
    z_ikt: dict[str, dict[str, dict[int, pulp.LpVariable]]]
    c_j: dict[str, pulp.LpVariable]
    s_j: dict[str, pulp.LpVariable]
    named_circuits: list[JobHelper]
        
def generate_schedule(
    problem: InfoProblem,
    schedule_type: SchedulerType,
) -> tuple[float, list[JobResultInfo], LPInstance | None]:
    """Generates the schedule for the given problem and schedule type.

    Baseline: Generates a schedule using binpacking.
    Else generates the schedule using MILP  and then calculates the makespan
    by executing the schedule with the correct p_ij and s_ij values.
    Args:
        problem (InfoProblem | ExecutableProblem ): The full problem definition.
        schedule_type (SchedulerType): The type of schedule to use.

    Returns:
        list[ScheduledJob]: List of ScheduledJobs. |
        tuple[float, list[JobResultInfo]]: The makespan and the list of jobs with their
        assigned machine and start and completion times.

    Raises:
        NotImplementedError: Unsupported types.
    """
    if isinstance(problem, InfoProblem):
        # print("Run info")
        return _generate_schedule_info(problem, schedule_type)
    raise NotImplementedError("Unsupported type")

def set_up_base_lp(
    base_jobs: list[QuantumCircuit],
    accelerators: dict[str, int],
    big_m: int,
    timesteps: int,
) -> LPInstance:
    """Wrapper to set up the base LP instance through one function.

    Generates a base LP instance with the given jobs and accelerators.
    It contains all the default constraints and variables.
    Does not contain the constraints regarding the successor relationship.

    Args:
        base_jobs (list[CircuitJob] | list[QuantumCircuit]): The list of quantum cirucits (jobs).
        accelerators (list[Accelerator] | dict[str, int]):
            The list of available accelerators (machines).
        big_m (int): Metavariable for the LP.
        timesteps (int): Meta variable for the LP, big enough to cover largest makespan.

    Returns:
        LPInstance: The LP instance object.

    Raises:
        NotImplementedError: If the input types are not supported.
    """
    if isinstance(accelerators, dict):
        return _set_up_base_lp_info(base_jobs, accelerators, big_m, timesteps)

    raise NotImplementedError

def _set_up_base_lp_info(
    base_jobs: list[QuantumCircuit],
    accelerators: dict[str, int],
    big_m: int,
    timesteps: int,
) -> LPInstance:
    """Sets up the base LP instance for use outside of provider.

    Generates a base LP instance with the given jobs and accelerators.
    It contains all the default constraints and variables.
    Does not contain the constraints regarding the successor relationship.

    Args:
        base_jobs (list[QuantumCircuit]): The list of quantum cirucits (jobs).
        accelerators (dict[str, int]): The list of available accelerators (machines).
        big_m (int): Metavariable for the LP.
        timesteps (int): Meta variable for the LP, big enough to cover largest makespan.

    Returns:
        LPInstance: The LP instance object.
    """
    # Set up input params
    job_capacities = {str(idx + 1): job.num_qubits for idx, job in enumerate(base_jobs)}
    job_capacities = {"0": 0} | job_capacities

    machine_capacities = accelerators

    lp_instance = _define_lp(
        job_capacities, machine_capacities, list(range(timesteps)), big_m
    )
    lp_instance.named_circuits = [JobHelper("0", None)] + [
        JobHelper(str(idx + 1), job) for idx, job in enumerate(base_jobs)
    ]
    return lp_instance

def _define_lp(
    job_capacities: dict[str, int],
    machine_capacities: dict[str, int],
    timesteps: list[int],
    big_m: int,
) -> LPInstance:
    jobs = list(job_capacities.keys())
    # print("Jobs in define_lp:")
    # print(jobs)
    machines = list(machine_capacities.keys())
    x_ik = pulp.LpVariable.dicts("x_ik", (jobs, machines), cat="Binary")                # Binary variable indicating whether job job is assigned to machine
    z_ikt = pulp.LpVariable.dicts("z_ikt", (jobs, machines, timesteps), cat="Binary")   # Binary variable indicating whether job job is assigned to machine at timestep t

    c_j = pulp.LpVariable.dicts("c_j", (jobs), 0, cat="Continuous")                     # Completion time of job
    s_j = pulp.LpVariable.dicts("s_j", (jobs), 0, cat="Continuous")                     # Start time of job
    c_max = pulp.LpVariable("makespan", 0, cat="Continuous")                            # Makespan of the schedule

    problem = pulp.LpProblem("Scheduling", pulp.LpMinimize)
    # set up problem constraints
    problem += pulp.lpSum(c_max)                                                        # (OBJ)
    problem += c_j["0"] == 0                                                            # (C2)
    for job in jobs[1:]:
        problem += c_j[job] <= c_max                                                    # (C1)
        problem += pulp.lpSum(x_ik[job][machine] for machine in machines) == 1          # (C3)
        
        problem += c_j[job] - s_j[job] + 1 == pulp.lpSum(                               # (C7)
            z_ikt[job][machine][timestep]
            for timestep in timesteps
            for machine in machines
        )
        for machine in machines:
            problem += (                                                                 # (C8)
                pulp.lpSum(z_ikt[job][machine][timestep] for timestep in timesteps)
                <= x_ik[job][machine] * big_m
            )

        for timestep in timesteps:
            problem += (                                                                # (C9)
                pulp.lpSum(z_ikt[job][machine][timestep] for machine in machines)
                * timestep
                <= c_j[job]
            )
            problem += (
                pulp.lpSum(z_ikt[job][machine][timestep] for machine in machines) <= 1  # (C4)
            )
            problem += s_j[job] <= pulp.lpSum(                                          # (C10)
                z_ikt[job][machine][timestep] for machine in machines
            ) * timestep + big_m * (
                1 - pulp.lpSum(z_ikt[job][machine][timestep] for machine in machines)
            )
    for timestep in timesteps:
        for machine in machines:
            problem += (                                                                # (C11)
                pulp.lpSum(
                    z_ikt[job][machine][timestep] * job_capacities[job]
                    for job in jobs[1:]
                )
                <= machine_capacities[machine]
            )
    return LPInstance(
        problem=problem,
        jobs=jobs,
        machines=machines,
        x_ik=x_ik,
        z_ikt=z_ikt,
        c_j=c_j,
        s_j=s_j,
        named_circuits=[],
    )
    
def _generate_schedule_info(
    problem: InfoProblem,
    schedule_type: SchedulerType,
) -> tuple[float, list[JobResultInfo], LPInstance | None]:
    """Generates the schedule for the given problem and schedule type.

    Calculates the true makespan by 'executing' the schedlue.
    Args:
        problem (InfoProblem): The full problem definition.
        schedule_type (SchedulerType): The type of schedule to use.

    Returns:
        tuple[float, list[JobResultInfo]]: The makespan and the list of jobs with their
            assigned machine and start and completion times.
    """

    lp_instance = set_up_base_lp(
        problem.base_jobs, problem.accelerators, problem.big_m, problem.timesteps
    )
    # # show jobs 
    # print("Jobs:")
    # for job in problem.base_jobs:
    #     print(job.num_qubits)
    
    if schedule_type == SchedulerType.EXTENDED:
        lp_instance = set_up_extended_lp(
            lp_instance=lp_instance,
            process_times=problem.process_times,
            setup_times=problem.setup_times,
        )

    lp_instance = solve_lp(lp_instance)
    _, jobs = extract_info_schedule(lp_instance)
    makespan = calculate_makespan(
        lp_instance, jobs, problem.process_times, problem.setup_times
    )

    return makespan, jobs, lp_instance

def calculate_makespan(
    lp_instance: LPInstance,
    jobs: list[JobResultInfo],
    process_times: PTimes,
    setup_times: STimes,
) -> float:
    """Calculates the actual makespan from the list of results.

    Executes the schedule with the corret p_ij and s_ij values.

    Args:
        lp_instance (LPInstance): The base LP instance.
        jobs (list[JobResultInfo]): The list of job results.
        process_times (PTimes): The correct  p_ij.
        setup_times (STimes) The correct s_ij.

    Returns:
        float: The makespan of the schedule.
    """
    return _calc_makespan(
        jobs,
        process_times,
        setup_times,
        lp_instance.jobs,
        lp_instance.machines,
    )

def _calc_makespan(
    jobs: list[JobResultInfo],
    process_times: PTimes,
    setup_times: STimes,
    job_names: list[str],
    machines: list[str],
    for_bin: bool = False,
) -> float:
    s_times = pulp.makeDict(
        [job_names, job_names, machines],
        setup_times,
        0,
    )
    p_times = pulp.makeDict(
        [job_names[1:], machines],
        process_times,
        0,
    )

    assigned_machines: defaultdict[str, list[JobResultInfo]] = defaultdict(list)
    for job in jobs:
        assigned_machines[job.machine].append(job)
    makespans = []
    for machine, assigned_jobs in assigned_machines.items():
        assigned_jobs_copy = deepcopy(assigned_jobs)
        for job in sorted(assigned_jobs, key=lambda x: x.start_time):
            # Find the last predecessor that is completed before the job starts
            # this can technically change the correct predecessor to a wrong one
            # because completion times are updated in the loop
            # I'm not sure if copying before the loop corrects this
            if for_bin:
                last_completed = max(
                    (job for job in assigned_jobs), key=lambda x: x.completion_time
                )
                if job.start_time == 0.0:
                    last_completed = JobResultInfo("0", machine, 0.0, 0.0, 0)
                job.start_time = last_completed.completion_time
            else:
                last_completed = _find_last_completed(
                    job.name, assigned_jobs_copy, machine
                )
                if job.start_time == 0.0:
                    last_completed = JobResultInfo("0", machine, 0.0, 0.0, 0)
                job.start_time = next(
                    (
                        j.completion_time
                        for j in assigned_jobs
                        if last_completed.name == j.name
                    ),
                    0.0,
                )
            # calculate p_j + s_ij
            job.completion_time = (  # check if this order is correct
                last_completed.completion_time
                + p_times[job.name][machine]
                + s_times[last_completed.name][job.name][machine]
            )
        makespans.append(max(job.completion_time for job in assigned_jobs))

    return max(makespans)

def _find_last_completed(
    job_name: str, jobs: list[JobResultInfo], machine: str
) -> JobResultInfo:
    """Finds the last completed job before the given job from the original schedule."""
    for job in jobs:
        if job.name == job_name:
            original_starttime = job.start_time
            break
    else:
        raise ValueError(f"Job {job_name} not found in {jobs}")
    completed_before = [j for j in jobs if j.completion_time <= original_starttime]
    if len(completed_before) == 0:
        return JobResultInfo("0", machine, 0.0, 0.0, 0)

    return max(completed_before, key=lambda x: x.completion_time)

def _calculate_exmaple_process_times(job_i, machine_k) -> float:
    if job_i == 0:
        return 0
    return job_i + np.random.randint(-2, 3) + machine_k

def _calculate_example_setup_times(job_i, job_j_, machine_k) -> float:
    if job_j_ == 0:
        return 0
    return (job_i + job_j_) // 2 + np.random.randint(-2, 3) + machine_k

def _generate_problem(big_m: int, timesteps: int, jobs: list, job_capacities: dict, machines: list, machine_capacities: dict) -> tuple[InfoProblem, dict[str, int]]:
    # Inputs
    processing_times = [
        [
            _calculate_exmaple_process_times(
                job_capacities[job], machine_capacities[machine]
            )
            for machine in machines
        ]
        for job in jobs
    ]
    setup_times = [
        [
            [
                50  # BIG!
                if job_i in [job_j, "0"]
                else _calculate_example_setup_times(
                    job_capacities[job_i],
                    job_capacities[job_j],
                    machine_capacities[machine],
                )
                for machine in machines
            ]
            for job_i in jobs
        ]
        for job_j in jobs
    ]
    del job_capacities["0"]
    # Print the processing and setup times
    # for i in range(len(jobs)):
    #     print(f"Processing times for {jobs[i]}: {processing_times[i]}")
    # for i in range(len(jobs)):
    #     for j in range(len(jobs)):
    #         print(f"Setup times for {jobs[i]} and {jobs[j]}: {setup_times[i][j]}")
    return (
        InfoProblem(
            base_jobs=[QuantumCircuit(cap) for cap in job_capacities.values()],
            accelerators=machine_capacities,
            big_m=big_m,
            timesteps=timesteps,
            process_times=processing_times,
            setup_times=setup_times,
        ),
        job_capacities,
    )

def set_up_extended_lp(
    lp_instance: LPInstance,
    process_times: PTimes,
    setup_times: STimes,
    big_m: int = 1000,
) -> LPInstance:
    """Sets up the LP for the extended scheduling problem.

    This uses the complex successor relationship.

    Args:
        lp_instance (LPInstance): The base LP.
        process_times (PTimes): Original process times.
        setup_times (STimes): Original setup times.
        big_m (int, optional): Metavariable for the LP. Defaults to 1000.

    Returns:
        LPInstance: The updated LP instance.
    """
    # List of jobs
    # Compare lenght job with machines
    # Print the jobs
    # print("Jobs in set_up_extended_lp:")
    # for job in lp_instance.jobs:
    #     print(job)
    # # Print the machines
    # print("Machines in set_up_extended_lp:")
    # for machine in lp_instance.machines:
    #     print(machine)
    # # Print the process times
    # print("Process times:")
    # print(process_times)
    p_times = pulp.makeDict(
        [lp_instance.jobs[1:], lp_instance.machines],
        process_times[1:],
        0,
    )
    # Print the process times
    # print("Process times:")
    # print(p_times)
    s_times = pulp.makeDict(
        [lp_instance.jobs, lp_instance.jobs, lp_instance.machines],
        setup_times,
        0,
    )
    # Print the setup times
    # for job_i in lp_instance.jobs:
    #     for job_j in lp_instance.jobs:
    #         for machine in lp_instance.machines:
    #             print(f"Setup time for job {job_i} on job {job_j} on machine {machine}: {s_times[job_i][job_j][machine]}")
    # decision variables
    y_ijk = pulp.LpVariable.dicts(
        "y_ijk",
        (lp_instance.jobs, lp_instance.jobs, lp_instance.machines),
        cat="Binary",
    )
    a_ij = pulp.LpVariable.dicts(
        "a_ij", (lp_instance.jobs, lp_instance.jobs), cat="Binary"
    )  # a: Job i ends before job j starts
    b_ij = pulp.LpVariable.dicts(
        "b_ij", (lp_instance.jobs, lp_instance.jobs), cat="Binary"
    )  # b: Job i ends before job j ends
    d_ijk = pulp.LpVariable.dicts(
        "d_ijk",
        (lp_instance.jobs, lp_instance.jobs, lp_instance.machines),
        cat="Binary",
    )  # d: Job i and  j run on the same machine
    e_ijlk = pulp.LpVariable.dicts(
        "e_ijlk",
        (lp_instance.jobs, lp_instance.jobs, lp_instance.jobs, lp_instance.machines),
        cat="Binary",
    )

    for job in lp_instance.jobs[1:]:
        lp_instance.problem += (                                                        # 
            pulp.lpSum(                                 # (Constraint 12)
                y_ijk[job_j][job][machine]
                for machine in lp_instance.machines
                for job_j in lp_instance.jobs
            )
            >= 1  # each job has a predecessor
        )
        lp_instance.problem += lp_instance.c_j[job] >= lp_instance.s_j[  # (Constrait 5)
            job
        ] + pulp.lpSum(
            lp_instance.x_ik[job][machine] * p_times[job][machine]
            for machine in lp_instance.machines
        ) + pulp.lpSum(
            y_ijk[job_j][job][machine] * s_times[job_j][job][machine]
            for machine in lp_instance.machines
            for job_j in lp_instance.jobs
        )
        for machine in lp_instance.machines:
            lp_instance.problem += (  # prec                         # (Constraint 13)
                lp_instance.x_ik[job][machine]
                >= pulp.lpSum(y_ijk[job_j][job][machine] for job_j in lp_instance.jobs)
                / big_m
            )
            lp_instance.problem += (  # Sucesssor                         # (Constraint 14)
                lp_instance.x_ik[job][machine]
                >= pulp.lpSum(y_ijk[job][job_j][machine] for job_j in lp_instance.jobs)
                / big_m
            )
            lp_instance.problem += (                                                                # (Constraint 15)
                lp_instance.z_ikt[job][machine][0] == y_ijk["0"][job][machine]
            )
                                                                 
        for job_j in lp_instance.jobs:
            lp_instance.problem += (                                                            # (Constraint 6)
                lp_instance.c_j[job_j]
                + (
                    pulp.lpSum(
                        y_ijk[job_j][job][machine] for machine in lp_instance.machines
                    )
                    - 1
                )
                * big_m
                <= lp_instance.s_j[job]
            )

    # Extended constraints
    for job in lp_instance.jobs[1:]:
        for job_j in lp_instance.jobs[1:]:
            if job == job_j:
                lp_instance.problem += a_ij[job][job_j] == 0
                lp_instance.problem += b_ij[job][job_j] == 0
                continue
            lp_instance.problem += (
                a_ij[job][job_j]
                >= (lp_instance.s_j[job_j] - lp_instance.c_j[job]) / big_m          # (Constraint 16)
            )
            lp_instance.problem += (
                b_ij[job][job_j]
                >= (lp_instance.c_j[job_j] - lp_instance.c_j[job]) / big_m          # (Constraint 17)
            )
            for machine in lp_instance.machines:
                lp_instance.problem += (                                # (Constraint 18)
                    d_ijk[job][job_j][machine]
                    >= lp_instance.x_ik[job][machine]
                    + lp_instance.x_ik[job_j][machine]
                    - 1
                )
                for job_l in lp_instance.jobs[1:]:                      # (Constraint 19)
                    lp_instance.problem += (
                        e_ijlk[job][job_j][job_l][machine]
                        >= b_ij[job][job_l]
                        + a_ij[job_l][job_j]
                        + d_ijk[job][job_j][machine]
                        + d_ijk[job][job_l][machine]
                        - 3
                    )

    for job in lp_instance.jobs[1:]:
        for job_j in lp_instance.jobs[1:]:
            for machine in lp_instance.machines:
                lp_instance.problem += (                            # (Constraint 20)
                    y_ijk[job][job_j][machine]
                    >= a_ij[job][job_j]
                    + (
                        pulp.lpSum(
                            e_ijlk[job][job_j][job_l][machine]
                            for job_l in lp_instance.jobs[1:]
                        )
                        / big_m
                    )
                    + d_ijk[job][job_j][machine]
                    - 2
                )
    return lp_instance

def solve_lp(lp_instance: LPInstance) -> LPInstance:
    """Solves a LP using gurobi.

    Args:
        lp_instance (LPInstance): The input LP instance.

    Returns:
        lp_instance (LPInstance): The LP instance with the solved problem object..
    """
    solver_list = pulp.listSolvers(onlyAvailable=True)
    gurobi = "GUROBI_CMD"
    if gurobi in solver_list:
        solver = pulp.getSolver(gurobi)
        lp_instance.problem.solve(solver)
    else:
        lp_instance.problem.solve()
    return lp_instance

def extract_info_schedule(
    lp_instance: LPInstance,
) -> tuple[float, list[JobResultInfo]]:
    """Extracts a schedule for evaluation purposes.

    Args:
        lp_instance (LPInstance): A solved LP instance.

    Returns:
        tuple[float, list[JobResultInfo]]: The objective value and the list of jobs with their
            with their assigned machine and start and completion times.
    """
    # TODO check if _first_name_func is needed once we change to uuids
    assigned_jobs = _extract_gurobi_results(lp_instance, _first_name_func)
    return lp_instance.problem.objective.value(), list(assigned_jobs.values())

def _first_name_func(name: str) -> tuple[str, str]:
    # For single character jobs
    names = name.split("_")[2:]
    return names[0], names[1]

def _extract_gurobi_results(
    lp_instance: LPInstance, name_function: Callable[[str], tuple[str, str]]
) -> dict[str, JobResultInfo]:
    assigned_jobs = {
        job.name: JobResultInfo(
            name=job.name,
            machine="",
            start_time=-1.0,
            completion_time=-1.0,
            capacity=job.circuit.num_qubits,
        )
        if job.circuit is not None
        else JobResultInfo(
            name=job.name,
            machine="",
            start_time=-1.0,
            completion_time=-1.0,
            capacity=0,
        )
        for job in lp_instance.named_circuits
    }
    for var in lp_instance.problem.variables():
        if var.name.startswith("x_") and var.varValue > 0.0:
            names = name_function(var.name)
            assigned_jobs[names[0]].machine = names[1]
        elif var.name.startswith("s_"):
            name = "-".join(var.name.split("_")[2:])
            assigned_jobs[name].start_time = float(var.varValue)
        elif var.name.startswith("c_"):
            name = "-".join(var.name.split("_")[2:])
            # TODO for some reason this was name[0] before
            assigned_jobs[name].completion_time = float(var.varValue)
    del assigned_jobs["0"]
    return assigned_jobs

def example_problem(big_m: int, timesteps: int, filename: str = "scheduling", jobs: list = None, job_capacities: dict = None, machines: list = None, machine_capacities: dict = None):
    """Runs the example problem and saves the LP file and JSON file.
    TODO should also run the solution explorer and produce the output pdf.

    Args:
        big_m (int): LP metavariable.
        timesteps (int): LP metavariable.
        filename (str, optional): Filename for .lp, .json and .pdf. Defaults to "scheduling".
    """
    _problem, job_capacities = _generate_problem(big_m, timesteps, jobs, job_capacities, machines, machine_capacities)
    _, _, lp_instance = generate_schedule(_problem, SchedulerType.EXTENDED)
    
    
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