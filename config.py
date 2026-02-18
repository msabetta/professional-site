import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_DATABASE_URI = os.getenv("DATABASE_URL")
    POSTGRES_SECRET_KEY = os.getenv("SECRET_KEY")
    POSTGRES_TRACK_MODIFICATIONS = False