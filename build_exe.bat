@echo off
REM ===== Build a single VanAnumodan.exe on a Windows machine =====
REM Requires: Python 3.11+ and (for OCR) Tesseract-OCR installed.
setlocal
cd /d %~dp0
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt pyinstaller
if not exist web mkdir web
echo Copying web UI into .\web ...
for %%F in (index.html help.html rules.json manifest.webmanifest ^
  header-emblem.png logo-full.png icon-180.png icon-192.png icon-512.png icon-any-512.png) do (
  if exist "..\%%F" copy /Y "..\%%F" "web\%%F" >nul
)
REM Optional: bundle Tesseract so the exe is self-contained (self-contained OCR)
if exist "C:\Program Files\Tesseract-OCR\tesseract.exe" (
  echo Bundling Tesseract-OCR ...
  if not exist vendor\tesseract mkdir vendor\tesseract
  xcopy /Y /E "C:\Program Files\Tesseract-OCR\*" "vendor\tesseract\" >nul
)
pyinstaller van_anumodan.spec
echo.
echo Built: dist\VanAnumodan.exe
pause
