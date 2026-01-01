# Quantum Scheduling Benchmarks

Hệ thống benchmarking toàn diện để so sánh hiệu suất của các giải thuật lập lịch quantum khác nhau.

## Nhanh Chóng Bắt Đầu

```bash
# Chạy tất cả giải thuật
cd comparison
python comparison_runner.py

# Xem kết quả
cat ../reports/comparison_results.json
```

## Giải Thuật Được Hỗ Trợ

1. **FFD** (First Fit Decreasing) - Heuristic
2. **MTMC** (Multi-Task Multi-Core) - Heuristic
3. **MILQ_extend** (Mixed Integer Linear Programming Extended) - ILP
4. **NoTaDS** (No Task Decomposition Scheduling) - ILP

## Cấu Trúc

- `comparison/` - Tâm trung tâm so sánh & chạy benchmark
- `algorithms/` - Thực hiện các giải thuật
- `reports/` - Báo cáo tổng hợp kết quả

## Chi Tiết

- Xem [USAGE_GUIDE.md](USAGE_GUIDE.md) để hướng dẫn chi tiết
- Xem [comparison/README.md](comparison/README.md) để thông tin về cấu trúc thư mục
- Xem [algorithms/ALGORITHM_DETAILS.md](algorithms/ALGORITHM_DETAILS.md) để chi tiết giải thuật

## Chỉ Số So Sánh

- Execution Time (thời gian thực thi)
- Memory Usage (sử dụng bộ nhớ)
- Solution Quality (chất lượng giải pháp)
- Approximation Ratio (tỉ số xấp xỉ)
- Convergence Speed (tốc độ hội tụ)

