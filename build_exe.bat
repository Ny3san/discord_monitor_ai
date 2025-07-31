@echo off
pip install pyinstaller
pyinstaller --onefile --windowed interface.py
pause
