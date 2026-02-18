from flask import request
from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models.post import Post
from app.services.feed_service import get_feed

feed_bp = Blueprint("feed", __name__, url_prefix="/api/feed")

@feed_bp.route("/", methods=["GET"])
@login_required
def feed():
    posts = get_feed(current_user.id)
    return jsonify([
        {
            "id": p.id,
            "content": p.content,
            "author_id": p.author_id,
            "created_at": p.created_at
        }
        for p in posts
    ])

@feed_bp.route("/post", methods=["POST"])
@login_required
def create_post():
    data = request.json
    post = Post(
        content=data["content"],
        author_id=current_user.id
    )
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "Post created"}), 201