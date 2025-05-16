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
    key_cols = ['num_circuit', 'num_qubits_each_circuit']
    algorithms = df['dataset'].unique()
    num_algorithms = len(algorithms)
    print(f"Đang xử lý {metric} ({filename})")

    output_path = os.path.join(output_dir, f'output_{metric}.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        def assign_points(group):
            if len(group['dataset'].unique()) < num_algorithms:
                print(
                    f"BỎ QUA nhóm {group['num_circuit'].iloc[0]} mạch, {group['num_qubits_each_circuit'].iloc[0]} qubit vì thiếu thuật toán.",
                    file=f
                )
                return None
            group = group.copy()
            ascending = False if metric in bigger_better else True
            group['rank'] = group[metric].rank(method='min', ascending=ascending)
            group['points'] = num_algorithms - group['rank'] + 1
            print(f"Điểm cho nhóm {group['num_circuit'].iloc[0]} mạch, {group['num_qubits_each_circuit'].iloc[0]} qubit:", file=f)
            print(group[['dataset', metric, 'rank', 'points']], file=f)
            return group

        grouped = df.groupby(key_cols, group_keys=False)
        results = []
        for _, group in grouped:
            res = assign_points(group)
            if res is not None:
                results.append(res)
        if results:
            df_points = pd.concat(results, ignore_index=True)
            print("Tổng điểm từng thuật toán:", file=f)
            total_points = df_points.groupby('dataset')['points'].sum().reset_index()
            print(total_points, file=f)

            min_points = total_points['points'].min()
            total_points['normalized_score'] = total_points['points'] / min_points

            print("\nChuẩn hóa điểm (points/min):", file=f)
            print(total_points[['dataset', 'points', 'normalized_score']], file=f)

            total_points['rank'] = total_points['points'].rank(method='min', ascending=False)
            total_points['final_rank'] = num_algorithms - total_points['rank'] + 1
            print("\nXếp hạng thuật toán (tốt nhất là 4, tệ nhất là 1):", file=f)
            print(total_points[['dataset', 'points', 'final_rank']], file=f)

            # Save results to CSV
            csv_output_path = os.path.join(output_dir, f'result_{metric}.csv')
            total_points[['dataset', 'final_rank', 'normalized_score']].to_csv(csv_output_path, index=False)
        else:
            print("Không có nhóm hợp lệ để tính điểm.", file=f)