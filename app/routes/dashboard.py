from flask import Blueprint
from flask_login import login_required, current_user

from run import app

dashboard = Blueprint("auth", __name__, url_prefix="/dashboard")

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome {current_user.username}! <a href="/logout">Logout</a>'