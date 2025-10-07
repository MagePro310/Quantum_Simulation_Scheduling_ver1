import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_data(data):
    """
    Visualize the job schedule as a Gantt chart.

    Args:
        data (list): A list of dictionaries containing job information.
                     Each dictionary should have keys: 'job', 'qubits', 'machine',
                     'capacity', 'start', 'end', and 'duration'.
    """
    # Normalize time for better visualization

    # Sort jobs by job ID for vertical order
    data.sort(key=lambda x: x['job'])

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Colors for each machine
    colors = {
        'fake_belem': 'steelblue',
        'fake_manila': 'lightblue'
    }

    # Creating patches for legend
    patches = [
        mpatches.Patch(color='steelblue', label='fake_belem (5 qubits)'),
        mpatches.Patch(color='lightblue', label='fake_manila (5 qubits)')
    ]

    # Add jobs to the Gantt chart
    for job in data:
        ax.barh(
            y=f"{job['job']} ({job['qubits']})", 
            width=job['duration'], 
            left=job['start'], 
            color=colors[job['machine']], 
            edgecolor='black'
        )

    # Reverse the y-axis
    ax.invert_yaxis()

    # Add legend with larger font
    ax.legend(handles=patches, loc='upper right', fontsize=12)

    # Labels and title with larger fonts
    ax.set_xlabel("Time", fontsize=14)
    ax.set_ylabel("Jobs (Qubits)", fontsize=14)
    ax.set_title("Gantt Chart of Jobs on Quantum Machines", fontsize=16)

    # Increase tick label font size
    ax.tick_params(axis='both', which='major', labelsize=12)

    # Grid and layout adjustments
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Show plot
    # print("Gantt chart saved as img/FFD_schedule_estimated.pdf")
    # plt.savefig("img/FFD_schedule_estimated.pdf")

    print("Gantt chart saved as img/FFD_schedule_simulation.pdf")
    plt.savefig("img/FFD_schedule_simulation.pdf")

    # print("Gantt chart saved as img/MILQ_schedule_simulation.pdf")
    # plt.savefig("img/MILQ_schedule_simulation.pdf")

    # print("Gantt chart saved as img/MILQ_schedule_estimated.pdf")
    # plt.savefig("img/MILQ_schedule_estimated.pdf")
    plt.show()