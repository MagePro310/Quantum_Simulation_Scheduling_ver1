# Legacy Root Files - Archived

## Lý Do Archive

Các file này đã được **di chuyển vào archive** vì:
- Đã được sao chép vào cấu trúc mới: `benchmarks/comparison/config/`
- Giữ lại để tham khảo hoặc rollback nếu cần
- Không nên sử dụng trực tiếp - sử dụng phiên bản trong `benchmarks/` thay vào đó

## Files Được Archive

### Test Scripts (runLoopTest*.py)
- `runLoopTestFFD.py` → Sử dụng: `benchmarks/comparison/config/runLoopTestFFD.py`
- `runLoopTestMTMC.py` → Sử dụng: `benchmarks/comparison/config/runLoopTestMTMC.py`
- `runLoopTestMILQ.py` → Sử dụng: `benchmarks/comparison/config/runLoopTestMILQ.py`
- `runLoopTestNoTaDS.py` → Sử dụng: `benchmarks/comparison/config/runLoopTestNoTaDS.py`

### Jupyter Notebooks (test_algorithm_*.ipynb)
- `test_algorithm_FFD.ipynb` → Sử dụng: `benchmarks/comparison/config/test_algorithm_FFD.ipynb`
- `test_algorithm_MTMC.ipynb` → Sử dụng: `benchmarks/comparison/config/test_algorithm_MTMC.ipynb`
- `test_algorithm_MILQ.ipynb` → Sử dụng: `benchmarks/comparison/config/test_algorithm_MILQ.ipynb`
- `test_algorithm_NoTaDS.ipynb` → Sử dụng: `benchmarks/comparison/config/test_algorithm_NoTaDS.ipynb`

## Ngày Archive
2025-12-31

## Cấu Trúc Mới

Tất cả test files bây giờ nằm trong cấu trúc có tổ chức:

```
benchmarks/
├── comparison/
│   ├── config/
│   │   ├── runLoopTestFFD.py
│   │   ├── runLoopTestMTMC.py
│   │   ├── runLoopTestMILQ.py
│   │   ├── runLoopTestNoTaDS.py
│   │   ├── test_algorithm_FFD.ipynb
│   │   ├── test_algorithm_MTMC.ipynb
│   │   ├── test_algorithm_MILQ.ipynb
│   │   └── test_algorithm_NoTaDS.ipynb
│   └── ...
└── ...
```

## Cách Chạy Tests (Phiên Bản Mới)

```bash
# Activate conda environment
conda activate squan

# Chạy từ config directory
cd benchmarks/comparison/config
python runLoopTestFFD.py 5 8
```

## Khôi Phục Files

Nếu cần khôi phục files:
```bash
cp .archive/legacy_root_files/runLoopTestFFD.py ./
```

**Lưu ý**: Không khuyến khích khôi phục. Sử dụng cấu trúc mới trong `benchmarks/`.
