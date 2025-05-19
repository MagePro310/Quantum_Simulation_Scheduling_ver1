import os
import pandas as pd

# Danh sách các file và metric tương ứng
metrics = [
    ("average_fidelity_data.csv", "average_fidelity"),
    ("average_responseTime_data.csv", "average_responseTime"),
    ("average_throughput_data.csv", "average_throughput"),
    ("average_turnaroundTime_data.csv", "average_turnaroundTime"),
    ("average_utilization_data.csv", "average_utilization"),
    ("makespan_data.csv", "makespan"),
    ("sampling_overhead_data.csv", "sampling_overhead"),
    ("scheduler_latency_data.csv", "scheduler_latency"),
]

# Các metric càng lớn càng tốt
bigger_better = {"average_fidelity", "average_utilization"}

# Đảm bảo thư mục output tồn tại
output_dir = "analyze/calculation"
os.makedirs(output_dir, exist_ok=True)

for filename, metric in metrics:
    df = pd.read_csv(f'analyze/all/csv/{filename}')
    # Filter num_circuit from 2 to 5
    df = df[(df['num_circuit'] >= 2) & (df['num_circuit'] <= 4)]
    key_cols = ['num_circuit', 'num_qubits_each_circuit']
    algorithms = df['dataset'].unique()
    num_algorithms = len(algorithms)
    print(f"Đang xử lý {metric} ({filename})")

    def normalize_group(group):
        group = group.copy()
        if metric in bigger_better:
            max_val = group[metric].max()
            group['score'] = group[metric] / max_val if max_val != 0 else 0
            print(f"Max value for {metric} in group: {max_val}")
        else:
            min_val = group[metric].min()
            if min_val < 0:
                print(f"Excluded group with min {metric} < 0: {min_val}")
                return pd.DataFrame()  # Exclude this group
            print(f"Algorithm with minimum {metric} in group: {group.loc[group[metric].idxmin(), 'dataset']}")
            print(f"Min value for {metric} in group: {min_val}")
            group['score'] = min_val / group[metric]
        return group

    df = df.groupby(key_cols, group_keys=False).apply(normalize_group)

    # Average score for each algorithm
    avg_scores = df.groupby('dataset')['score'].mean().reset_index()
    
    # **Thêm bước scale lại ở đây**
    max_score = avg_scores['score'].max()
    avg_scores['final_score'] = avg_scores['score'] / max_score if max_score != 0 else 0

    avg_scores = avg_scores.sort_values('final_score', ascending=False)
    print(f"Trung bình điểm chuẩn hóa cho {metric}:", avg_scores)

    # Save results to CSV
    output_path = os.path.join(output_dir, f'normalized_{metric}.csv')
    avg_scores.to_csv(output_path, index=False)