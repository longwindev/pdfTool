# Định nghĩa các biến môi trường
PYTHON = venv/bin/python
PIP = venv/bin/pip
UVICORN = uvicorn
APP_MODULE = app.main:app

# Ngôn ngữ mặc định nếu người dùng không truyền tham số "lang="
lang ?= en

.PHONY: help run install i18n-extract i18n-init i18n-update i18n-compile clean

help:
	@echo "====== Các lệnh rút gọn cho dự án FastAPI ======"
	@echo "make run          : Khởi chạy server FastAPI"
	@echo "make install      : Cài đặt các thư viện từ requirements.txt"
	@echo "make i18n-extract  : Quét và trích xuất các chữ cần dịch ra file .pot"
	@echo "make i18n-init lang=xx : Khởi tạo ngôn ngữ mới (Ví dụ: make i18n-init lang=en)"
	@echo "make i18n-update   : Cập nhật chữ mới quét vào TẤT CẢ các ngôn ngữ hiện có"
	@echo "make i18n-compile  : Biên dịch file .po sang .mo để hệ thống nhận bản dịch"
	@echo "make clean         : Dọn dẹp các file cache thừa (__pycache__)"
	@echo "================================================"

run:
	$(UVICORN) $(APP_MODULE) --reload --host 0.0.0.0 --port 8000

install:
	. venv/bin/activate && pip install -r requirements.txt

i18n-extract:
	pybabel extract -F babel.cfg -o messages.pot .

# Lệnh khởi tạo một ngôn ngữ cụ thể (Truyền tham số lang=...)
i18n-init:
	@if [ ! -d "translations" ]; then mkdir translations; fi
	pybabel init -i messages.pot -d translations -l $(lang)

# Lệnh cực kỳ quan trọng: Đồng bộ chữ mới trích xuất vào tất cả các ngôn ngữ hiện tại
i18n-update:
	pybabel update -i messages.pot -d translations

i18n-compile:
	pybabel compile -d translations

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete