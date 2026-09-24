@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Execute INICIAR.bat pelo menos uma vez antes de gerar o EXE.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" -m pip install pyinstaller
if errorlevel 1 goto :erro
".venv\Scripts\python.exe" -m PyInstaller --noconfirm --clean --name DeliveryGo --onedir --add-data "app\templates;app\templates" --add-data "app\static;app\static" desktop_launcher.py
if errorlevel 1 goto :erro
echo.
echo EXE criado em dist\DeliveryGo\DeliveryGo.exe
pause
exit /b 0
:erro
echo Falha ao gerar executavel.
pause
exit /b 1
