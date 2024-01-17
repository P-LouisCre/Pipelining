@echo off
git pull origin main
pip install -r requirements.txt
start cmd /k python app.py
