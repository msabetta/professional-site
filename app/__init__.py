from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db, login_manager, migrate
from config import Config

db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object("config.Config")
#
#     db.init_app(app)
#
#     from .routes import main
#     app.register_blueprint(main)
#
#     return app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from routes.auth import auth_bp
    from routes.profile import profile_bp
    from routes.network import network_bp
    from routes.feed import feed_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(network_bp)
    app.register_blueprint(feed_bp)

    return app