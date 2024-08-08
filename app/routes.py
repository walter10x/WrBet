# app/routes.py
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from mongoengine.errors import NotUniqueError, DoesNotExist
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

bp = Blueprint('main', __name__)

# Helper function to create JWT token
def create_jwt_token(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=50)
    token = jwt.encode({
        'sub': str(user_id),
        'exp': int(expiration_time.timestamp())
    }, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

# ENDPOINT SIGNUP [POST]
@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    try:
        user = User(
            email=data['email'],
            password=hashed_password,
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        user.save()
        token = create_jwt_token(user.id)
        return jsonify({'message': 'User created', 'token': token}), 201
    except NotUniqueError:
        return jsonify({'message': 'Email already exists'}), 400

# ENDPOINT LOGIN [POST]
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        user = User.objects.get(email=data['email'])
        if not check_password_hash(user.password, data['password']):
            return jsonify({'message': 'Invalid credentials'}), 401
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404

    token = create_jwt_token(user.id)
    return jsonify({'message': 'Login successful', 'token': token}), 200

# ENDPOINT GET USERS [GET]
@bp.route('/api/users', methods=['GET'])

def get_users():
    users = User.objects()
    users_list = [user.to_json() for user in users]
    return jsonify(users_list), 200

# ENDPOINT GET USER BY ID [GET]
@bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    try:
        user = User.objects.get(id=ObjectId(user_id))
        return jsonify(user.to_json()), 200
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500
        

# ENDPOINT CREATE USER [POST]
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        user = User(
            email=data['email'],
            password=data['password'],  # Deberías encriptar la contraseña aquí
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        user.save()
    except NotUniqueError:
        return jsonify({'message': 'Email already exists'}), 400

    return jsonify({'message': 'User created', 'user': user.to_json()}), 201

# ENDPOINT UPDATE USER [PUT]
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
        user.password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    if 'first_name' in data:
        user.first_name = data['first_name']
    
    if 'last_name' in data:
        user.last_name = data['last_name']
    
    user.save()
    return jsonify({'message': 'User updated', 'user': user.to_json()}), 200

# ENDPOINT DELETE USER [DELETE]
@bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.objects.get(id=ObjectId(user_id))
    except DoesNotExist:
        return jsonify({'message': 'User not found'}), 404

    user.delete()
    return jsonify({'message': 'User deleted'}), 200


@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@bp.route('/api/data', methods=['GET'])
def get_data():
    # Aquí puedes hacer una consulta a una base de datos o realizar algún proceso
    data = {'message': 'Hello from Flask! me estan lalamdo desde el back'}
    return jsonify(data)

if __name__ == '__main__':
    bp.run(debug=True)