from flask import Flask
from models import db
from routes import main
from config import Config
from flask_jwt_extended import JWTManager

# Initialize the Flask application
app = Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)

app.config.from_object(Config)  # Load configuration
db.init_app(app)  # Initialize the database
jwt = JWTManager(app)  # Initialize JWT manager

# Register the main blueprint
app.register_blueprint(main)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode

print("App is running!")
print("Configuration loaded.")
print("Database initialized.")
print("App is running!")
