@echo off
git pull origin main
pip install -r requirements.txt
python run_app.py
