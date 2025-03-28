#!/bin/bash

# Lấy đường dẫn hiện tại
CURRENT_DIR=$(pwd)

# Thêm đường dẫn này vào PYTHONPATH nếu chưa có
if [[ ":$PYTHONPATH:" != *":$CURRENT_DIR:"* ]]; then
    export PYTHONPATH="$PYTHONPATH:$CURRENT_DIR"
fi

# Xác nhận với người dùng
echo "[✔] PYTHONPATH has been updated:"
echo "$PYTHONPATH"