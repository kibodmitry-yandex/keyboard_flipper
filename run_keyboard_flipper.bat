@echo off
REM Keyboard Flipper - Portable Application Launcher
REM This script starts KeyboardFlipper.exe with proper working directory

setlocal enabledelayedexpansion

REM Get script directory
set SCRIPT_DIR=%~dp0

REM Navigate to script directory
cd /d "%SCRIPT_DIR%"

REM Check if EXE exists in dist folder
if exist "%SCRIPT_DIR%dist\KeyboardFlipper.exe" (
    echo Запуск Keyboard Flipper...
    start "" "%SCRIPT_DIR%dist\KeyboardFlipper.exe"
    echo Keyboard Flipper запущен в системном трее
    echo.
    echo Нажмите Ctrl+Shift+F для переворота раскладки выделенного текста
    echo Конфигурация: %SCRIPT_DIR%keyboard_flipper_config.json
    exit /b 0
) else (
    echo ошибка: KeyboardFlipper.exe не найден
    echo Пожалуйста, соберите приложение с помощью: python build_exe.py
    exit /b 1
)
