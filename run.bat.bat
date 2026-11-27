@echo off
call ".venv\Scripts\activate.bat"
pytest -v -s testClasses\SwagLabLoginTest6_Grouping.py
pause