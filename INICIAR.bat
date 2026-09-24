@echo off
setlocal
cd /d "%~dp0"
title DeliveryGo - Inicializador

echo ========================================
echo          DeliveryGo - Iniciando
echo ========================================

where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON=py"
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo.
        echo ERRO: Python nao foi encontrado.
        echo Instale Python 3.11 ou superior e marque "Add Python to PATH".
        pause
        exit /b 1
    )
    set "PYTHON=python"
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/4] Criando ambiente virtual...
    %PYTHON% -m venv .venv
    if errorlevel 1 goto :erro
)
set "VPY=.venv\Scripts\python.exe"
set "VPIP=.venv\Scripts\pip.exe"
if not exist ".venv\.dependencias_ok" (
    echo [2/4] Instalando dependencias pela primeira vez...
    "%VPY%" -m pip install --upgrade pip
    if errorlevel 1 goto :erro
    "%VPIP%" install -r requirements.txt
    if errorlevel 1 goto :erro
    type nul > ".venv\.dependencias_ok"
) else (
    echo [2/4] Dependencias ja instaladas.
)
if not exist "delivery.db" (
    echo [3/4] Criando e populando banco de dados...
    "%VPY%" seed.py
    if errorlevel 1 goto :erro
) else (
    echo [3/4] Banco de dados existente. Dados preservados.
)
echo [4/4] Abrindo navegador e iniciando servidor...
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:5000"
"%VPY%" run.py
exit /b 0
:erro
echo.
echo Ocorreu um erro durante a inicializacao.
echo Verifique as mensagens acima.
pause
exit /b 1
