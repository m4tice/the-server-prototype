# FILE: app/main/routes.py
from flask import render_template

from . import main
from app.models import headers, data


@main.route('/')
def index():
    return "Hello, World!"

@main.route('/wzw')
def wzw():
    """
    warzone's weapone page
    """
    return render_template('main/wzw.html', headers=headers, data=data)
