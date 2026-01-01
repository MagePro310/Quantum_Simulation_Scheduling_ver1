# Algorithm Details

## Heuristic Algorithms

### FFD (First Fit Decreasing)
**Mô tả**: Thuật toán heuristic sắp xếp công việc lớn nhất trước tiên vào slot đầu tiên có sẵn.

**Ưu điểm**:
- Thời gian thực thi nhanh
- Dễ hiểu và triển khai
- Không yêu cầu giải quyết bài toán tối ưu hóa phức tạp

**Nhược điểm**:
- Có thể không tìm ra giải pháp tối ưu
- Chất lượng giải pháp phụ thuộc vào thứ tự công việc

---

### MTMC (Multi-Task Multi-Core)
**Mô tả**: Thuật toán heuristic cho các hệ thống đa tác vụ, đa nhân (core).

**Ưu điểm**:
- Tối ưu hóa cho các hệ thống song song
- Cân bằng tải giữa các nhân
- Thích ứng với kiến trúc đa nhân

**Nhược điểm**:
- Phức tạp hơn FFD
- Vẫn là heuristic (không đảm bảo tối ưu toàn cục)

---

## ILP (Integer Linear Programming) Algorithms

### MILQ_extend (Mixed Integer Linear Programming Extended)
**Mô tả**: Thuật toán dựa trên lập trình tuyến tính nguyên với các phần mở rộng.

**Ưu điểm**:
- Tìm giải pháp tối ưu (hoặc gần tối ưu)
- Có tính toán học chặt chẽ
- Xử lý tốt các ràng buộc phức tạp

**Nhược điểm**:
- Thời gian thực thi lâu hơn
- Yêu cầu nhiều tài nguyên tính toán
- Có thể không hoàn thành trong thời gian hợp lý với các bài toán lớn

---

### NoTaDS (No Task Decomposition Scheduling)
**Mô tả**: Thuật toán ILP không phân tách công việc (task decomposition).

**Ưu điểm**:
- Xử lý toàn bộ bài toán một lần
- Tìm giải pháp tối ưu toàn cục
- Tránh mất thông tin do phân tách

**Nhược điểm**:
- Kích thước vấn đề lớn hơn (exponential complexity)
- Thời gian giải quyết có thể rất lâu
- Yêu cầu nhiều bộ nhớ hơn

---

## Tóm Tắt So Sánh

| Thuộc Tính | FFD | MTMC | MILQ_extend | NoTaDS |
|-----------|-----|------|------------|--------|
| **Loại** | Heuristic | Heuristic | ILP | ILP |
| **Tối ưu** | Không | Không | Có/Gần | Có |
| **Tốc độ** | Nhanh | Nhanh | Trung bình | Chậm |
| **Chất lượng** | Trung bình | Tốt | Tốt | Tốt nhất |
| **Scalability** | Tốt | Tốt | Vừa | Kém |
| **Độ phức tạp** | Đơn giản | Trung bình | Cao | Rất cao |

