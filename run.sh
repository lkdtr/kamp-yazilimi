#!/bin/bash

pyenv virtualenv 3.7.1 venv
pyenv activate venv

cd mudur
python manage.py runserver --insecure
