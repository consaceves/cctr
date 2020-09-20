import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    heroku = Heroku(app)

    with app.app_context():
        from . import models
        db.drop_all()
        db.create_all()

    from . import api
    app.register_blueprint(api.home.app)
    app.register_blueprint(api.dashboard.app)
    app.register_blueprint(api.user.app)
    app.register_blueprint(api.workout.app)
    app.register_blueprint(api.sms.app)

    return app