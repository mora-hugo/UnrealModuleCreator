@echo off
if "%~1"=="" (
    echo Usage: CreateInstaller.bat "<path_to_iss_file>"
    exit /b 1
)

if not exist "%~1" (
    echo Error: The installer script "%~1" does not exist.
    exit /b 1
)

call "ISCC" "%~1" || (
    echo Error: Failed to create the installer from "%~1".
    exit /b 1
)

echo Installer created successfully from "%~1".
exit /b
