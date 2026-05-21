FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install streamlit requests

# CACHE BREAKER: Change this version string to force a fresh file copy
ENV CACHE_BYPASS=v1.0.1

COPY . .

# Run our Python-native process manager
CMD ["python", "run.py"]