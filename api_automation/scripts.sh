#!/bin/bash
virtualenv -p python3 venv_shell
source venv_shell/bin/activate
pip install -r requirements.txt
ls -lrt
pip freeze
pip list
pytest --version
pytest -v test_reqres.py --html=reports.html
