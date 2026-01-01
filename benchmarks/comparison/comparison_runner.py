#!/usr/bin/env python3
"""
Comparison Runner for Quantum Scheduling Algorithms
====================================================

Purpose:
    Orchestrates automated benchmarking of 4 scheduling algorithms:
    - FFD (First Fit Decreasing) - Heuristic
    - MTMC (Multi-Task Multi-Constraint) - Heuristic
    - MILQ_extend (Mixed Integer Linear with cutting) - ILP
    - NoTaDS (No Task Decomposition Scheduling) - ILP
    
Workflow:
    1. Load benchmark configuration from benchmark_config.json
    2. Run each algorithm with same input parameters
    3. Collect execution times, metrics, and results
    4. Generate comparison report to reports/comparison_results.json
    5. Print summary with performance rankings
    
Usage:
    # Run all algorithms
    cd benchmarks/comparison
    conda activate squan  # CRITICAL: Must activate environment first
    python comparison_runner.py
    
    # Or use from code
    from comparison_runner import BenchmarkRunner
    runner = BenchmarkRunner()
    runner.run_all_algorithms()
    runner.generate_comparison_report()
    
Configuration:
    Edit config/benchmark_config.json to modify:
    - Algorithm selection
    - Job counts and qubit ranges
    - Timeout settings
    - Output directories
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# Add parent directories to path for component/flow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

class BenchmarkRunner:
    """
    Orchestrates benchmarking across multiple scheduling algorithms.
    
    Responsibilities:
        1. Load algorithm configurations from JSON
        2. Execute each algorithm with standardized inputs
        3. Capture execution metrics (time, makespan, fidelity)
        4. Generate unified comparison report
        
    Attributes:
        config_path: Path to benchmark_config.json
        config: Loaded configuration dictionary
        results: Dict storing algorithm execution results
        start_time: Benchmark suite start timestamp
        end_time: Benchmark suite completion timestamp
        
    Key Methods:
        - run_all_algorithms(): Execute full benchmark suite
        - run_single_algorithm(): Run one algorithm and record metrics
        - generate_comparison_report(): Create JSON report with results
        - print_summary(): Display console summary of results
        
    Configuration Schema:
        {
            "benchmark_info": {"name": "...", "version": "..."},
            "algorithms": {
                "FFD": {
                    "name": "First Fit Decreasing",
                    "type": "heuristic",
                    "run_file": "config/runLoopTestFFD.py",
                    "test_file": "config/test_algorithm_FFD.ipynb"
                },
                ...
            }
        }
    """
    
    def __init__(self, config_path: str = "benchmark_config.json"):
        """
        Initialize benchmark runner.
        
        Args:
            config_path: Relative or absolute path to benchmark_config.json
                        Default looks in current directory
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.results = {}
        self.start_time = None
        self.end_time = None
        
    def _load_config(self) -> Dict[str, Any]:
        """
        Load and parse benchmark configuration file.
        
        Returns:
            Configuration dictionary with algorithm definitions and parameters
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def run_all_algorithms(self) -> Dict[str, Any]:
        """
        Execute full benchmark suite across all configured algorithms.
        
        Process:
            1. Record start time
            2. Load algorithm list from config
            3. Execute each algorithm sequentially
            4. Collect results into self.results dictionary
            5. Record end time
            
        Returns:
            Dict[algo_name, result_dict] with execution metrics
            
        Output Format:
            {
                "FFD": {
                    "name": "First Fit Decreasing",
                    "type": "heuristic",
                    "execution_time": 12.34,
                    "status": "completed",
                    "timestamp": "2025-01-15T10:30:00"
                },
                ...
            }
            
        Side Effects:
            - Prints progress to console
            - Updates self.results
            - Sets self.start_time and self.end_time
        """
        self.start_time = datetime.now()
        algorithms = self.config['algorithms']
        
        print("\n" + "="*70)
        print("QUANTUM SCHEDULING ALGORITHM BENCHMARK")
        print("="*70)
        print(f"Start time: {self.start_time}")
        print(f"Total algorithms to test: {len(algorithms)}")
        print("-"*70)
        
        for algo_name, algo_config in algorithms.items():
            print(f"\n▶ Running {algo_config['name']} ({algo_name})...")
            self.run_single_algorithm(algo_name, algo_config)
        
        self.end_time = datetime.now()
        return self.results
    
    def run_single_algorithm(self, algo_name: str, algo_config: Dict[str, Any]):
        """
        Execute a single scheduling algorithm and capture metrics.
        
        Args:
            algo_name: Algorithm identifier (e.g., "FFD", "MILQ_extend")
            algo_config: Configuration dict from benchmark_config.json
                        Contains: name, type, run_file, test_file
        
        Process:
            1. Start timer
            2. Load algorithm module from run_file
            3. Execute algorithm with standard inputs
            4. Record execution time
            5. Capture success/failure status
            6. Store results in self.results[algo_name]
            
        Result Dictionary Structure:
            On Success:
            {
                "name": "First Fit Decreasing",
                "type": "heuristic",
                "execution_time": 12.34,
                "status": "completed",
                "timestamp": "2025-01-15T10:30:00"
            }
            
            On Failure:
            {
                "name": "First Fit Decreasing",
                "type": "heuristic",
                "error": "ModuleNotFoundError: ...",
                "status": "failed",
                "timestamp": "2025-01-15T10:30:00"
            }
            
        Side Effects:
            - Prints progress messages
            - Updates self.results
            
        """
        algo_start = time.time()
        
        try:
            config_dir = Path(self.config_path).parent
            script_path = config_dir / algo_config['run_file']
            if not script_path.exists():
                raise FileNotFoundError(f"Run file not found: {script_path}")

            benchmark_params = self.config.get("benchmark_parameters", {})
            num_jobs = int(benchmark_params.get("default_num_jobs", 5))
            num_qubits = int(next(iter(benchmark_params.get("num_qubits", [5]))))

            print(f"   - Executing: {script_path} ({num_jobs} jobs, {num_qubits} qubits/job)")
            print(f"   - Testing with benchmark: {algo_config['test_file']}")
            print(f"   - Algorithm type: {algo_config['type']}")

            subprocess.run(
                [sys.executable, str(script_path), str(num_jobs), str(num_qubits)],
                check=True,
                cwd=script_path.parent,
            )
            algo_duration = time.time() - algo_start

            self.results[algo_name] = {
                'name': algo_config['name'],
                'type': algo_config['type'],
                'execution_time': algo_duration,
                'status': 'completed',
                'timestamp': datetime.now().isoformat()
            }
            
            print(f"   ✓ Completed in {algo_duration:.2f} seconds")
            
        except Exception as e:
            # Record failure with error details
            self.results[algo_name] = {
                'name': algo_config['name'],
                'type': algo_config['type'],
                'error': str(e),
                'status': 'failed',
                'timestamp': datetime.now().isoformat()
            }
            print(f"   ✗ Failed: {e}")
    
    def generate_comparison_report(self, output_path: str = "../reports/comparison_results.json"):
        """
        Generate comprehensive JSON report comparing all algorithm results.
        
        Args:
            output_path: Path for output JSON file
                        Default: benchmarks/reports/comparison_results.json
        
        Report Structure:
            {
                "metadata": {
                    "benchmark_name": "Quantum Scheduling Comparison",
                    "timestamp": "2025-01-15T10:35:00",
                    "duration_seconds": 123.45
                },
                "results": {
                    "FFD": {...},
                    "MTMC": {...},
                    "MILQ_extend": {...},
                    "NoTaDS": {...}
                },
                "algorithms_tested": ["FFD", "MTMC", "MILQ_extend", "NoTaDS"]
            }
        
        Side Effects:
            - Creates output directory if needed
            - Writes JSON file to output_path
            - Prints confirmation message
        
        Returns:
            Dict containing the complete report
        """
        report = {
            'metadata': {
                'benchmark_name': self.config['benchmark_info']['name'],
                'timestamp': datetime.now().isoformat(),
                'duration_seconds': (self.end_time - self.start_time).total_seconds() if self.end_time else 0
            },
            'results': self.results,
            'algorithms_tested': list(self.config['algorithms'].keys())
        }
        
        # Ensure output directory exists
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Write report to JSON
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n✓ Report saved to: {output_path}")
        return report
    
    def print_summary(self):
        """
        Print human-readable summary of benchmark results to console.
        
        Displays:
            - Total benchmark duration
            - Success/failure counts
            - Algorithm performance rankings (sorted by execution time)
            
        Output Example:
            ======================================================================
            BENCHMARK SUMMARY
            ======================================================================
            Total duration: 123.45 seconds
            Successful: 3/4
            Failed: 1/4
            
            Algorithm Performance:
            ----------------------------------------------------------------------
              FFD                        2.34s
              MTMC                       3.21s
              NoTaDS                     8.90s
            ======================================================================
        """
        print("\n" + "="*70)
        print("BENCHMARK SUMMARY")
        print("="*70)
        
        # Calculate statistics
        total_duration = (self.end_time - self.start_time).total_seconds() if self.end_time else 0
        successful = sum(1 for r in self.results.values() if r.get('status') == 'completed')
        failed = sum(1 for r in self.results.values() if r.get('status') == 'failed')
        
        print(f"Total duration: {total_duration:.2f} seconds")
        print(f"Successful: {successful}/{len(self.results)}")
        print(f"Failed: {failed}/{len(self.results)}")
        
        # Display algorithm rankings
        if successful > 0:
            print("\nAlgorithm Performance:")
            print("-"*70)
            # Sort by execution time (ascending)
            for algo_name, result in sorted(self.results.items(), 
                                          key=lambda x: x[1].get('execution_time', float('inf'))):
                if result.get('status') == 'completed':
                    print(f"  {algo_name:20} {result['execution_time']:10.2f}s")
        
        print("="*70 + "\n")


if __name__ == "__main__":
    """
    Main entry point for comparison benchmarking.
    
    Execution Flow:
        1. Create BenchmarkRunner instance
        2. Run all configured algorithms
        3. Generate JSON report
        4. Print console summary
        
    Prerequisites:
        - Must run from benchmarks/comparison/ directory
        - Requires conda activate squan before execution
        - Requires benchmark_config.json in current directory
        
    Usage:
        cd benchmarks/comparison
        conda activate squan
        python comparison_runner.py
        
    Output:
        - Console: Progress updates and summary
        - File: ../reports/comparison_results.json
    """
    runner = BenchmarkRunner()
    runner.run_all_algorithms()
    runner.generate_comparison_report()
    runner.print_summary()
