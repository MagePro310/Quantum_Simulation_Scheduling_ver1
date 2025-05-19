import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# List all normalized CSVs in the calculation folder
csv_folder = 'analyze/calculation'
csv_files = sorted(glob.glob(os.path.join(csv_folder, 'normalized_*.csv')))

# Read and merge all CSVs on 'dataset'
dfs = []
labels = []
for csv_file in csv_files:
    metric = os.path.basename(csv_file).replace('normalized_', '').replace('.csv', '').replace('_', ' ').title()
    labels.append(metric)
    df = pd.read_csv(csv_file)[['dataset', 'final_score']].rename(columns={'final_score': metric})
    dfs.append(df)

from functools import reduce
df_merged = reduce(lambda left, right: pd.merge(left, right, on='dataset'), dfs)

# Radar plot setup
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close the circle

# Create output folder
output_folder = 'radarplots'
os.makedirs(output_folder, exist_ok=True)

# Assign a color to each algorithm (dataset)
color_map = plt.get_cmap('tab10')
datasets = df_merged['dataset'].tolist()
colors = {dataset: color_map(i % 10) for i, dataset in enumerate(datasets)}

# 1. Save one radar plot for each algorithm, using the same color as in the total plot
for _, row in df_merged.iterrows():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    values = row[labels].tolist()
    values += values[:1]
    color = colors[row['dataset']]
    ax.plot(angles, values, label=row['dataset'], color=color)
    ax.fill(angles, values, color=color, alpha=0.1)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 1.1)
    plt.title(f'Radar Plot: {row["dataset"]}')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'{row["dataset"]}_radar.png'))
    plt.close()

# 2. Save one radar plot for all algorithms together, using the same colors
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
for _, row in df_merged.iterrows():
    values = row[labels].tolist()
    values += values[:1]
    color = colors[row['dataset']]
    ax.plot(angles, values, label=row['dataset'], color=color)
    ax.fill(angles, values, color=color, alpha=0.1)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0, 1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.title('Radar Plot: All Metrics')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'all_algorithms_radar.png'))
plt.close()