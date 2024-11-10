@echo off

REM Create directories
mkdir my_flask_app
mkdir my_flask_app\app
mkdir my_flask_app\app\main

REM Create files
type nul > my_flask_app\app\__init__.py
type nul > my_flask_app\app\main\__init__.py
type nul > my_flask_app\app\main\routes.py
type nul > my_flask_app\requirements.txt
type nul > my_flask_app\run.py

echo Directory structure created successfully.