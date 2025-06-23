import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
import numpy as np

def visualize_data(data, save_path="quantum_schedule.pdf"):
    """
    Enhanced visualization of job schedule as a Gantt chart with detailed information.

    Args:
        data (list): A list of dictionaries containing job information.
                     Each dictionary should have keys: 'job', 'qubits', 'machine',
                     'capacity', 'start', 'end', and 'duration'.
        save_path (str): Path to save the PDF file (default: "quantum_schedule.pdf").
    """
    # Normalize time for better visualization
    for job in data:
        job['start'] /= 10
        job['end'] /= 10
        job['duration'] /= 10

    # Sort jobs by job ID for vertical order
    data.sort(key=lambda x: x['job'])

    # Create enhanced figure with better proportions for larger text
    fig, ax = plt.subplots(figsize=(16, 12))  # Increased from (14, 10) to (16, 12)
    
    # Set professional style
    plt.style.use('default')
    fig.patch.set_facecolor('white')
    ax.set_facecolor('#f8f9fa')

    # Enhanced color palette with gradients
    colors = {
        'fake_belem': '#2E86AB',      # Ocean Blue
        'fake_manila': '#A23B72',     # Plum Purple  
        'fake_santiago': '#F18F01',   # Orange
        'fake_casablanca': '#C73E1D', # Red
        'fake_athens': '#6A994E',     # Green
        'fake_kolkata': '#7209B7',    # Purple
        'fake_montreal': '#FF6B6B',   # Light Red
        'fake_toronto': '#4ECDC4'     # Teal
    }

    # Get unique machines and their capacities (simplified)
    machines = {}
    for job in data:
        machines[job['machine']] = job['capacity']

    # Add jobs to the Gantt chart with qubit info in Y-axis labels
    y_positions = []
    y_labels = []
    
    for i, job in enumerate(data):
        y_pos = i
        y_positions.append(y_pos)
        
        # Y-axis label with job name and qubit count
        y_label = f"Job {job['job']} ({job['qubits']}q)"
        y_labels.append(y_label)
        
        color = colors.get(job['machine'], '#6c757d')
        
        # Create main bar with thinner height but still adjacent
        bar = ax.barh(
            y=y_pos,
            width=job['duration'], 
            left=job['start'], 
            color=color,
            edgecolor='white',
            linewidth=1.5,
            alpha=0.85,
            height=0.9  # Set to 0.9 for thinner bars that are still adjacent
        )
        
        # Add shadow effect with matching height
        ax.barh(
            y=y_pos - 0.05,
            width=job['duration'], 
            left=job['start'], 
            color='black',
            alpha=0.1,
            height=0.9,  # Set to 0.9 to match main bar - thinner but adjacent
            zorder=0
        )
        
        # Add job name and qubit count on the bar
        if job['duration'] > 0:
            bar_center_x = job['start'] + job['duration'] / 2
            bar_center_y = y_pos
            
            # Job identifier with qubit count - large and clear
            ax.text(
                bar_center_x, bar_center_y,
                f"J{job['job']} ({job['qubits']}q)",
                ha='center', va='center',
                fontsize=18, fontweight='bold',  # Slightly smaller to fit both job and qubit info
                color='white', zorder=10
            )

    # Simplified legend positioned inside the chart
    patches = []
    for machine, capacity in machines.items():
        machine_name = machine.replace('fake_', '').title()
        color = colors.get(machine, '#6c757d')
        
        # Simplified legend label without utilization
        label = f'{machine_name} ({capacity}q)'
        patches.append(mpatches.Patch(color=color, label=label))

    # Position legend outside the chart to avoid overlapping with bars
    legend = ax.legend(
        handles=patches, 
        bbox_to_anchor=(1.02, 1),
        loc='upper left',
        framealpha=0.95,
        fancybox=True,
        shadow=True,
        borderpad=1,
        fontsize=12,  # Increased from 9 to 12
        title="Quantum Machines",
        title_fontsize=14  # Increased from 10 to 14
    )
    legend.get_frame().set_facecolor('#ffffff')
    legend.get_frame().set_edgecolor('#dee2e6')

    # Enhanced axes customization
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=12)  # Increased from 9 to 12
    ax.invert_yaxis()

    # Simplified labels and title
    total_qubits = sum(job['qubits'] for job in data)
    makespan = max(job['end'] for job in data) if data else 0
    
    ax.set_xlabel('Time (time units) [normalized]', fontweight='bold', fontsize=14)  # Increased from 12 to 14
    ax.set_ylabel('Scheduled Jobs', fontweight='bold', fontsize=14)  # Increased from 12 to 14
    
    # Increase tick label font sizes
    ax.tick_params(axis='x', labelsize=12)  # X-axis numbers
    ax.tick_params(axis='y', labelsize=12)  # Y-axis labels (already set above but ensuring consistency)
    
    # Simplified title
    title_line1 = 'Quantum Job Scheduling Gantt Chart'
    # title_line2 = f'{len(data)} jobs • {len(machines)} machines • {total_qubits} total qubits'
    # title_line3 = f'Makespan: {makespan:.1f}'
    
    ax.set_title(f'{title_line1}', 
                fontweight='bold', fontsize=16, pad=25)  # Increased from 14 to 16

    # Simplified grid system
    ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5, color='#dee2e6')
    ax.set_axisbelow(True)

    # Set axis limits with padding
    if data:
        max_time = max(job['end'] for job in data)
        ax.set_xlim(-max_time * 0.02, max_time * 1.02)
        ax.set_ylim(-0.5, len(data) - 0.5)

    # Enhanced layout
    plt.tight_layout()

    # Save as high-quality PDF
    save_path = Path(save_path)
    if not save_path.suffix.lower() == '.pdf':
        save_path = save_path.with_suffix('.pdf')
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    # fig.savefig(save_path, dpi=300, bbox_inches='tight', format='pdf', 
    #             facecolor='white', edgecolor='none')
    print(f"📊 Minimal Gantt chart saved to {save_path}")
    print(f"   ✓ {len(data)} jobs visualized across {len(machines)} machines")
    print(f"   ✓ Total qubits: {total_qubits}, Makespan: {makespan:.1f}")

    # Show the plot
    plt.show()