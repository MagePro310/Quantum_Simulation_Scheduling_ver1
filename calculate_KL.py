import numpy as np

# Kết quả phân phối 1 và phân phối 2
ideal = {'111': 423, '010': 35, '000': 483, '001': 6, '100': 5, '110': 12, '101': 45, '011': 15}
noise = {'111': 510, '000': 514}

# Tổng số lần đo cho mỗi phân phối
total_ideal = sum(ideal.values())
total_noise = sum(noise.values())

# Chuẩn hóa thành xác suất
prob_ideal = {k: v / total_ideal for k, v in ideal.items()}
prob_noise = {k: v / total_noise for k, v in noise.items()}

# Đảm bảo hai phân phối có cùng các kết quả (các khoá giống nhau)
all_keys = set(prob_ideal.keys()).union(set(prob_noise.keys()))
for key in all_keys:
    prob_ideal.setdefault(key, 0)
    prob_noise.setdefault(key, 0)

# Tính KL Divergence
kl_divergence = sum(prob_ideal[key] * np.log(prob_ideal[key] / prob_noise[key]) for key in all_keys if prob_ideal[key] > 0 and prob_noise[key] > 0)

print(f"Kullback-Leibler Divergence: {kl_divergence}")

from scipy.stats import chisquare

# Các giá trị tần suất (quantities) trong phân phối
observed = list(ideal.values())
expected = [noise.get(key, 0) for key in ideal.keys()]

# Tính Chi-square test
chi2_stat, p_value = chisquare(observed, expected)

print(f"Chi-square statistic: {chi2_stat}, p-value: {p_value}")
