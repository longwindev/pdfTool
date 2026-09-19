FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr tesseract-ocr-eng tesseract-ocr-vie tesseract-ocr-jpn \
    tesseract-ocr-kor tesseract-ocr-chi-sim tesseract-ocr-fra \
    tesseract-ocr-deu tesseract-ocr-spa tesseract-ocr-por tesseract-ocr-rus \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
# Docker sẽ tự tạo môi trường mới tại đây, tránh được lỗi đường dẫn
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "gunicorn -w 2 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:${PORT:-8000}"]
