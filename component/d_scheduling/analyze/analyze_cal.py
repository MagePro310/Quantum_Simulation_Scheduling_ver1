"""
Quantum Job Scheduling Analytics Module

This module provides comprehensive analytics and metrics calculation for quantum
job scheduling systems, including performance metrics like makespan, throughput,
utilization, and response times.

Author: Quantum Simulation Scheduling Team
Date: June 23, 2025
"""

import json
from collections import defaultdict
from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JobSchedulingAnalyzer:
    """
    A comprehensive analyzer for quantum job scheduling performance metrics.
    
    This class provides methods to calculate various scheduling metrics including
    makespan, throughput, utilization, turnaround time, and response time from
    job scheduling data.
    """
    
    @staticmethod
    def load_job_data(filepath: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        Load job scheduling data from a JSON file.
        
        Args:
            filepath (Union[str, Path]): Path to the JSON file containing job data.
            
        Returns:
            List[Dict[str, Any]]: List of job dictionaries with scheduling information.
            
        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
            ValueError: If the loaded data is not in the expected format.
            
        Example:
            >>> analyzer = JobSchedulingAnalyzer()
            >>> jobs = analyzer.load_job_data("scheduling_results.json")
            >>> print(f"Loaded {len(jobs)} jobs")
        """
        filepath = Path(filepath)
        
        if not filepath.exists():
            raise FileNotFoundError(f"Job data file not found: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {filepath}: {e}")
        
        if not isinstance(data, list):
            raise ValueError("Job data must be a list of job dictionaries")
        
        # Validate job data structure
        required_fields = {'job', 'qubits', 'machine', 'capacity', 'start', 'end', 'duration'}
        for i, job in enumerate(data):
            if not isinstance(job, dict):
                raise ValueError(f"Job {i} must be a dictionary")
            missing_fields = required_fields - set(job.keys())
            if missing_fields:
                raise ValueError(f"Job {i} missing required fields: {missing_fields}")
        
        logger.info(f"Successfully loaded {len(data)} jobs from {filepath}")
        return data
    
    @staticmethod
    def calculate_utilization_per_machine(job_data: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Calculate the resource utilization for each machine.
        
        Utilization is calculated as the ratio of actual resource usage to the
        maximum possible resource usage over the makespan period.
        
        Args:
            job_data (List[Dict[str, Any]]): List of job scheduling data.
            
        Returns:
            Dict[str, float]: Dictionary mapping machine names to their utilization rates.
            
        Raises:
            ValueError: If job_data is empty or contains invalid data.
            
        Example:
            >>> jobs = [
            ...     {'machine': 'qpu1', 'qubits': 2, 'duration': 100, 'capacity': 5, 'end': 150},
            ...     {'machine': 'qpu1', 'qubits': 3, 'duration': 80, 'capacity': 5, 'end': 120}
            ... ]
            >>> utilization = JobSchedulingAnalyzer.calculate_utilization_per_machine(jobs)
            >>> print(f"QPU1 utilization: {utilization['qpu1']:.2%}")
        """
        if not job_data:
            raise ValueError("Job data cannot be empty")
        
        utilization_per_machine = defaultdict(float)
        makespan_per_machine = defaultdict(float)
        machine_capacity = defaultdict(float)
        
        # Extract machine capacities and calculate makespan per machine
        for job in job_data:
            machine = job['machine']
            machine_capacity[machine] = job['capacity']
            makespan_per_machine[machine] = max(makespan_per_machine[machine], job['end'])
        
        # Calculate total resource usage per machine
        for job in job_data:
            machine = job['machine']
            resource_usage = job['qubits'] * job['duration']
            utilization_per_machine[machine] += resource_usage
        
        # Normalize by maximum possible resource usage
        for machine, total_usage in utilization_per_machine.items():
            max_possible_usage = makespan_per_machine[machine] * machine_capacity[machine]
            if max_possible_usage > 0:
                utilization_per_machine[machine] = total_usage / max_possible_usage
            else:
                utilization_per_machine[machine] = 0.0
        
        return dict(utilization_per_machine)
    
    @staticmethod
    def calculate_comprehensive_metrics(
        job_data: List[Dict[str, Any]], 
        utilization_per_machine: Optional[Dict[str, float]] = None
    ) -> Dict[str, float]:
        """
        Calculate comprehensive scheduling performance metrics.
        
        Args:
            job_data (List[Dict[str, Any]]): List of job scheduling data.
            utilization_per_machine (Optional[Dict[str, float]]): Pre-calculated 
                utilization per machine. If None, will be calculated automatically.
                
        Returns:
            Dict[str, float]: Dictionary containing various performance metrics:
                - average_turnaround_time: Average time from submission to completion
                - average_response_time: Average time from submission to start
                - makespan: Total time to complete all jobs
                - throughput: Jobs completed per unit time
                - average_utilization: Weighted average utilization across machines
                
        Raises:
            ValueError: If job_data is empty or contains invalid data.
            
        Example:
            >>> jobs = JobSchedulingAnalyzer.load_job_data("results.json")
            >>> metrics = JobSchedulingAnalyzer.calculate_comprehensive_metrics(jobs)
            >>> print(f"Makespan: {metrics['makespan']:.2f}")
            >>> print(f"Throughput: {metrics['throughput']:.2f} jobs/time")
        """
        if not job_data:
            raise ValueError("Job data cannot be empty")
        
        num_jobs = len(job_data)
        
        # Basic time metrics
        total_turnaround_time = sum(job['end'] for job in job_data)
        total_response_time = sum(job['start'] for job in job_data)
        makespan = max(job['end'] for job in job_data)
        
        # Calculate averages
        average_turnaround_time = total_turnaround_time / num_jobs
        average_response_time = total_response_time / num_jobs
        
        # Throughput (jobs per unit time)
        throughput = num_jobs / makespan if makespan > 0 else 0.0
        
        # Calculate utilization if not provided
        if utilization_per_machine is None:
            utilization_per_machine = JobSchedulingAnalyzer.calculate_utilization_per_machine(job_data)
        
        # Calculate weighted average utilization
        machine_capacity = defaultdict(float)
        for job in job_data:
            machine_capacity[job['machine']] = job['capacity']
        
        total_weighted_utilization = 0.0
        total_capacity = sum(machine_capacity.values())
        
        for machine, utilization in utilization_per_machine.items():
            weight = machine_capacity[machine] / total_capacity if total_capacity > 0 else 0.0
            total_weighted_utilization += utilization * weight
        
        return {
            'average_turnaround_time': average_turnaround_time,
            'average_response_time': average_response_time,
            'makespan': makespan,
            'throughput': throughput,
            'average_utilization': total_weighted_utilization,
            'num_jobs': num_jobs,
            'num_machines': len(machine_capacity)
        }
    
    @staticmethod
    def print_metrics(
        metrics: Dict[str, float], 
        utilization_per_machine: Optional[Dict[str, float]] = None,
        precision: int = 4
    ) -> None:
        """
        Print scheduling metrics in a professional, readable format.
        
        Args:
            metrics (Dict[str, float]): Dictionary of calculated metrics.
            utilization_per_machine (Optional[Dict[str, float]]): Per-machine utilization data.
            precision (int): Number of decimal places for floating-point values.
        """
        print("\n" + "="*60)
        print("QUANTUM JOB SCHEDULING PERFORMANCE METRICS")
        print("="*60)
        
        # Time-based metrics
        print(f"\n📊 TEMPORAL METRICS:")
        print(f"   • Makespan:                {metrics['makespan']:.{precision}f} time units")
        print(f"   • Average Turnaround Time: {metrics['average_turnaround_time']:.{precision}f} time units")
        print(f"   • Average Response Time:   {metrics['average_response_time']:.{precision}f} time units")
        
        # Performance metrics
        print(f"\n⚡ PERFORMANCE METRICS:")
        print(f"   • Throughput:              {metrics['throughput']:.{precision}f} jobs/time unit")
        print(f"   • Average Utilization:     {metrics['average_utilization']:.{precision}%}")
        
        # System metrics
        print(f"\n🏗️  SYSTEM METRICS:")
        print(f"   • Total Jobs Processed:    {int(metrics['num_jobs'])}")
        print(f"   • Number of Machines:      {int(metrics['num_machines'])}")
        
        # Per-machine utilization
        if utilization_per_machine:
            print(f"\n🖥️  MACHINE UTILIZATION:")
            sorted_machines = sorted(utilization_per_machine.items(), key=lambda x: x[1], reverse=True)
            for machine, utilization in sorted_machines:
                print(f"   • {machine:<20}: {utilization:.{precision}%}")
        
        print("="*60)
    
    @staticmethod
    def analyze_scheduling_efficiency(job_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform comprehensive scheduling efficiency analysis.
        
        Args:
            job_data (List[Dict[str, Any]]): List of job scheduling data.
            
        Returns:
            Dict[str, Any]: Comprehensive analysis including metrics and insights.
        """
        if not job_data:
            raise ValueError("Job data cannot be empty")
        
        utilization_per_machine = JobSchedulingAnalyzer.calculate_utilization_per_machine(job_data)
        metrics = JobSchedulingAnalyzer.calculate_comprehensive_metrics(
            job_data, utilization_per_machine
        )
        
        # Additional analysis
        machine_workloads = defaultdict(list)
        for job in job_data:
            machine_workloads[job['machine']].append({
                'qubits': job['qubits'],
                'duration': job['duration'],
                'start': job['start'],
                'end': job['end']
            })
        
        # Calculate load balancing metrics
        utilization_values = list(utilization_per_machine.values())
        utilization_variance = sum((u - metrics['average_utilization'])**2 for u in utilization_values) / len(utilization_values)
        load_balance_score = 1.0 - (utilization_variance / (metrics['average_utilization']**2 + 1e-10))
        
        return {
            'metrics': metrics,
            'utilization_per_machine': utilization_per_machine,
            'machine_workloads': dict(machine_workloads),
            'load_balance_score': load_balance_score,
            'most_utilized_machine': max(utilization_per_machine.items(), key=lambda x: x[1]),
            'least_utilized_machine': min(utilization_per_machine.items(), key=lambda x: x[1])
        }


# Legacy functions for backward compatibility
def load_job_data(filepath: str) -> List[Dict[str, Any]]:
    """Legacy wrapper for JobSchedulingAnalyzer.load_job_data()."""
    return JobSchedulingAnalyzer.load_job_data(filepath)


def calculate_metrics(data: List[Dict[str, Any]], utilization_per_machine: Dict[str, float]) -> Dict[str, float]:
    """Legacy wrapper for JobSchedulingAnalyzer.calculate_comprehensive_metrics()."""
    return JobSchedulingAnalyzer.calculate_comprehensive_metrics(data, utilization_per_machine)


def calculate_utilization(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """Legacy wrapper for JobSchedulingAnalyzer.calculate_utilization_per_machine()."""
    return JobSchedulingAnalyzer.calculate_utilization_per_machine(data)


def print_metrics(metrics: Dict[str, float]) -> None:
    """Legacy wrapper for JobSchedulingAnalyzer.print_metrics()."""
    JobSchedulingAnalyzer.print_metrics(metrics)
