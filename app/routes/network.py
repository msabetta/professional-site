from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models.connection import Connection
from app.extensions import db

network_bp = Blueprint("network", __name__, url_prefix="/api/network")

@network_bp.route("/request/<int:user_id>", methods=["POST"])
@login_required
def send_request(user_id):
    conn = Connection(
        sender_id=current_user.id,
        receiver_id=user_id
    )
    db.session.add(conn)
    db.session.commit()

    return jsonify({"message": "Connection request sent"})


@network_bp.route("/accept/<int:connection_id>", methods=["POST"])
@login_required
def accept_request(connection_id):
    conn = Connection.query.get_or_404(connection_id)
    conn.status = "accepted"
    db.session.commit()

    return jsonify({"message": "Connection accepted"})
