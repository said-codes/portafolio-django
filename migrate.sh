#!/bin/bash
source .venv/bin/activate  # Si usas un entorno virtual en tu proyecto
python manage.py makemigrations
python manage.py migrate
