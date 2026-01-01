#!/usr/bin/env python3
"""
Quick visualization script for algorithm comparison.
Run this after executing algorithm benchmarks to generate comparison charts.

Usage:
    python visualize_results.py                    # Generate all charts
    python visualize_results.py --chart radar      # Generate specific chart
"""

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from benchmarks.comparison.analysis.visualize_comparison import AlgorithmVisualizer


def main():
    """Main entry point for quick visualization."""
    print("\n" + "="*70)
    print("🎨 QUANTUM SCHEDULING ALGORITHM VISUALIZATION")
    print("="*70)
    
    # Get current directory
    current_dir = Path(__file__).parent
    results_dir = current_dir / "results"
    output_dir = current_dir / "reports"
    
    # Check if results exist
    if not results_dir.exists():
        print(f"\n❌ Error: Results directory not found: {results_dir}")
        print("Please run algorithm benchmarks first!")
        return 1
    
    # Check for algorithm directories
    algorithms = ['FFD', 'MTMC', 'MILQ_extend', 'NoTaDS']
    found_algos = [a for a in algorithms if (results_dir / a).exists()]
    
    if not found_algos:
        print(f"\n❌ Error: No algorithm result directories found in {results_dir}")
        print(f"Expected directories: {', '.join(algorithms)}")
        return 1
    
    print(f"\n✓ Found results for: {', '.join(found_algos)}")
    print(f"✓ Results directory: {results_dir}")
    print(f"✓ Output directory: {output_dir}")
    
    # Create visualizer
    visualizer = AlgorithmVisualizer(results_dir=str(results_dir))
    
    # Generate all visualizations
    try:
        visualizer.generate_all_visualizations(output_dir=str(output_dir))
        print("\n✅ SUCCESS! All visualizations generated.")
        print(f"\n📁 Check the reports in: {output_dir}")
        return 0
    except Exception as e:
        print(f"\n❌ Error generating visualizations: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
