# app/models.py
from mongoengine import Document, StringField
from bson import ObjectId

class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    first_name = StringField()
    last_name = StringField()

    def to_json(self):
        user_dict = self.to_mongo().to_dict()
        user_dict['id'] = str(user_dict['_id'])  # Convertir ObjectId a string
        del user_dict['_id']  # Eliminar _id del diccionario de salida
        return user_dict
