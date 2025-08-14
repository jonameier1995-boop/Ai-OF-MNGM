FROM python:3.11-slim
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code kopieren und starten
COPY handler.py .
CMD ["python", "-u", "handler.py"]
