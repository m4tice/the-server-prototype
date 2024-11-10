from . import authentication_bp

from flask import render_template

@authentication_bp.route('/')
def login():
    return render_template('authentication/authentication.html')