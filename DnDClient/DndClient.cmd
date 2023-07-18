@ECHO OFF

:: SET python_path=E:/Application/Python/Python36
SET working_path=D:/Work/MyWork/DarkAndDawn/DnDClient

:: "%python_path%/python.exe" %working_path%/Main.py

python %working_path%/Main.py > Result.txt

PAUSE