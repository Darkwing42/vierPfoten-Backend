import datetime
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash


ROLES = (
    "admin",
    "mitarbeiter"
)
class User(Document):
    user_id = DynamicField(max_length=200, required=True)
    username = StringField(max_length=200, required=True)
    email = EmailField(max_length=200, required=True)
    password = StringField(max_length=256,required=True)

    first_name = StringField(max_lenght=100)
    last_name = StringField(max_length=100)
    role = StringField(max_lenght=11, choices=ROLES)

    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)
    edit = BooleanField(default=False)

    @staticmethod
    def hash_password(password):
        new_pw = generate_password_hash(password)
        return new_pw


    @classmethod
    def get_all(cls):
        obj = cls.objects
