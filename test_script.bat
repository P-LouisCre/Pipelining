@echo off
git pull origin staging
pip install -r requirements.txt
python unit_test.py
