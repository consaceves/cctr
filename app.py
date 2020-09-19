from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from . import api
    app.register_blueprint(api.home.app)
    app.register_blueprint(api.dashboard.app)

    return app
