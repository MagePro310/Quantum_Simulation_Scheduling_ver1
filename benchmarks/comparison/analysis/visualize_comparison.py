#!/usr/bin/env python3
"""
Visualization tool for comparing quantum scheduling algorithm results.
Reads JSON result files and generates comparison charts.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


class AlgorithmVisualizer:
    """Visualize and compare results from multiple scheduling algorithms."""
    
    def __init__(self, results_dir: str = None):
        """
        Initialize visualizer.
        
        Args:
            results_dir: Path to results directory containing algorithm subdirectories
        """
        if results_dir is None:
            # Default to benchmarks/comparison/results
            current_dir = Path(__file__).parent.parent
            results_dir = current_dir / "results"
        
        self.results_dir = Path(results_dir)
        self.algorithms = ['FFD', 'MTMC', 'MILQ_extend', 'NoTaDS']
        self.colors = {
            'FFD': '#2E86AB',
            'MTMC': '#A23B72',
            'MILQ_extend': '#F18F01',
            'NoTaDS': '#C73E1D'
        }
        
        # Metrics to compare
        self.metrics = [
            'makespan',
            'average_turnaroundTime',
            'average_responseTime',
            'average_utilization',
            'average_throughput',
            'average_fidelity',
            'sampling_overhead',
            'scheduler_latency'
        ]
        
        self.metric_labels = {
            'makespan': 'Makespan (time units)',
            'average_turnaroundTime': 'Avg Turnaround Time',
            'average_responseTime': 'Avg Response Time',
            'average_utilization': 'Avg Utilization (%)',
            'average_throughput': 'Avg Throughput',
            'average_fidelity': 'Avg Fidelity',
            'sampling_overhead': 'Sampling Overhead',
            'scheduler_latency': 'Scheduler Latency (s)'
        }
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
    
    def load_algorithm_results(self, algorithm: str) -> Dict[str, Any]:
        """
        Load results for a specific algorithm.
        
        Args:
            algorithm: Algorithm name (FFD, MTMC, MILQ_extend, NoTaDS)
            
        Returns:
            Dictionary containing schedule and metrics data
        """
        algo_dir = self.results_dir / algorithm
        
        results = {
            'schedule': [],
            'metrics': {},
            'algorithm': algorithm
        }
        
        # Load schedule.json
        schedule_file = algo_dir / 'schedule.json'
        if schedule_file.exists():
            with open(schedule_file, 'r') as f:
                results['schedule'] = json.load(f)
        
        # Load metrics from result files (if they exist)
        for result_file in algo_dir.glob('result_*.json'):
            with open(result_file, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    results['metrics'].update(data)
        
        # Calculate metrics from schedule if not provided
        if not results['metrics'] and results['schedule']:
            results['metrics'] = self._calculate_metrics_from_schedule(results['schedule'])
        
        return results
    
    def _calculate_metrics_from_schedule(self, schedule: List[Dict]) -> Dict[str, float]:
        """Calculate basic metrics from schedule data."""
        if not schedule:
            return {}
        
        metrics = {}
        
        # Makespan: max end time
        metrics['makespan'] = max(job['end'] for job in schedule)
        
        # Average turnaround time (assuming jobs start at submission time 0)
        metrics['average_turnaroundTime'] = np.mean([job['end'] for job in schedule])
        
        # Average response time (start - submission)
        metrics['average_responseTime'] = np.mean([job['start'] for job in schedule])
        
        # Calculate utilization
        total_time = metrics['makespan']
        total_capacity = len(set(job['machine'] for job in schedule)) * max(job['capacity'] for job in schedule)
        total_used = sum(job['duration'] * job['qubits'] for job in schedule)
        metrics['average_utilization'] = (total_used / (total_capacity * total_time)) * 100 if total_time > 0 else 0
        
        # Throughput: jobs per time unit
        metrics['average_throughput'] = len(schedule) / metrics['makespan'] if metrics['makespan'] > 0 else 0
        
        # Default values for metrics not in schedule
        metrics['average_fidelity'] = 0.95  # Placeholder
        metrics['sampling_overhead'] = 1.0  # Placeholder
        metrics['scheduler_latency'] = 0.0  # Placeholder
        
        return metrics
    
    def load_all_results(self) -> Dict[str, Dict]:
        """Load results for all algorithms."""
        all_results = {}
        
        print("=" * 70)
        print("📊 LOADING ALGORITHM RESULTS")
        print("=" * 70)
        
        for algo in self.algorithms:
            print(f"\n[LOAD] Loading {algo}...")
            try:
                results = self.load_algorithm_results(algo)
                all_results[algo] = results
                print(f"  ✓ Jobs scheduled: {len(results['schedule'])}")
                print(f"  ✓ Metrics loaded: {len(results['metrics'])}")
            except Exception as e:
                print(f"  ✗ Error loading {algo}: {e}")
                all_results[algo] = {'schedule': [], 'metrics': {}, 'algorithm': algo}
        
        print("\n" + "=" * 70)
        return all_results
    
    def plot_metrics_comparison_bar(self, all_results: Dict[str, Dict], output_file: str = None):
        """Create bar chart comparing all metrics across algorithms."""
        print("\n📊 Generating metrics comparison bar chart...")
        
        fig, axes = plt.subplots(2, 4, figsize=(20, 10))
        axes = axes.flatten()
        
        for idx, metric in enumerate(self.metrics):
            ax = axes[idx]
            
            # Collect data for this metric
            algorithms = []
            values = []
            colors = []
            
            for algo in self.algorithms:
                if algo in all_results and metric in all_results[algo]['metrics']:
                    algorithms.append(algo)
                    values.append(all_results[algo]['metrics'][metric])
                    colors.append(self.colors[algo])
            
            if values:
                bars = ax.bar(algorithms, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
                
                # Add value labels on bars
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height:.2f}',
                           ha='center', va='bottom', fontsize=9, fontweight='bold')
                
                ax.set_ylabel(self.metric_labels[metric], fontweight='bold')
                ax.set_title(f'{self.metric_labels[metric]}', fontsize=12, fontweight='bold')
                ax.grid(axis='y', alpha=0.3)
                
                # Rotate x labels if needed
                ax.set_xticklabels(algorithms, rotation=45, ha='right')
        
        plt.suptitle('Algorithm Performance Comparison - All Metrics', 
                    fontsize=16, fontweight='bold', y=0.995)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved to: {output_file}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_makespan_comparison(self, all_results: Dict[str, Dict], output_file: str = None):
        """Create detailed makespan comparison chart."""
        print("\n📊 Generating makespan comparison chart...")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Bar chart
        algorithms = []
        makespans = []
        colors_list = []
        
        for algo in self.algorithms:
            if algo in all_results and 'makespan' in all_results[algo]['metrics']:
                algorithms.append(algo)
                makespans.append(all_results[algo]['metrics']['makespan'])
                colors_list.append(self.colors[algo])
        
        if makespans:
            bars = ax1.bar(algorithms, makespans, color=colors_list, alpha=0.8, 
                          edgecolor='black', linewidth=2)
            
            # Add value labels
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f}',
                        ha='center', va='bottom', fontsize=12, fontweight='bold')
            
            ax1.set_ylabel('Makespan (time units)', fontsize=12, fontweight='bold')
            ax1.set_title('Makespan Comparison', fontsize=14, fontweight='bold')
            ax1.grid(axis='y', alpha=0.3)
            ax1.set_xticklabels(algorithms, rotation=45, ha='right')
            
            # Percentage difference from best
            min_makespan = min(makespans)
            percentages = [((m - min_makespan) / min_makespan * 100) for m in makespans]
            
            bars2 = ax2.bar(algorithms, percentages, color=colors_list, alpha=0.8,
                           edgecolor='black', linewidth=2)
            
            for bar in bars2:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'+{height:.1f}%',
                        ha='center', va='bottom', fontsize=12, fontweight='bold')
            
            ax2.set_ylabel('% Difference from Best', fontsize=12, fontweight='bold')
            ax2.set_title('Makespan - Relative Performance', fontsize=14, fontweight='bold')
            ax2.grid(axis='y', alpha=0.3)
            ax2.axhline(y=0, color='green', linestyle='--', linewidth=2, alpha=0.5)
            ax2.set_xticklabels(algorithms, rotation=45, ha='right')
        
        plt.suptitle('Makespan Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved to: {output_file}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_utilization_fidelity(self, all_results: Dict[str, Dict], output_file: str = None):
        """Create scatter plot for utilization vs fidelity."""
        print("\n📊 Generating utilization vs fidelity scatter plot...")
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        for algo in self.algorithms:
            if algo in all_results:
                metrics = all_results[algo]['metrics']
                if 'average_utilization' in metrics and 'average_fidelity' in metrics:
                    util = metrics['average_utilization']
                    fidelity = metrics['average_fidelity']
                    
                    ax.scatter(util, fidelity, s=300, c=self.colors[algo], 
                             alpha=0.7, edgecolors='black', linewidth=2, label=algo)
                    
                    # Add algorithm label
                    ax.annotate(algo, (util, fidelity), 
                              xytext=(10, 10), textcoords='offset points',
                              fontsize=11, fontweight='bold')
        
        ax.set_xlabel('Average Utilization (%)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Average Fidelity', fontsize=12, fontweight='bold')
        ax.set_title('Utilization vs Fidelity Trade-off', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved to: {output_file}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_radar_chart(self, all_results: Dict[str, Dict], output_file: str = None):
        """Create radar chart comparing normalized metrics."""
        print("\n📊 Generating radar chart...")
        
        # Select key metrics for radar chart
        radar_metrics = [
            'makespan',
            'average_utilization',
            'average_fidelity',
            'average_throughput',
            'average_turnaroundTime'
        ]
        
        # Normalize metrics (0-1 scale, with direction consideration)
        normalized_data = {}
        
        for metric in radar_metrics:
            values = []
            for algo in self.algorithms:
                if algo in all_results and metric in all_results[algo]['metrics']:
                    values.append(all_results[algo]['metrics'][metric])
                else:
                    values.append(0)
            
            if max(values) > 0:
                # For metrics where lower is better (makespan, turnaround time)
                if metric in ['makespan', 'average_turnaroundTime', 'average_responseTime']:
                    # Invert: best (lowest) becomes 1, worst becomes 0
                    min_val = min(v for v in values if v > 0)
                    normalized = [min_val / v if v > 0 else 0 for v in values]
                else:
                    # For metrics where higher is better
                    max_val = max(values)
                    normalized = [v / max_val for v in values]
                
                for idx, algo in enumerate(self.algorithms):
                    if algo not in normalized_data:
                        normalized_data[algo] = []
                    normalized_data[algo].append(normalized[idx])
        
        # Create radar chart
        labels = ['Makespan\n(lower better)', 'Utilization', 'Fidelity', 
                 'Throughput', 'Turnaround\n(lower better)']
        num_vars = len(labels)
        
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]  # Complete the circle
        
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        for algo in self.algorithms:
            if algo in normalized_data:
                values = normalized_data[algo]
                values += values[:1]  # Complete the circle
                
                ax.plot(angles, values, 'o-', linewidth=2, label=algo, 
                       color=self.colors[algo])
                ax.fill(angles, values, alpha=0.15, color=self.colors[algo])
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=11)
        ax.set_ylim(0, 1)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=9)
        ax.grid(True)
        
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)
        plt.title('Algorithm Performance Radar Chart\n(Normalized Metrics)', 
                 fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved to: {output_file}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_gantt_chart(self, all_results: Dict[str, Dict], output_file: str = None):
        """Create Gantt chart showing job schedules for all algorithms."""
        print("\n📊 Generating Gantt chart...")
        
        num_algos = len([a for a in self.algorithms if a in all_results and all_results[a]['schedule']])
        
        if num_algos == 0:
            print("  ✗ No schedule data available for Gantt chart")
            return
        
        fig, axes = plt.subplots(num_algos, 1, figsize=(14, 4 * num_algos))
        
        if num_algos == 1:
            axes = [axes]
        
        algo_idx = 0
        for algo in self.algorithms:
            if algo not in all_results or not all_results[algo]['schedule']:
                continue
            
            ax = axes[algo_idx]
            schedule = all_results[algo]['schedule']
            
            # Get unique machines
            machines = sorted(set(job['machine'] for job in schedule))
            machine_to_y = {m: idx for idx, m in enumerate(machines)}
            
            # Plot jobs
            for job in schedule:
                y_pos = machine_to_y[job['machine']]
                start = job['start']
                duration = job['duration']
                
                # Color based on qubits (darker = more qubits)
                color_intensity = job['qubits'] / max(j['qubits'] for j in schedule)
                color = plt.cm.Blues(0.3 + 0.6 * color_intensity)
                
                ax.barh(y_pos, duration, left=start, height=0.6, 
                       color=color, edgecolor='black', linewidth=1)
                
                # Add job label
                ax.text(start + duration/2, y_pos, f"J{job['job']}\n{job['qubits']}q",
                       ha='center', va='center', fontsize=8, fontweight='bold')
            
            ax.set_yticks(range(len(machines)))
            ax.set_yticklabels(machines, fontsize=9)
            ax.set_xlabel('Time', fontsize=10, fontweight='bold')
            ax.set_ylabel('Machines', fontsize=10, fontweight='bold')
            ax.set_title(f'{algo} - Job Schedule (Makespan: {max(j["end"] for j in schedule):.1f})',
                        fontsize=12, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            
            algo_idx += 1
        
        plt.suptitle('Gantt Charts - Algorithm Comparison', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved to: {output_file}")
        else:
            plt.show()
        
        plt.close()
    
    def generate_summary_report(self, all_results: Dict[str, Dict], output_file: str = None):
        """Generate text summary report."""
        print("\n📊 Generating summary report...")
        
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("QUANTUM SCHEDULING ALGORITHM COMPARISON REPORT")
        report_lines.append("=" * 80)
        report_lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Results Directory: {self.results_dir}")
        report_lines.append("\n" + "-" * 80)
        
        for algo in self.algorithms:
            if algo not in all_results:
                continue
            
            report_lines.append(f"\n{algo} Algorithm:")
            report_lines.append("-" * 40)
            
            schedule = all_results[algo]['schedule']
            metrics = all_results[algo]['metrics']
            
            report_lines.append(f"  Jobs Scheduled: {len(schedule)}")
            
            if schedule:
                machines = set(job['machine'] for job in schedule)
                report_lines.append(f"  Machines Used: {len(machines)}")
                report_lines.append(f"  Machine List: {', '.join(sorted(machines))}")
            
            report_lines.append("\n  Metrics:")
            for metric in self.metrics:
                if metric in metrics:
                    value = metrics[metric]
                    label = self.metric_labels.get(metric, metric)
                    report_lines.append(f"    {label:.<45} {value:.4f}")
        
        # Best performer for each metric
        report_lines.append("\n" + "=" * 80)
        report_lines.append("BEST PERFORMERS BY METRIC")
        report_lines.append("=" * 80)
        
        for metric in self.metrics:
            values = {}
            for algo in self.algorithms:
                if algo in all_results and metric in all_results[algo]['metrics']:
                    values[algo] = all_results[algo]['metrics'][metric]
            
            if values:
                # Determine best based on metric type
                if metric in ['makespan', 'average_turnaroundTime', 'average_responseTime', 
                             'sampling_overhead', 'scheduler_latency']:
                    best_algo = min(values.items(), key=lambda x: x[1])
                else:
                    best_algo = max(values.items(), key=lambda x: x[1])
                
                label = self.metric_labels.get(metric, metric)
                report_lines.append(f"  {label:.<45} {best_algo[0]} ({best_algo[1]:.4f})")
        
        report_lines.append("\n" + "=" * 80)
        
        report_text = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f"  ✓ Saved to: {output_file}")
        
        print("\n" + report_text)
        
        return report_text
    
    def generate_all_visualizations(self, output_dir: str = None):
        """Generate all visualization charts and reports."""
        if output_dir is None:
            output_dir = self.results_dir.parent / "reports"
        
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Generate timestamp for file names
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        print("\n" + "=" * 70)
        print("🎨 GENERATING ALL VISUALIZATIONS")
        print("=" * 70)
        print(f"Output Directory: {output_dir}")
        
        # Load all results
        all_results = self.load_all_results()
        
        # Generate all charts
        self.plot_metrics_comparison_bar(
            all_results,
            output_dir / f'metrics_comparison_{timestamp}.png'
        )
        
        self.plot_makespan_comparison(
            all_results,
            output_dir / f'makespan_comparison_{timestamp}.png'
        )
        
        self.plot_utilization_fidelity(
            all_results,
            output_dir / f'utilization_fidelity_{timestamp}.png'
        )
        
        self.plot_radar_chart(
            all_results,
            output_dir / f'radar_chart_{timestamp}.png'
        )
        
        self.plot_gantt_chart(
            all_results,
            output_dir / f'gantt_chart_{timestamp}.png'
        )
        
        self.generate_summary_report(
            all_results,
            output_dir / f'summary_report_{timestamp}.txt'
        )
        
        print("\n" + "=" * 70)
        print("✅ ALL VISUALIZATIONS COMPLETED")
        print("=" * 70)
        print(f"\n📁 Results saved to: {output_dir}")
        print(f"\nGenerated files:")
        for file in sorted(output_dir.glob(f'*{timestamp}*')):
            print(f"  • {file.name}")


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Visualize and compare quantum scheduling algorithm results'
    )
    parser.add_argument(
        '--results-dir',
        type=str,
        help='Path to results directory (default: benchmarks/comparison/results)'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        help='Path to output directory for charts (default: benchmarks/comparison/reports)'
    )
    parser.add_argument(
        '--chart',
        type=str,
        choices=['all', 'metrics', 'makespan', 'scatter', 'radar', 'gantt', 'report'],
        default='all',
        help='Type of visualization to generate (default: all)'
    )
    
    args = parser.parse_args()
    
    # Create visualizer
    visualizer = AlgorithmVisualizer(results_dir=args.results_dir)
    
    # Load results
    all_results = visualizer.load_all_results()
    
    # Generate requested visualizations
    if args.chart == 'all':
        visualizer.generate_all_visualizations(output_dir=args.output_dir)
    else:
        output_dir = Path(args.output_dir) if args.output_dir else visualizer.results_dir.parent / "reports"
        output_dir.mkdir(exist_ok=True, parents=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if args.chart == 'metrics':
            visualizer.plot_metrics_comparison_bar(all_results, output_dir / f'metrics_{timestamp}.png')
        elif args.chart == 'makespan':
            visualizer.plot_makespan_comparison(all_results, output_dir / f'makespan_{timestamp}.png')
        elif args.chart == 'scatter':
            visualizer.plot_utilization_fidelity(all_results, output_dir / f'scatter_{timestamp}.png')
        elif args.chart == 'radar':
            visualizer.plot_radar_chart(all_results, output_dir / f'radar_{timestamp}.png')
        elif args.chart == 'gantt':
            visualizer.plot_gantt_chart(all_results, output_dir / f'gantt_{timestamp}.png')
        elif args.chart == 'report':
            visualizer.generate_summary_report(all_results, output_dir / f'report_{timestamp}.txt')


if __name__ == '__main__':
    main()
