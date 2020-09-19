from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.api import *

def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    app.register_blueprint(home.app)
    app.register_blueprint(dashboard.app)

    return app