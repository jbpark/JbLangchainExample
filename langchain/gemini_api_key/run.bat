@echo off
set CONDA_ENV_NAME=pygem311

:: Conda 활성화
call conda activate base

:: Conda 환경 목록 확인 후 존재하지 않으면 생성
:: conda create -y -n pygem311 python=3.11
conda info --envs | findstr /C:"%CONDA_ENV_NAME%" >nul
if %errorlevel% neq 0 (
    echo Creating conda environment: %CONDA_ENV_NAME%
    conda create -y -n %CONDA_ENV_NAME% python=3.11
)

:: Conda 환경 활성화
call conda activate %CONDA_ENV_NAME%
