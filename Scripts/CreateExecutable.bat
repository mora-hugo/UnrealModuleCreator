@echo off

call ClearDirectoryContent.bat Output

call python -m PyInstaller --onefile --icon=src/icon.ico --add-data "../Template;Template" ../create_module.py --clean --noconfirm || exit /b

move dist\create_module.exe Output || exit /b

rmdir /s /q build
rmdir /s /q dist
del create_module.spec

echo Build process completed successfully.
