@echo off

REM Verificar si Python está instalado
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Instalando Python...
    REM Descargar instalador de Python
    bitsadmin /transfer pythonInstaller https://www.python.org/ftp/python/3.8.12/python-3.8.12.exe "%CD%\python-installer.exe"
    REM Instalar Python
    %CD%\python-installer.exe /quiet
)

REM Verificar si Pipenv está instalado
where pipenv >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Instalando Pipenv...
    REM Instalar Pipenv
    python -m pip install pipenv
)

REM Instalar las dependencias del proyecto
pipenv install
