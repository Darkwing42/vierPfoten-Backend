import datetime
from mongoengine import *
animal_type = (
    "hund",
    "katze",
    "kleintier"
)

class Animal(EmbeddedDocument):
    name = StringField(max_lenght=200, required=True)
    animal_type = StringField(max_lenght=10, choices=animal_type)

    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)

class Customer(Document):
    last_name = StringField(max_lenght=200, required=True)
    first_name = StringField(max_lenght=200)
    email = EmailField()
    animals = ListField(EmbeddedDocumentField(Animal))
    
    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)
