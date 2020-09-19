from flask import Blueprint

app = Blueprint("home", __name__)


@app.route('/')
def index():
    return "This is home"