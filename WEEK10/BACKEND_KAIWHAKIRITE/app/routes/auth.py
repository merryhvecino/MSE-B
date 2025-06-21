from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    # Create new user
    user = User(
        username=data['username'],
        role=data.get('role', 'kaimahi')  # Default to kaimahi if role not specified
    )
    user.set_password(data['password'])
    
    # Only allow rangatira role if no users exist (first user)
    if user.role == 'rangatira' and User.query.count() > 0:
        return jsonify({'error': 'Cannot create admin user'}), 403
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity={
            'user_id': user.id,
            'username': user.username,
            'role': user.role
        })
        return jsonify({
            'access_token': access_token,
            'user': {
                'username': user.username,
                'role': user.role
            }
        }), 200
    
    return jsonify({'error': 'Invalid username or password'}), 401

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200
