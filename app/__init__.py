from flask import Flask
from mongoengine import connect
from config import Config
from app.routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Conectar a MongoDB
    connect(**app.config['MONGODB_SETTINGS'])

    # Registrar rutas
    app.register_blueprint(routes_bp)

    return app
