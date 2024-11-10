# FILE: app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    from .authentication import authentication_bp

    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(authentication_bp, url_prefix='/auth')

    return app
