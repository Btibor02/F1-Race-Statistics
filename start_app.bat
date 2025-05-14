@echo off
echo --- Starting Flask app ---

REM Downloading required packages

pip install -r requirements.txt

REM Open backend folder

cd backend

REM Start Flask app
echo running run.py

python run.py
echo --- Flask app started ---


