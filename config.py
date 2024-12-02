import os

# Configuration class for Flask application
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///projects.db'  # SQLite database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Change this to a strong secret key