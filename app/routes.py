# app/routes.py
from flask import Blueprint, request, jsonify
from app.models import User
from mongoengine.errors import NotUniqueError

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validar que los datos necesarios están presentes
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        # Crear un nuevo usuario
        user = User(
            email=data['email'],
            password=data['password'],  # En un caso real, deberías encriptar la contraseña
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )

        user.save()  # Guardar el usuario en la base de datos

    except NotUniqueError:
        return jsonify({'message': 'Email already exists'}), 400

    # Usar el método to_json para la serialización
    return jsonify({'message': 'User created', 'user': user.to_json()}), 201


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.objects()
    users_list = [user.to_json() for user in users]
    return jsonify(users_list), 200
