@echo off
REM ===== Van Anumodan - run on Windows with Python installed =====
setlocal
cd /d %~dp0
if not exist .venv (
  echo Creating a local Python environment (first run only)...
  python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
echo.
echo Starting Van Anumodan... your browser will open automatically.
python app.py
pause
