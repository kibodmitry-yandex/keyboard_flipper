@echo off
REM Create Windows startup shortcut for Keyboard Flipper
REM Run this as Administrator to add to autostart

setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set EXE_PATH=%SCRIPT_DIR%dist\KeyboardFlipper.exe
set CONFIG_PATH=%SCRIPT_DIR%keyboard_flipper_config.json
set STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_PATH=%STARTUP_DIR%\Keyboard Flipper.lnk

echo.
echo Keyboard Flipper Autostart Setup
echo ==================================
echo.

REM Check if EXE exists
if not exist "%EXE_PATH%" (
    echo ошибка: KeyboardFlipper.exe не найден в %EXE_PATH%
    echo Пожалуйста, соберите приложение с помощью: python build_exe.py
    pause
    exit /b 1
)

REM Check for admin rights (optional check for future use)
echo.
echo EXE path: %EXE_PATH%
echo Startup folder: %STARTUP_DIR%
echo.

REM Create VBScript to make shortcut (workaround for Windows)
set VBS_SCRIPT=%TEMP%\CreateShortcut.vbs

(
    echo Set oWS = WScript.CreateObject("WScript.Shell"^)
    echo sLinkFile = "%SHORTCUT_PATH%"
    echo Set oLink = oWS.CreateShortcut(sLinkFile^)
    echo oLink.TargetPath = "%EXE_PATH%"
    echo oLink.WorkingDirectory = "%SCRIPT_DIR%"
    echo oLink.Description = "Keyboard Flipper - Text Layout Converter"
    echo oLink.Save
) > "%VBS_SCRIPT%"

REM Run VBScript
cscript //nologo "%VBS_SCRIPT%"

if exist "%SHORTCUT_PATH%" (
    echo ✓ Ярлык создан: %SHORTCUT_PATH%
    echo ✓ Keyboard Flipper будет запускаться при старте Windows
    echo.
    echo Для удаления из автозагрузки - удалите ярлык из:
    echo %STARTUP_DIR%
) else (
    echo ошибка: Не удалось создать ярлык
)

REM Cleanup
del "%VBS_SCRIPT%"
echo.
pause
