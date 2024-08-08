from flask import Flask
from flask_cors import CORS  # Importa CORS
from mongoengine import connect
from config import Config
from app.routes import bp as routes_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configura CORS
    CORS(app)  # Permite CORS para todas las rutas

    # Conectar a MongoDB
    connect(**app.config['MONGODB_SETTINGS'])

    # Configurar JWT
    jwt = JWTManager(app)

    # Registrar rutas
    app.register_blueprint(routes_bp)

    return app
