#!/usr/bin/env python3
"""
Main execution script for the Quantum Scheduling Pipeline.

This script provides a command-line interface for running quantum scheduling
experiments with various configurations.

Usage:
    python main.py --help
    python main.py --qubits 7 --jobs 2 --algorithm FFD --mode multi_threaded
    python main.py --config config.json
"""

import argparse
import sys
import json
from typing import Optional

from quantum_scheduling_pipeline import QuantumSchedulingPipeline
from config import (
    PipelineConfig, ExperimentConfig, SimulationMode, 
    SchedulingAlgorithm, DEFAULT_PIPELINE_CONFIG
)
from component.utils import setup_logging, save_json, load_json, print_pipeline_summary


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Quantum Circuit Scheduling and Simulation Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Run with default settings
    python main.py
    
    # Run with custom parameters and show plots
    python main.py --qubits 10 --jobs 5 --algorithm FFD --mode single_threaded --show-plots
    
    # Load configuration from file
    python main.py --config my_config.json
    
    # Run experiment with verbose output
    python main.py --qubits 7 --jobs 2 --verbose
        """
    )
    
    # Basic configuration
    parser.add_argument(
        '--qubits', '-q', type=int, default=7,
        help='Number of qubits per job (default: 7)'
    )
    parser.add_argument(
        '--jobs', '-j', type=int, default=2,
        help='Number of jobs to schedule (default: 2)'
    )
    parser.add_argument(
        '--algorithm', '-a', type=str, default='FFD',
        choices=['FFD', 'MILQ', 'MTMC', 'NoTaDS'],
        help='Scheduling algorithm to use (default: FFD)'
    )
    parser.add_argument(
        '--mode', '-m', type=str, default='multi_threaded',
        choices=['single_threaded', 'multi_threaded'],
        help='Simulation execution mode (default: multi_threaded)'
    )
    parser.add_argument(
        '--backends', '-b', nargs='+', default=['belem', 'manila'],
        help='Quantum backends to use (default: belem manila)'
    )
    parser.add_argument(
        '--shots', '-s', type=int, default=1024,
        help='Number of shots for quantum simulation (default: 1024)'
    )
    
    # Experiment configuration
    parser.add_argument(
        '--experiment-id', '-e', type=str, default='5_5',
        help='Experiment identifier for result storage (default: 5_5)'
    )
    parser.add_argument(
        '--no-cutting', action='store_true',
        help='Disable circuit cutting'
    )
    parser.add_argument(
        '--no-knitting', action='store_true',
        help='Disable circuit knitting'
    )
    parser.add_argument(
        '--no-visualizations', action='store_true',
        help='Disable visualization generation'
    )
    parser.add_argument(
        '--show-plots', action='store_true',
        help='Display plots during execution (default: save only)'
    )
    
    # Configuration file
    parser.add_argument(
        '--config', '-c', type=str,
        help='Load configuration from JSON file'
    )
    parser.add_argument(
        '--save-config', type=str,
        help='Save current configuration to JSON file'
    )
    
    # Output and logging
    parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--quiet', action='store_true',
        help='Suppress all output except errors'
    )
    parser.add_argument(
        '--output-dir', '-o', type=str,
        help='Custom output directory for results'
    )
    
    return parser.parse_args()


def create_config_from_args(args: argparse.Namespace) -> PipelineConfig:
    """Create pipeline configuration from command line arguments."""
    return PipelineConfig(
        num_qubits_per_job=args.qubits,
        num_jobs=args.jobs,
        backend_names=args.backends,
        scheduling_algorithm=SchedulingAlgorithm(args.algorithm),
        simulation_mode=SimulationMode(args.mode),
        shots=args.shots,
        enable_circuit_cutting=not args.no_cutting,
        enable_circuit_knitting=not args.no_knitting,
        experiment_id=args.experiment_id,
        save_visualizations=not args.no_visualizations,
        show_plots=args.show_plots,
        log_level="DEBUG" if args.verbose else ("ERROR" if args.quiet else "INFO")
    )


def load_config_from_file(filepath: str) -> PipelineConfig:
    """Load pipeline configuration from JSON file."""
    try:
        config_data = load_json(filepath)
        
        # Convert string enums back to enum objects
        if 'scheduling_algorithm' in config_data:
            config_data['scheduling_algorithm'] = SchedulingAlgorithm(
                config_data['scheduling_algorithm']
            )
        if 'simulation_mode' in config_data:
            config_data['simulation_mode'] = SimulationMode(
                config_data['simulation_mode']
            )
        
        return PipelineConfig(**config_data)
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        sys.exit(1)


def save_config_to_file(config: PipelineConfig, filepath: str) -> None:
    """Save pipeline configuration to JSON file."""
    try:
        config_dict = config.__dict__.copy()
        
        # Convert enums to strings for JSON serialization
        if 'scheduling_algorithm' in config_dict:
            config_dict['scheduling_algorithm'] = config_dict['scheduling_algorithm'].value
        if 'simulation_mode' in config_dict:
            config_dict['simulation_mode'] = config_dict['simulation_mode'].value
        
        save_json(config_dict, filepath)
        print(f"Configuration saved to {filepath}")
    except Exception as e:
        print(f"Error saving configuration file: {e}")
        sys.exit(1)


def run_single_experiment(config: PipelineConfig) -> str:
    """
    Run a single quantum scheduling experiment.
    
    Args:
        config: Pipeline configuration
        
    Returns:
        Path to the results file
    """
    # Set up logging
    logger = setup_logging(config.log_level)
    
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        logger.error(f"Invalid configuration: {e}")
        sys.exit(1)
    
    # Create and run pipeline
    pipeline = QuantumSchedulingPipeline(config)
    
    try:
        result_path = pipeline.run_complete_pipeline(
            experiment_id=config.experiment_id
        )
        
        # Print summary
        print_pipeline_summary(config, pipeline.metrics.__dict__)
        
        return result_path
        
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        if config.log_level == "DEBUG":
            import traceback
            traceback.print_exc()
        sys.exit(1)


def main():
    """Main execution function."""
    args = parse_arguments()
    
    # Load or create configuration
    if args.config:
        config = load_config_from_file(args.config)
        print(f"Loaded configuration from {args.config}")
    else:
        config = create_config_from_args(args)
    
    # Save configuration if requested
    if args.save_config:
        save_config_to_file(config, args.save_config)
        return
    
    # Print configuration summary
    if not args.quiet:
        print("\n" + "="*60)
        print("QUANTUM SCHEDULING PIPELINE")
        print("="*60)
        print(f"Jobs: {config.num_jobs}")
        print(f"Qubits per job: {config.num_qubits_per_job}")
        print(f"Algorithm: {config.scheduling_algorithm.value}")
        print(f"Mode: {config.simulation_mode.value}")
        print(f"Backends: {', '.join(config.backend_names)}")
        print(f"Shots: {config.shots}")
        print(f"Save Visualizations: {config.save_visualizations}")
        print(f"Show Plots: {config.show_plots}")
        print(f"Experiment ID: {config.experiment_id}")
        print("="*60)
    
    # Run experiment
    result_path = run_single_experiment(config)
    
    if not args.quiet:
        print(f"\n✅ Experiment completed successfully!")
        print(f"📊 Results saved to: {result_path}")


if __name__ == "__main__":
    main()
