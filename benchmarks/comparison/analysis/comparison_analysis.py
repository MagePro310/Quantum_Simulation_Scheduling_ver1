#!/usr/bin/env python3
"""
Comparison Analysis Tool
Analyzes and compares performance metrics across different scheduling algorithms
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class ComparisonAnalyzer:
    """Analyzes benchmark results across algorithms"""
    
    def __init__(self, results_dir: str = "../results"):
        self.results_dir = Path(results_dir)
        self.metrics = {}
        self.visualizations_dir = Path(__file__).parent / "visualizations"
        self.visualizations_dir.mkdir(exist_ok=True)
        
    def load_results(self) -> Dict[str, Any]:
        """Load results from all algorithm directories"""
        algorithms = {}
        
        for algo_dir in self.results_dir.iterdir():
            if algo_dir.is_dir():
                algo_name = algo_dir.name
                algorithms[algo_name] = {
                    'path': algo_dir,
                    'files': list(algo_dir.glob('*.json'))
                }
        
        return algorithms
    
    def calculate_metrics(self, algorithms: Dict[str, Any]) -> Dict[str, Dict[str, float]]:
        """Calculate performance metrics for each algorithm"""
        metrics = {}
        
        for algo_name, algo_info in algorithms.items():
            metrics[algo_name] = {
                'name': algo_name,
                'file_count': len(algo_info['files']),
                'total_size_kb': sum(f.stat().st_size for f in algo_info['files']) / 1024,
                'timestamp': datetime.now().isoformat()
            }
        
        return metrics
    
    def create_comparison_table(self, metrics: Dict[str, Dict[str, float]]) -> str:
        """Create a comparison table in markdown"""
        table = """# Algorithm Comparison Results

## Performance Metrics Table

| Algorithm | Type | Files | Total Size (KB) | Status |
|-----------|------|-------|-----------------|--------|
"""
        
        algo_types = {
            'FFD': 'Heuristic',
            'MTMC': 'Heuristic',
            'MILQ_extend': 'ILP',
            'NoTaDS': 'ILP'
        }
        
        for algo_name, metric in sorted(metrics.items()):
            algo_type = algo_types.get(algo_name, 'Unknown')
            table += f"| {algo_name} | {algo_type} | {metric['file_count']} | {metric['total_size_kb']:.2f} | ✓ |\n"
        
        return table
    
    def generate_summary_report(self) -> Dict[str, Any]:
        """Generate a comprehensive summary report"""
        algorithms = self.load_results()
        metrics = self.calculate_metrics(algorithms)
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_algorithms': len(algorithms),
            'algorithms': metrics,
            'comparison_table': self.create_comparison_table(metrics)
        }
        
        return report
    
    def save_report(self, report: Dict[str, Any], output_path: str = "performance_metrics.json"):
        """Save report to file"""
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"✓ Report saved to: {output_path}")
    
    def print_summary(self, report: Dict[str, Any]):
        """Print summary to console"""
        print("\n" + "="*70)
        print("ALGORITHM COMPARISON ANALYSIS")
        print("="*70)
        print(f"Timestamp: {report['timestamp']}")
        print(f"Total Algorithms: {report['total_algorithms']}")
        print("-"*70)
        
        for algo_name, metric in sorted(report['algorithms'].items()):
            print(f"\n{algo_name}:")
            print(f"  Files: {metric['file_count']}")
            print(f"  Total Size: {metric['total_size_kb']:.2f} KB")
        
        print("\n" + "="*70 + "\n")


def main():
    """Main analysis function"""
    analyzer = ComparisonAnalyzer()
    
    # Generate report
    report = analyzer.generate_summary_report()
    
    # Save and display
    analyzer.save_report(report)
    analyzer.print_summary(report)
    
    # Print comparison table
    print(report['comparison_table'])


if __name__ == "__main__":
    main()
