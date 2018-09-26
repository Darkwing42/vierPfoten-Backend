from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from mongoengine import *


from vierPfoten.security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'Generate_here_a_secret_key'

jwt = JWT(app, authenticate, identity) #/auth is generated automatically

CORS(app, resources={r"/api/*": {"origins": "*"}})

#TODO: generate secret key

#DATABASE DATA
DB_NAME = "mongo_rest"
DB_HOST = "ds119072.mlab.com"
DB_PORT = 19072
DB_USERNAME = "mongo_user"
DB_PASSWORD = "test2345"


#DATABASE CONNECTION
connect(
    db=DB_NAME,
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)



#resource import
from vierPfoten.resources.admin import Users


url_prefix = "/api/v1"

api.add_resource(Users, url_prefix + '/admin')
