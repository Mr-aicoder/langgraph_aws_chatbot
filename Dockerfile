FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install streamlit requests

COPY . .

# Make our startup shell script executable
RUN chmod +x start.sh

# Change entrypoint to execute our combined startup script
CMD ["./start.sh"]