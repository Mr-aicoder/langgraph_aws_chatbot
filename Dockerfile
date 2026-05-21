FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install streamlit requests

COPY . .

# Run our Python-native process manager
CMD ["python", "run.py"]