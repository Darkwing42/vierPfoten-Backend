import datetime
from mongoengine import *

ANREDE = [
    "Herr",
    "Frau"
]

class Tiere(EmbeddedDocument):
    name = StringField(max_lenght=200, required=True)
    tierart = StringField(max_lenght=200, required=True)
    rasse = StringField(max_lenght=200, required=True)
    medHistory = ListField()
    besonderheiten = ListField()

    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)

class Kunde(Document):
    kundennummer = IntField(required=True)
    titel = StringField(max_lenght=200)
    anrede = StringField(max_length=4, choices=ANREDE)
    nachname = StringField(max_lenght=200, required=True)
    vorname = StringField(max_lenght=200)
    email = EmailField()
    besonderheiten = StringField(max_length=200)
    tiere = ListField(EmbeddedDocumentField(Tiere))
    rabatt = IntField()

    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)
