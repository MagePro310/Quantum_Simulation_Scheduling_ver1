#!/usr/bin/env python3
"""
Benchmark Management Tool
Tổng hợp công cụ quản lý và chạy toàn bộ hệ thống benchmarking
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import subprocess

class BenchmarkManager:
    """Quản lý toàn bộ hệ thống benchmarking"""
    
    def __init__(self, root_dir: str = "/home/trieu/D/Quantum_Repo/Quantum_Simulation_Scheduling/benchmarks"):
        self.root_dir = Path(root_dir)
        self.comparison_dir = self.root_dir / "comparison"
        self.reports_dir = self.root_dir / "reports"
        self.algorithms_dir = self.root_dir / "algorithms"
        
        # Tạo thư mục nếu chưa tồn tại
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        
    def list_algorithms(self) -> list:
        """Liệt kê tất cả giải thuật"""
        return [d.name for d in self.algorithms_dir.iterdir() if d.is_dir()]
    
    def run_all_algorithms(self) -> dict:
        """Chạy tất cả giải thuật"""
        results = {}
        config_dir = self.comparison_dir / "config"
        
        algorithms = {
            'FFD': 'runLoopTestFFD.py',
            'MTMC': 'runLoopTestMTMC.py',
            'MILQ_extend': 'runLoopTestMILQ.py',
            'NoTaDS': 'runLoopTestNoTaDS.py'
        }
        
        print("\n" + "="*70)
        print("QUANTUM SCHEDULING BENCHMARK - RUNNING ALL ALGORITHMS")
        print("="*70)
        print(f"Timestamp: {datetime.now().isoformat()}")
        print(f"Total algorithms: {len(algorithms)}")
        print("-"*70 + "\n")
        
        for algo_name, script_name in algorithms.items():
            script_path = config_dir / script_name
            
            if not script_path.exists():
                print(f"✗ {algo_name}: Script not found at {script_path}")
                results[algo_name] = {'status': 'failed', 'error': 'Script not found'}
                continue
            
            print(f"▶ Running {algo_name}...")
            
            try:
                # Chạy script
                result = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=str(config_dir),
                    capture_output=True,
                    timeout=600,  # 10 phút timeout
                    text=True
                )
                
                if result.returncode == 0:
                    print(f"  ✓ Success")
                    results[algo_name] = {'status': 'completed'}
                else:
                    print(f"  ✗ Failed with return code {result.returncode}")
                    results[algo_name] = {
                        'status': 'failed',
                        'error': result.stderr[:200] if result.stderr else 'Unknown error'
                    }
            
            except subprocess.TimeoutExpired:
                print(f"  ✗ Timeout after 600 seconds")
                results[algo_name] = {'status': 'timeout'}
            except Exception as e:
                print(f"  ✗ Exception: {str(e)}")
                results[algo_name] = {'status': 'error', 'error': str(e)}
        
        return results
    
    def show_results(self):
        """Hiển thị kết quả"""
        print("\n" + "="*70)
        print("BENCHMARK RESULTS")
        print("="*70)
        
        for algo_name in self.list_algorithms():
            result_dir = self.comparison_dir / "results" / algo_name
            
            if not result_dir.exists():
                print(f"\n{algo_name}: No results found")
                continue
            
            files = list(result_dir.glob("*.json"))
            print(f"\n{algo_name}: {len(files)} result files")
            
            for f in files:
                size_kb = f.stat().st_size / 1024
                print(f"  - {f.name} ({size_kb:.2f} KB)")
    
    def generate_summary(self, results: dict) -> dict:
        """Tạo báo cáo tóm tắt"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_algorithms': len(results),
            'results': results,
            'successful': sum(1 for r in results.values() if r.get('status') == 'completed'),
            'failed': sum(1 for r in results.values() if r.get('status') != 'completed')
        }
        
        return summary
    
    def save_summary(self, summary: dict):
        """Lưu báo cáo tóm tắt"""
        output_file = self.reports_dir / "benchmark_summary.json"
        
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n✓ Summary saved to: {output_file}")
        
        return output_file
    
    def print_summary(self, summary: dict):
        """In báo cáo tóm tắt"""
        print("\n" + "="*70)
        print("BENCHMARK SUMMARY")
        print("="*70)
        print(f"Timestamp: {summary['timestamp']}")
        print(f"Total algorithms: {summary['total_algorithms']}")
        print(f"Successful: {summary['successful']}")
        print(f"Failed: {summary['failed']}")
        
        print("\nDetailed Results:")
        print("-"*70)
        for algo_name, result in summary['results'].items():
            status = result.get('status', 'unknown')
            print(f"  {algo_name:20} {status:15}", end="")
            if 'error' in result:
                print(f"  ({result['error'][:30]})")
            else:
                print()
        
        print("="*70)
    
    def show_directory_structure(self):
        """Hiển thị cấu trúc thư mục"""
        print("\n" + "="*70)
        print("BENCHMARK DIRECTORY STRUCTURE")
        print("="*70)
        
        def print_tree(directory, prefix="", max_depth=3, current_depth=0):
            if current_depth >= max_depth:
                return
            
            items = []
            try:
                items = sorted(directory.iterdir())
            except PermissionError:
                return
            
            for i, item in enumerate(items):
                if item.name.startswith('.'):
                    continue
                
                is_last = i == len(items) - 1
                current_prefix = "└── " if is_last else "├── "
                print(f"{prefix}{current_prefix}{item.name}")
                
                if item.is_dir() and current_depth < max_depth - 1:
                    next_prefix = prefix + ("    " if is_last else "│   ")
                    print_tree(item, next_prefix, max_depth, current_depth + 1)
        
        print(f"\n{self.root_dir.name}/")
        print_tree(self.root_dir)
        print("="*70)


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Quantum Scheduling Benchmark Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python benchmark_manager.py --run-all       # Run all algorithms
  python benchmark_manager.py --show-results  # Show results
  python benchmark_manager.py --show-tree     # Show directory structure
        """
    )
    
    parser.add_argument('--run-all', action='store_true',
                       help='Run all scheduling algorithms')
    parser.add_argument('--show-results', action='store_true',
                       help='Show benchmark results')
    parser.add_argument('--show-tree', action='store_true',
                       help='Show directory structure')
    parser.add_argument('--summary', action='store_true',
                       help='Generate summary report')
    
    args = parser.parse_args()
    
    manager = BenchmarkManager()
    
    if args.run_all:
        results = manager.run_all_algorithms()
        summary = manager.generate_summary(results)
        manager.save_summary(summary)
        manager.print_summary(summary)
    
    elif args.show_results:
        manager.show_results()
    
    elif args.show_tree:
        manager.show_directory_structure()
    
    elif args.summary:
        manager.show_directory_structure()
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
