from app.models.post import Post
from app.models.connection import Connection

def get_feed(user_id):
    connections = Connection.query.filter(
        ((Connection.sender_id == user_id) |
         (Connection.receiver_id == user_id)) &
        (Connection.status == "accepted")
    ).all()

    user_ids = {
        c.sender_id if c.sender_id != user_id else c.receiver_id
        for c in connections
    }

    return Post.query.filter(
        Post.author_id.in_(user_ids)
    ).order_by(Post.created_at.desc()).limit(50)

