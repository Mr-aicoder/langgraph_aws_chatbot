# Step 1: Use an official, lightweight Python run-time environment
FROM python:3.11-slim

# Step 2: Set the operational directory inside the container
WORKDIR /app

# Step 3: Copy requirements and install them securely
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the application code into the container
COPY . .

# Step 5: Expose Port 8000 for web traffic
EXPOSE 8000

# Step 6: Start the FastAPI web application using Uvicorn
CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8000"]