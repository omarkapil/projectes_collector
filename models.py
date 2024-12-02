from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the database
db = SQLAlchemy()

# User model to store user information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    projects = db.relationship('Project', backref='owner', lazy=True)

# Project model to store project information
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

# Task model to store tasks related to projects
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Discussion model to store discussions related to projects
class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)