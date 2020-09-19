from flask import Blueprint

app = Blueprint("dashboard", __name__)


@app.route('/dashboard')
def index():
    return "This is the dashboard"