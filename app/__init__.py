import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)

    appdir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(appdir, 'cctr.db')}"

    with app.app_context():
        from . import models
        db.drop_all()
        db.create_all()

    from . import api
    app.register_blueprint(api.home.app)
    app.register_blueprint(api.dashboard.app)
    app.register_blueprint(api.user.app)
    app.register_blueprint(api.workout.app)

    return app