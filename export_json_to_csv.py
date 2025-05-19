import os
import json
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Define metrics to extract
metrics = [
    "average_turnaroundTime",
    "average_responseTime",
    "average_fidelity",
    "sampling_overhead",
    "average_throughput",
    "average_utilization",
    "scheduler_latency",
    "makespan"
]

# Define folders for the datasets
folder_paths = {
    "FFD": os.path.join("component", "finalResult", "5_5", "FFD", "ghz"),
    "MILQ": os.path.join("component", "finalResult", "5_5", "MILQ", "ghz"),
    "NoTaDS": os.path.join("component", "finalResult", "5_5", "NoTaDS", "ghz"),
    "MTMC": os.path.join("component", "finalResult", "5_5", "MTMC", "ghz"),
}

# Compile regex to match files like 2_0.0_0.json → 10_6.0_0.json
pattern = re.compile(r"(\d+)_(\d+)\.0_0\.json")

# Read data from all datasets
data = []
for dataset_name, folder_path in folder_paths.items():
    for file in os.listdir(folder_path):
        match = pattern.match(file)
        if match:
            num_circuit = int(match.group(1))
            num_qubits_each_circuit = int(match.group(2))
            with open(os.path.join(folder_path, file), "r") as f:
                content = json.load(f)
                entry = {metric: content.get(metric, None) for metric in metrics}
                entry["filename"] = file
                entry["dataset"] = dataset_name
                entry["num_circuit"] = num_circuit
                entry["num_qubits_each_circuit"] = num_qubits_each_circuit
                data.append(entry)

if not data:
    print(f"No matching files found. Please check folders and regex pattern.")
    exit()

# Convert to DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by=["num_circuit", "num_qubits_each_circuit", "dataset"])

# Output folder
output_dir = os.path.join("analyze", "all")
os.makedirs(output_dir, exist_ok=True)

# Generate plot and CSV for each metric
for metric in metrics:
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=df,
        x="num_circuit",
        y=metric,
        hue="dataset",
        style="num_qubits_each_circuit",
        markers=True,
        dashes=True,
        palette="tab10",
        linewidth=2,
        markersize=8
    )
    plt.title(metric)
    plt.xlabel("Num Circuits")
    plt.ylabel(metric)
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.legend(title="Dataset & NumQubits", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save plot
    pdf_path = os.path.join(output_dir,"plot", f"{metric}_plot.pdf")
    plt.savefig(pdf_path)
    plt.close()

    # Save data used for this metric to CSV
    csv_data = df[["num_circuit", "num_qubits_each_circuit", "dataset", metric]].dropna()
    csv_path = os.path.join(output_dir, "csv", f"{metric}_data.csv")
    csv_data.to_csv(csv_path, index=False)

    print(f"Saved: {pdf_path} and {csv_path}")