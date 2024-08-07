# app/models.py
from mongoengine import Document, StringField
from bson import ObjectId

class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    first_name = StringField()
    last_name = StringField()

    def to_json(self):
        return {
            "id": str(self.id),  # Convert ObjectId to string
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
