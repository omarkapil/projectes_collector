from flask import Blueprint, request, jsonify
from models import db, User, Project, Task, Discussion
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Create a Blueprint for main routes
main = Blueprint('main', __name__)

# Route for user registration
@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])  # Create a new user
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User  registered successfully'}), 201

# Route for user login
@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()  # Find user by username
    if user and user.password == data['password']:  # Check password
        access_token = create_access_token(identity=user.id)  # Create JWT token
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Route to create a new project
@main.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    current_user_id = get_jwt_identity()  # Get current user's ID
    data = request.get_json()
    new_project = Project(title=data['title'], description=data['description'], user_id=current_user_id)  # Create a new project
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully'}), 201

# Route to get all projects
@main.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    current_user_id = get_jwt_identity()  # Get current user's ID
    projects = Project.query.filter_by(user_id=current_user_id).all()  # Get projects for the current user
    return jsonify([{'id': project.id, 'title': project.title, 'description': project.description} for project in projects]), 200