class Config:
    """Base configuration."""
    SECRET_KEY = 'walterriveroprimeraaplicacion'
    JWT_SECRET_KEY = 'RealMadridHayclenMathiasMatheoWalter4geeks20241989199220192014MilagrosLove1962'  # Clave secreta para JWT
    MONGODB_SETTINGS = {
        'db': 'WrBet',
        'host': 'localhost',
        'port': 27017
    }
#    BACKEND_URL = 'http://localhost:5000'  # Añade esta línea para definir la URL del backend
