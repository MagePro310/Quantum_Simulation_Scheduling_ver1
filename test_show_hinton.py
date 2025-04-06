from qiskit.quantum_info import DensityMatrix
import numpy as np
import matplotlib.pyplot as plt

# Kết quả đếm (counts)
counts = {'00': 507, '11': 487, '10': 18, '01': 12}

# Tổng số lần đo
total_counts = sum(counts.values())

# Tính toán xác suất cho mỗi trạng thái
probabilities = {key: value / total_counts for key, value in counts.items()}
print("Probabilities:", probabilities)

# Khởi tạo ma trận mật độ (density matrix) từ các xác suất
dim = 4  # Vì hệ thống có 2 qubit, nên ma trận mật độ sẽ có kích thước 4x4

# Khởi tạo ma trận mật độ với kích thước 4x4 (2 qubit)
rho_matrix = np.zeros((dim, dim), dtype=complex)

# Danh sách các trạng thái cơ bản (cho 2 qubit)
basis_states = ['00', '01', '10', '11']

# Xây dựng ma trận mật độ
for state, prob in probabilities.items():
    # Tạo vector trạng thái cơ bản
    state_idx = basis_states.index(state)
    # Cập nhật ma trận mật độ
    rho_matrix[state_idx, state_idx] = prob

# Tạo đối tượng DensityMatrix từ ma trận mật độ
rho = DensityMatrix(rho_matrix)
print("Density Matrix:\n", rho)

# # Trực quan hóa ma trận mật độ bằng Hinton plot
# rho.draw(output='hinton')

# # Hiển thị biểu đồ
# plt.show()

# Trực quan hóa ma trận mật độ bằng qsphere
rho.draw(output='qsphere')

# Hiển thị biểu đồ
plt.show()
