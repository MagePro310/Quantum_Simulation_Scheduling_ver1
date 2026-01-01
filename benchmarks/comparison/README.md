# Quantum Scheduling Algorithms - Benchmarking Framework

## Cấu trúc Thư mục

```
benchmarks/
├── comparison/
│   ├── config/                          # Cấu hình benchmark và test files
│   │   ├── benchmark_config.json        # Cấu hình chính
│   │   ├── runLoopTestFFD.py            # Script chạy FFD
│   │   ├── runLoopTestMTMC.py           # Script chạy MTMC
│   │   ├── runLoopTestMILQ.py           # Script chạy MILQ_extend
│   │   ├── runLoopTestNoTaDS.py         # Script chạy NoTaDS
│   │   ├── test_algorithm_FFD.ipynb     # Notebook test FFD
│   │   ├── test_algorithm_MTMC.ipynb    # Notebook test MTMC
│   │   ├── test_algorithm_MILQ.ipynb    # Notebook test MILQ
│   │   └── test_algorithm_NoTaDS.ipynb  # Notebook test NoTaDS
│   ├── results/                         # Kết quả so sánh theo giải thuật
│   │   ├── FFD/                         # Kết quả FFD
│   │   ├── MTMC/                        # Kết quả MTMC
│   │   ├── MILQ_extend/                 # Kết quả MILQ_extend
│   │   └── NoTaDS/                      # Kết quả NoTaDS
│   ├── analysis/                        # Phân tích và so sánh chi tiết
│   │   ├── performance_metrics.json     # Chỉ số hiệu suất
│   │   ├── comparison_analysis.py       # Script phân tích so sánh
│   │   └── visualizations/              # Biểu đồ so sánh
│   ├── comparison_runner.py             # Script chạy tất cả giải thuật
│   └── README.md                        # Tài liệu hướng dẫn
├── algorithms/
│   ├── FFD/                             # Thực hiện FFD
│   │   └── FFD_implement.py
│   ├── MTMC/                            # Thực hiện MTMC
│   └── MILQ_extend/                     # Thực hiện MILQ_extend
│   └── NoTaDS/                          # Thực hiện NoTaDS
└── reports/
    ├── comparison_results.json          # Kết quả so sánh tổng hợp
    └── benchmark_report.html            # Báo cáo HTML

```

## Các Giải Thuật

### 1. **FFD (First Fit Decreasing)** - Heuristic
- **Loại**: Heuristic
- **File thực hiện**: `benchmarks/algorithms/FFD/`
- **Test file**: `benchmarks/comparison/config/test_algorithm_FFD.ipynb`
- **Script chạy**: `benchmarks/comparison/config/runLoopTestFFD.py`
- **Kết quả**: `benchmarks/comparison/results/FFD/`

### 2. **MTMC (Multi-Task Multi-Core)** - Heuristic
- **Loại**: Heuristic
- **File thực hiện**: `benchmarks/algorithms/MTMC/`
- **Test file**: `benchmarks/comparison/config/test_algorithm_MTMC.ipynb`
- **Script chạy**: `benchmarks/comparison/config/runLoopTestMTMC.py`
- **Kết quả**: `benchmarks/comparison/results/MTMC/`

### 3. **MILQ_extend (Mixed Integer Linear Programming Extended)** - ILP
- **Loại**: ILP (Integer Linear Programming)
- **File thực hiện**: `benchmarks/algorithms/MILQ_extend/`
- **Test file**: `benchmarks/comparison/config/test_algorithm_MILQ.ipynb`
- **Script chạy**: `benchmarks/comparison/config/runLoopTestMILQ.py`
- **Kết quả**: `benchmarks/comparison/results/MILQ_extend/`

### 4. **NoTaDS (No Task Decomposition Scheduling)** - ILP
- **Loại**: ILP (Integer Linear Programming)
- **File thực hiện**: `benchmarks/algorithms/NoTaDS/`
- **Test file**: `benchmarks/comparison/config/test_algorithm_NoTaDS.ipynb`
- **Script chạy**: `benchmarks/comparison/config/runLoopTestNoTaDS.py`
- **Kết quả**: `benchmarks/comparison/results/NoTaDS/`

## Cách Sử Dụng

### ⚠️ Điều Kiện Tiên Quyết
```bash
# BẮT BUỘC: Activate conda environment trước
conda activate squan
```

### Chạy Tất Cả Giải Thuật

```bash
cd benchmarks/comparison
python comparison_runner.py
```

### Chạy Một Giải Thuật Cụ Thể

```bash
# FFD
python config/runLoopTestFFD.py

# MTMC
python config/runLoopTestMTMC.py

# MILQ_extend
python config/runLoopTestMILQ.py

# NoTaDS
python config/runLoopTestNoTaDS.py
```

### Kiểm Tra Kết Quả So Sánh

Kết quả được lưu tại:
- `benchmarks/reports/comparison_results.json` - Kết quả tổng hợp
- `benchmarks/comparison/results/{ALGORITHM}/` - Kết quả chi tiết từng giải thuật

## Chỉ Số So Sánh

### Performance Metrics
- **Execution Time** (giây): Thời gian thực thi
- **Memory Usage** (MB): Sử dụng bộ nhớ
- **Solution Quality**: Chất lượng giải pháp
- **Approximation Ratio**: Tỉ số xấp xỉ so với tối ưu lý thuyết
- **Convergence Speed**: Tốc độ hội tụ tới giải pháp

### Benchmark Parameters
- **Circuit Sizes**: small, medium, large
- **Num Qubits**: 5, 10, 15, 20
- **Depth Range**: 10, 50, 100
- **Num Runs**: 10 lần chạy cho mỗi giải thuật
- **Timeout**: 300 giây

## Phân Tích So Sánh

Để phân tích chi tiết kết quả:

```bash
cd benchmarks/comparison/analysis
python comparison_analysis.py
```

## Ghi Chú

- Tất cả kết quả được lưu trong JSON format
- Các biểu đồ so sánh được lưu trong `analysis/visualizations/`
- Báo cáo HTML được tạo tự động trong `reports/benchmark_report.html`

