@echo off
if "%~1"=="" (
    echo Usage: ClearDirectory.bat "<directory_path>"
    exit /b 1
)

if exist "%~1" (
    rmdir /s /q "%~1\*" >nul 2>&1
    del /q "%~1\*" >nul 2>&1
    echo The contents of "%~1" have been cleared.
) else (
    echo Error: The directory "%~1" does not exist.
)
exit /b
