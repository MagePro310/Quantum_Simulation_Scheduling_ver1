# Hướng Dẫn Sử Dụng Cấu Trúc Benchmarking

## Tổng Quan

Hệ thống benchmarking mới được tổ chức để dễ dàng so sánh hiệu suất giữa 4 giải thuật lập lịch quantum:
- **FFD** (First Fit Decreasing) - Heuristic
- **MTMC** (Multi-Task Multi-Core) - Heuristic
- **MILQ_extend** (ILP Extended) - ILP
- **NoTaDS** (No Task Decomposition) - ILP

## Cấu Trúc Thư Mục

```
benchmarks/
├── comparison/              # Trung tâm so sánh giải thuật
│   ├── config/             # Cấu hình & test scripts
│   ├── results/            # Kết quả từ mỗi giải thuật
│   ├── analysis/           # Công cụ phân tích
│   ├── comparison_runner.py # Chạy tất cả giải thuật
│   └── README.md
├── algorithms/             # Thực hiện giải thuật
│   ├── FFD/
│   ├── MTMC/
│   ├── MILQ_extend/
│   ├── NoTaDS/
│   └── ALGORITHM_DETAILS.md
└── reports/                # Báo cáo tổng hợp
```

## Cách Sử Dụng

### ⚠️ QUAN TRỌNG: Conda Environment

**Phải activate conda environment trước khi chạy bất kỳ lệnh nào:**
```bash
conda activate squan
```

Nếu chưa có environment, tạo và cài đặt dependencies:
```bash
conda create -n squan python=3.10
conda activate squan
pip install qiskit qiskit-aer qiskit-ibm-runtime qiskit-addon-cutting pulp matplotlib numpy
```

### 1. Chạy Tất Cả Giải Thuật Cùng Lúc

```bash
cd benchmarks/comparison
python comparison_runner.py
```

Lệnh này sẽ:
- Chạy lần lượt tất cả 4 giải thuật
- Thu thập chỉ số hiệu suất
- Lưu kết quả vào `reports/comparison_results.json`
- In ra bảng so sánh tóm tắt

### 2. Chạy Một Giải Thuật Cụ Thể

```bash
cd benchmarks/comparison/config

# Chạy FFD
python runLoopTestFFD.py

# Chạy MTMC
python runLoopTestMTMC.py

# Chạy MILQ_extend
python runLoopTestMILQ.py

# Chạy NoTaDS
python runLoopTestNoTaDS.py
```

### 3. Kiểm Tra Kết Quả Chi Tiết

```bash
cd benchmarks/comparison/results

# Xem kết quả FFD
ls -la FFD/

# Xem kết quả MTMC
ls -la MTMC/

# Xem kết quả ILP
ls -la MILQ_extend/
ls -la NoTaDS/
```

### 4. Phân Tích So Sánh

```bash
cd benchmarks/comparison/analysis
python comparison_analysis.py
```

Câu lệnh này sẽ tạo báo cáo phân tích với:
- Chỉ số hiệu suất so sánh
- Biểu đồ visualizations
- Bảng tóm tắt

## Chỉ Số So Sánh (Metrics)

### Performance Metrics
- **Execution Time**: Thời gian thực thi (giây)
- **Memory Usage**: Sử dụng bộ nhớ (MB)
- **Solution Quality**: Chất lượng giải pháp
- **Approximation Ratio**: Tỉ số so với tối ưu
- **Convergence Speed**: Tốc độ hội tụ

### Test Parameters
- **Circuit Sizes**: small, medium, large
- **Num Qubits**: 5, 10, 15, 20
- **Depth Range**: 10, 50, 100
- **Num Runs**: 10 lần chạy
- **Timeout**: 300 giây mỗi chạy

## Các Tệp Cấu Hình

### benchmark_config.json
Chứa:
- Thông tin chi tiết về mỗi giải thuật
- Các tham số benchmark
- Đường dẫn output

```json
{
  "algorithms": {
    "FFD": { "name": "First Fit Decreasing", ... },
    "MTMC": { "name": "Multi-Task Multi-Core", ... },
    ...
  }
}
```

## Vị Trí Lưu Kết Quả

### Kết Quả Chi Tiết Từng Giải Thuật
- `benchmarks/comparison/results/FFD/` - Kết quả FFD
- `benchmarks/comparison/results/MTMC/` - Kết quả MTMC
- `benchmarks/comparison/results/MILQ_extend/` - Kết quả MILQ_extend
- `benchmarks/comparison/results/NoTaDS/` - Kết quả NoTaDS

### Báo Cáo So Sánh Tổng Hợp
- `benchmarks/reports/comparison_results.json` - Kết quả tổng hợp
- `benchmarks/comparison/analysis/performance_metrics.json` - Chỉ số hiệu suất

## Kịch Bản Sử Dụng Phổ Biến

### Scenario 1: So Sánh Nhanh 4 Giải Thuật

```bash
cd benchmarks/comparison
python comparison_runner.py
# Xem kết quả trong reports/comparison_results.json
```

### Scenario 2: Phân Tích Chi Tiết Một Giải Thuật

```bash
cd benchmarks/comparison/config
python runLoopTestFFD.py
# Xem kết quả chi tiết trong ../results/FFD/
```

### Scenario 3: Tạo Báo Cáo So Sánh Toàn Bộ

```bash
# Bước 1: Chạy tất cả giải thuật
cd benchmarks/comparison
python comparison_runner.py

# Bước 2: Phân tích kết quả
cd analysis
python comparison_analysis.py

# Bước 3: Xem báo cáo
cat performance_metrics.json
```

## Tự Động Hóa (Tùy Chọn)

### Tạo Script Chạy Tất Cả

```bash
#!/bin/bash
cd /path/to/benchmarks/comparison

# Chạy tất cả
echo "Running FFD..."
python config/runLoopTestFFD.py

echo "Running MTMC..."
python config/runLoopTestMTMC.py

echo "Running MILQ_extend..."
python config/runLoopTestMILQ.py

echo "Running NoTaDS..."
python config/runLoopTestNoTaDS.py

echo "Analyzing results..."
python analysis/comparison_analysis.py

echo "Done!"
```

### 4. Tạo Biểu Đồ So Sánh (VISUALIZATION)

**MỚI**: Sau khi chạy benchmarks, tạo các biểu đồ so sánh trực quan:

```bash
# Từ benchmarks/comparison
python visualize_results.py

# Hoặc sử dụng utility script từ thư mục gốc
./run.sh visualize
```

**Các biểu đồ được tạo:**
- 📊 Metrics Comparison Bar Chart - So sánh tất cả metrics
- 📊 Makespan Comparison - So sánh thời gian hoàn thành
- 📊 Utilization vs Fidelity Scatter Plot - Trade-off analysis
- 📊 Performance Radar Chart - Tổng quan hiệu suất
- 📊 Gantt Charts - Timeline lập lịch công việc
- 📄 Summary Report - Báo cáo chi tiết dạng text

**Kết quả được lưu trong:** `benchmarks/comparison/reports/`

**Tạo biểu đồ cụ thể:**

```bash
# Chỉ tạo radar chart
./run.sh visualize-chart radar

# Chỉ tạo makespan comparison
./run.sh visualize-chart makespan

# Chỉ tạo Gantt chart
./run.sh visualize-chart gantt

# Các tùy chọn: all, metrics, makespan, scatter, radar, gantt, report
```

**Xem hướng dẫn chi tiết:**
- `benchmarks/comparison/VISUALIZATION_GUIDE.txt` - Quick guide
- `benchmarks/comparison/analysis/README.md` - Tài liệu đầy đủ

## Thêm Giải Thuật Mới

Để thêm một giải thuật mới:

1. Tạo thư mục: `benchmarks/algorithms/NEW_ALGORITHM/`
2. Thêm file implement: `NEW_ALGORITHM_implement.py`
3. Tạo folder kết quả: `benchmarks/comparison/results/NEW_ALGORITHM/`
4. Thêm test file vào: `benchmarks/comparison/config/test_algorithm_NEW.ipynb`
5. Cập nhật `benchmark_config.json`:

```json
{
  "algorithms": {
    "NEW_ALGORITHM": {
      "name": "New Algorithm Name",
      "type": "heuristic|ilp",
      "description": "...",
      "test_file": "test_algorithm_NEW.ipynb",
      "run_file": "runLoopTestNEW.py"
    }
  }
}
```

## Xử Sự Cố

### Vấn đề: ImportError khi chạy script

**Giải pháp**: 
```bash
cd benchmarks/comparison
# Hoặc từ thư mục gốc
python -m benchmarks.comparison.comparison_runner
```

### Vấn đề: Kết quả trống

**Giải pháp**:
- Kiểm tra các script test có chính xác không
- Kiểm tra dữ liệu input có hợp lệ không
- Xem log chi tiết trong console

### Vấn đề: Chạy quá lâu

**Giải pháp**:
- Giảm số lượng benchmark runs
- Giảm kích thước circuit
- Chạy một giải thuật thay vì tất cả

## Liên Hệ & Hỗ Trợ

Để thêm tính năng hoặc báo cáo lỗi, vui lòng kiểm tra:
- Các file config trong `config/`
- Các script phân tích trong `analysis/`
- Log output từ các lệnh chạy

