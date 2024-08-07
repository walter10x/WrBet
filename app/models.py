from mongoengine import Document, StringField
from bson import ObjectId

class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    first_name = StringField()
    last_name = StringField()

    def to_json(self):
        user_dict = self.to_mongo().to_dict()
        user_dict['id'] = str(user_dict['_id'])
        del user_dict['_id']
        return user_dict
