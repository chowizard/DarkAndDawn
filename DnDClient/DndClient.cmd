@ECHO OFF

SET VenvPath=..\.venv
SET PackageListFilePath=..\requirements.txt

IF NOT EXIST %VenvPath% (
    ECHO Install python virtual environment...
    python -m venv %VenvPath%
    CALL %VenvPath%\Scripts\activate.bat
    pip install -r %PackageListFilePath%
) ELSE (
    CALL %VenvPath%\Scripts\activate.bat
)

python .\Main.py

PAUSE
