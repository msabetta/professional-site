from flask import Blueprint

profile_bp = Blueprint("auth", __name__, url_prefix="/profile")