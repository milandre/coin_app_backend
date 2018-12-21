# Project Makefile

SHELL := /bin/bash

development:
	virtualenv -p python3 coin-app-env
	source coin-app-env/bin/activate
	pip install -r requirements.txt
	python manage.py migrate

serve:
	python manage.py runserver