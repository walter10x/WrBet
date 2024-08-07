from flask import Blueprint, request, jsonify
from app.models import User
from mongoengine.errors import NotUniqueError, DoesNotExist
from bson import ObjectId

bp = Blueprint('main', __name__)

# ENDPOINT GET USERS [GET]
@bp.route('/users', methods=['GET'])
def get_users():
    users = User.objects()
    users_list = [user.to_json() for user in users]
    return jsonify(users_list), 200

# ENDPOINT GET USERS(ID) [GET]
@bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.objects.get(id=ObjectId(user_id))
        return jsonify(user.to_json()), 200
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# ENDPOINT CREATE USERS [POST]
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        user = User(
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        user.save()
    except NotUniqueError:
        return jsonify({'message': 'Email already exists'}), 400

    return jsonify({'message': 'User created', 'user': user.to_json()}), 201

# ENDPOINT MODIFY USER [PUT]
@bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        user = User.objects.get(id=ObjectId(user_id))
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404

    if 'email' in data:
        user.email = data['email']
    
    if 'password' in data:
        # En un caso real, deberías encriptar la contraseña
        user.password = data['password']
    
    if 'first_name' in data:
        user.first_name = data['first_name']
    
    if 'last_name' in data:
        user.last_name = data['last_name']
    
    user.save()
    return jsonify({'message': 'User updated', 'user': user.to_json()}), 200


# ENDPOINT DELETE USER(ID) [DELETE]
@bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.objects.get(id=ObjectId(user_id))
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404

    user.delete()
    return jsonify({'message': 'User deleted'}), 200
