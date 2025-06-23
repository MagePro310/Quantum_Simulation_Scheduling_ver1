"""
Quantum Scheduling Data Analysis Pipeline

This module provides a comprehensive analysis pipeline for quantum scheduling experiments,
including data extraction from JSON results, CSV conversion, statistical analysis,
and visualization generation.

Author: Quantum Scheduling Team
Date: 2025
"""

import os
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from functools import reduce

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.backends.backend_pdf import PdfPages

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class AnalysisConfig:
    """Configuration class for analysis parameters."""
    
    # Metrics to analyze
    METRICS = [
        "average_turnaroundTime",
        "average_responseTime", 
        "average_fidelity",
        "sampling_overhead",
        "average_throughput",
        "average_utilization",
        "scheduler_latency",
        "makespan"
    ]
    
    # Algorithm datasets
    ALGORITHMS = ["FFD", "MILQ", "NoTaDS", "MTMC"]
    
    # File patterns
    JSON_PATTERN = re.compile(r"(\d+)_(\d+)\.0_0\.json")
    
    # Output directories
    OUTPUT_DIRS = {
        "base": "analyze",
        "all": "analyze/all",
        "csv": "analyze/all/csv", 
        "plots": "analyze/all/plots",
        "calculation": "analyze/calculation",
        "radar": "radarplots"
    }
    
    # Plot styling
    PLOT_STYLE = {
        "figure_size": (12, 8),
        "radar_size": (10, 10),
        "palette": "Set2",
        "line_width": 2.5,
        "marker_size": 8,
        "alpha": 0.15
    }


class DataExtractor:
    """Handles extraction and processing of JSON experiment data."""
    
    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def extract_json_data(self, base_path: str = "component/finalResult/5_5") -> pd.DataFrame:
        """
        Extract data from JSON files across all algorithm folders.
        
        Args:
            base_path: Base path to the results directory
            
        Returns:
            DataFrame containing all extracted data
        """
        data = []
        
        for algorithm in self.config.ALGORITHMS:
            folder_path = Path(base_path) / algorithm / "ghz"
            
            if not folder_path.exists():
                self.logger.warning(f"Folder not found: {folder_path}")
                continue
                
            self.logger.info(f"Processing {algorithm} data from {folder_path}")
            
            for file_path in folder_path.glob("*.json"):
                match = self.config.JSON_PATTERN.match(file_path.name)
                if not match:
                    continue
                    
                try:
                    with open(file_path, 'r') as f:
                        content = json.load(f)
                    
                    entry = {
                        'filename': file_path.name,
                        'algorithm': algorithm,
                        'num_circuits': int(match.group(1)),
                        'num_qubits_per_circuit': int(match.group(2))
                    }
                    
                    # Extract metrics
                    for metric in self.config.METRICS:
                        entry[metric] = content.get(metric, np.nan)
                    
                    data.append(entry)
                    
                except (json.JSONDecodeError, FileNotFoundError) as e:
                    self.logger.error(f"Error processing {file_path}: {e}")
        
        if not data:
            raise ValueError("No valid data found. Check file paths and patterns.")
        
        df = pd.DataFrame(data)
        df = df.sort_values(['num_circuits', 'num_qubits_per_circuit', 'algorithm'])
        
        self.logger.info(f"Extracted {len(df)} records from {len(df['algorithm'].unique())} algorithms")
        return df
    
    def save_metric_csvs(self, df: pd.DataFrame, output_dir: str) -> None:
        """Save individual metric data to CSV files."""
        os.makedirs(output_dir, exist_ok=True)
        
        for metric in self.config.METRICS:
            metric_data = df[['num_circuits', 'num_qubits_per_circuit', 'algorithm', metric]].dropna()
            csv_path = Path(output_dir) / f"{metric}_data.csv"
            metric_data.to_csv(csv_path, index=False)
            self.logger.info(f"Saved {metric} data to {csv_path}")


class DataNormalizer:
    """Handles data normalization and scoring calculations."""
    
    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def normalize_metrics(self, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        Normalize metrics and calculate final scores for each algorithm.
        
        Args:
            df: Raw data DataFrame
            
        Returns:
            Dictionary of normalized DataFrames for each metric
        """
        normalized_data = {}
        
        # Define metrics that should be minimized (lower is better)
        minimize_metrics = {
            'average_turnaroundTime', 'average_responseTime', 'sampling_overhead',
            'scheduler_latency', 'makespan'
        }
        
        for metric in self.config.METRICS:
            metric_df = df.groupby('algorithm')[metric].mean().reset_index()
            metric_df.columns = ['dataset', 'score']
            
            # Normalize scores to 0-1 range
            min_score = metric_df['score'].min()
            max_score = metric_df['score'].max()
            
            if metric in minimize_metrics:
                # For metrics to minimize: higher raw score gets lower normalized score
                metric_df['final_score'] = 1 - (metric_df['score'] - min_score) / (max_score - min_score)
            else:
                # For metrics to maximize: higher raw score gets higher normalized score
                metric_df['final_score'] = (metric_df['score'] - min_score) / (max_score - min_score)
            
            # Handle edge case where all values are the same
            if max_score == min_score:
                metric_df['final_score'] = 1.0
            
            normalized_data[metric] = metric_df
            
            # Save normalized data
            output_path = Path(self.config.OUTPUT_DIRS['calculation']) / f"normalized_{metric}.csv"
            os.makedirs(output_path.parent, exist_ok=True)
            metric_df.to_csv(output_path, index=False)
            
        self.logger.info(f"Normalized {len(self.config.METRICS)} metrics")
        return normalized_data


class Visualizer:
    """Handles all visualization tasks including line plots and radar charts."""
    
    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Set up matplotlib style
        plt.style.use('seaborn-v0_8')
        sns.set_palette(self.config.PLOT_STYLE['palette'])
    
    def create_metric_plots(self, df: pd.DataFrame, output_dir: str) -> None:
        """Create line plots for each metric."""
        plot_dir = Path(output_dir) / "plots"
        os.makedirs(plot_dir, exist_ok=True)
        
        # Create a multi-page PDF with all plots
        pdf_path = plot_dir / "all_metrics_analysis.pdf"
        
        with PdfPages(pdf_path) as pdf:
            for metric in self.config.METRICS:
                fig, ax = plt.subplots(figsize=self.config.PLOT_STYLE['figure_size'])
                
                # Create the plot
                sns.lineplot(
                    data=df,
                    x='num_circuits',
                    y=metric,
                    hue='algorithm',
                    style='num_qubits_per_circuit',
                    markers=True,
                    linewidth=self.config.PLOT_STYLE['line_width'],
                    markersize=self.config.PLOT_STYLE['marker_size'],
                    ax=ax
                )
                
                # Styling
                ax.set_title(f'{metric.replace("_", " ").title()} Analysis', 
                           fontsize=16, fontweight='bold', pad=20)
                ax.set_xlabel('Number of Circuits', fontsize=12, fontweight='bold')
                ax.set_ylabel(metric.replace('_', ' ').title(), fontsize=12, fontweight='bold')
                ax.grid(True, alpha=0.3)
                
                # Format x-axis to show only integer values
                ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
                
                # Improve legend
                handles, labels = ax.get_legend_handles_labels()
                algorithm_handles = handles[:len(self.config.ALGORITHMS)]
                algorithm_labels = labels[:len(self.config.ALGORITHMS)]
                
                legend1 = ax.legend(algorithm_handles, algorithm_labels, 
                                  title='Algorithm', loc='upper left')
                legend1.get_title().set_fontweight('bold')
                
                plt.tight_layout()
                pdf.savefig(fig, bbox_inches='tight', dpi=300)
                
                # Also save individual plots
                individual_path = plot_dir / f"{metric}_analysis.png"
                fig.savefig(individual_path, bbox_inches='tight', dpi=300)
                plt.close(fig)
        
        self.logger.info(f"Created metric plots in {plot_dir}")
    
    def create_radar_plots(self, normalized_data: Dict[str, pd.DataFrame], output_dir: str) -> None:
        """Create radar plots for algorithm comparison."""
        radar_dir = Path(output_dir)
        os.makedirs(radar_dir, exist_ok=True)
        
        # Merge all normalized data
        dfs = []
        metric_labels = []
        
        for metric, df in normalized_data.items():
            clean_label = metric.replace('average_', '').replace('_', ' ').title()
            metric_labels.append(clean_label)
            df_renamed = df[['dataset', 'final_score']].rename(
                columns={'final_score': clean_label}
            )
            dfs.append(df_renamed)
        
        df_merged = reduce(lambda left, right: pd.merge(left, right, on='dataset'), dfs)
        
        # Radar plot setup
        num_vars = len(metric_labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]  # Close the circle
        
        # Color mapping
        colors = plt.cm.Set2(np.linspace(0, 1, len(df_merged)))
        color_map = {dataset: colors[i] for i, dataset in enumerate(df_merged['dataset'])}
        
        # Individual radar plots for each algorithm
        for _, row in df_merged.iterrows():
            fig, ax = plt.subplots(figsize=self.config.PLOT_STYLE['radar_size'], 
                                 subplot_kw=dict(projection='polar'))
            
            values = row[metric_labels].tolist()
            values += values[:1]
            color = color_map[row['dataset']]
            
            ax.plot(angles, values, 'o-', linewidth=3, label=row['dataset'], color=color)
            ax.fill(angles, values, alpha=self.config.PLOT_STYLE['alpha'], color=color)
            
            # Styling
            ax.set_theta_offset(np.pi / 2)
            ax.set_theta_direction(-1)
            ax.set_thetagrids(np.degrees(angles[:-1]), metric_labels, fontsize=11)
            ax.set_ylim(0, 1.1)
            ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
            ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
            ax.grid(True, alpha=0.3)
            
            plt.title(f'{row["dataset"]} Algorithm Performance', 
                     fontsize=16, fontweight='bold', pad=30)
            plt.tight_layout()
            plt.savefig(radar_dir / f'{row["dataset"]}_radar.pdf', 
                       bbox_inches='tight', dpi=300, format='pdf')
            plt.close()
        
        # Combined radar plot
        fig, ax = plt.subplots(figsize=self.config.PLOT_STYLE['radar_size'], 
                             subplot_kw=dict(projection='polar'))
        
        for _, row in df_merged.iterrows():
            values = row[metric_labels].tolist()
            values += values[:1]
            color = color_map[row['dataset']]
            
            ax.plot(angles, values, 'o-', linewidth=3, 
                   label=row['dataset'], color=color, markersize=8)
            ax.fill(angles, values, alpha=self.config.PLOT_STYLE['alpha'], color=color)
        
        # Styling
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles[:-1]), metric_labels, fontsize=12)
        ax.set_ylim(0, 1.1)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=11)
        ax.grid(True, alpha=0.3)
        
        plt.title('Algorithm Performance Comparison', 
                 fontsize=18, fontweight='bold', pad=30)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)
        plt.tight_layout()
        plt.savefig(radar_dir / 'all_algorithms_radar.pdf', 
                   bbox_inches='tight', dpi=300, format='pdf')
        plt.close()
        
        self.logger.info(f"Created radar plots in {radar_dir}")


class QuantumSchedulingAnalyzer:
    """Main analyzer class that orchestrates the entire analysis pipeline."""
    
    def __init__(self, config: Optional[AnalysisConfig] = None):
        self.config = config or AnalysisConfig()
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Initialize components
        self.extractor = DataExtractor(self.config)
        self.normalizer = DataNormalizer(self.config)
        self.visualizer = Visualizer(self.config)
    
    def run_full_analysis(self, base_path: str = "component/finalResult/5_5") -> pd.DataFrame:
        """
        Run the complete analysis pipeline.
        
        Args:
            base_path: Path to the experiment results
            
        Returns:
            DataFrame containing all processed data
        """
        self.logger.info("Starting comprehensive quantum scheduling analysis...")
        
        # Create output directories
        for dir_path in self.config.OUTPUT_DIRS.values():
            os.makedirs(dir_path, exist_ok=True)
        
        try:
            # Step 1: Extract data from JSON files
            self.logger.info("Step 1: Extracting data from JSON files...")
            df = self.extractor.extract_json_data(base_path)
            
            # Step 2: Save individual metric CSVs
            self.logger.info("Step 2: Saving metric CSV files...")
            self.extractor.save_metric_csvs(df, self.config.OUTPUT_DIRS['csv'])
            
            # Step 3: Normalize metrics
            self.logger.info("Step 3: Normalizing metrics...")
            normalized_data = self.normalizer.normalize_metrics(df)
            
            # Step 4: Create visualizations
            self.logger.info("Step 4: Creating metric plots...")
            self.visualizer.create_metric_plots(df, self.config.OUTPUT_DIRS['all'])
            
            self.logger.info("Step 5: Creating radar plots...")
            self.visualizer.create_radar_plots(normalized_data, self.config.OUTPUT_DIRS['radar'])
            
            # Step 6: Generate summary report
            self.logger.info("Step 6: Generating summary report...")
            self._generate_summary_report(df, normalized_data)
            
            self.logger.info("Analysis completed successfully!")
            return df
            
        except Exception as e:
            self.logger.error(f"Analysis failed: {e}")
            raise
    
    def _generate_summary_report(self, df: pd.DataFrame, 
                               normalized_data: Dict[str, pd.DataFrame]) -> None:
        """Generate a summary report of the analysis."""
        report_path = Path(self.config.OUTPUT_DIRS['all']) / "analysis_summary.txt"
        
        with open(report_path, 'w') as f:
            f.write("QUANTUM SCHEDULING ANALYSIS SUMMARY\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Records Analyzed: {len(df)}\n")
            f.write(f"Algorithms Compared: {', '.join(self.config.ALGORITHMS)}\n")
            f.write(f"Metrics Evaluated: {len(self.config.METRICS)}\n\n")
            
            f.write("ALGORITHM RANKING BY METRIC:\n")
            f.write("-" * 30 + "\n")
            
            for metric in self.config.METRICS:
                if metric in normalized_data:
                    rankings = normalized_data[metric].sort_values('final_score', ascending=False)
                    f.write(f"\n{metric.replace('_', ' ').title()}:\n")
                    for i, (_, row) in enumerate(rankings.iterrows(), 1):
                        f.write(f"  {i}. {row['dataset']}: {row['final_score']:.4f}\n")
            
            # Overall performance summary
            f.write(f"\n\nOVERALL PERFORMANCE SUMMARY:\n")
            f.write("-" * 30 + "\n")
            
            # Calculate average normalized scores across all metrics
            all_scores = []
            for metric_df in normalized_data.values():
                scores_df = metric_df[['dataset', 'final_score']].copy()
                all_scores.append(scores_df)
            
            if all_scores:
                combined = pd.concat(all_scores)
                overall_ranking = combined.groupby('dataset')['final_score'].mean().sort_values(ascending=False)
                
                f.write("Average Performance Ranking:\n")
                for i, (algorithm, score) in enumerate(overall_ranking.items(), 1):
                    f.write(f"  {i}. {algorithm}: {score:.4f}\n")
        
        self.logger.info(f"Summary report saved to {report_path}")


def main():
    """Main execution function."""
    try:
        # Initialize analyzer
        analyzer = QuantumSchedulingAnalyzer()
        
        # Run analysis
        df = analyzer.run_full_analysis()
        
        print(f"\nAnalysis completed successfully!")
        print(f"Processed {len(df)} records from {len(df['algorithm'].unique())} algorithms")
        print(f"Results saved in: {analyzer.config.OUTPUT_DIRS['all']}")
        
    except Exception as e:
        print(f"Analysis failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
