import subprocess
import sys
import time

print("🚀 Starting Dual-Process AI Application Stack...")

# 1. Start the FastAPI backend on port 8000
backend_process = subprocess.Popen([
    sys.executable, "-m", "uvicorn", "main:app", 
    "--host", "0.0.0.0", "--port", "8000"
])

# 2. Start the Streamlit frontend on port 8501
frontend_process = subprocess.Popen([
    sys.executable, "-m", "streamlit", "run", "frontend.py", 
    "--server.port", "8501", "--server.address", "0.0.0.0"
])

print("🤖 Both processes initiated. Monitoring health...")

try:
    while True:
        # Check if either process has crashed or terminated
        backend_check = backend_process.poll()
        frontend_check = frontend_process.poll()
        
        if backend_check is not None:
            print(f"❌ Backend exited unexpectedly with code {backend_check}")
            sys.exit(1)
            
        if frontend_check is not None:
            print(f"❌ Frontend exited unexpectedly with code {frontend_check}")
            sys.exit(1)
            
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping application processes...")
    backend_process.terminate()
    frontend_process.terminate()