@echo off
REM Always use this project's venv so pip and uvicorn share the same Python.
cd /d "%~dp0"
if not exist "venv\Scripts\python.exe" (
  echo No venv found. Create one with:  python -m venv venv
  echo Then run this script again.
  exit /b 1
)
call venv\Scripts\activate.bat
python -m pip install -r requirements.txt -q

REM WinError 10013 = port 8000 already in use. Free it before starting.
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000" ^| findstr "LISTENING"') do (
  echo Port 8000 is in use by PID %%a. Stopping that process...
  taskkill /PID %%a /F >nul 2>&1
  timeout /t 2 /nobreak >nul
)

python -m uvicorn app:api --reload --host 127.0.0.1 --port 8000
