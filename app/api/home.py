from flask import Blueprint

app = Blueprint("home", __name__)


@app.route('/')
def index():
    return "This is home"

@app.route('/login')
def login():
    return True

@app.route('/logout')
def logout():
    # oidc.logout()
    return True