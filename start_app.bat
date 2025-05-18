@echo off
echo --- Starting Flask app ---

echo Create a new database named f1_db
pause

REM Downloading required packages

pip install -r requirements.txt

REM Open backend folder

cd backend

REM Start Flask app
echo running run.py

python run.py
echo --- Flask app started ---


