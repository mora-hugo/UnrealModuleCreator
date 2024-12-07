@echo off

if not exist "Output" (
    mkdir "Output"
)

call CreateExecutable.bat "Output" || exit /b

call CreateInstaller.bat "src\setup.iss" || exit /b

echo Build pipeline completed successfully.
pause
exit /b