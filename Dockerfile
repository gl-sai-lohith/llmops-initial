# Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY config.yaml .

CMD ["python", "server.py"]