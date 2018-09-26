from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class ReservierungsListe(Resource):
	def get(self):
		#TODO: get all reservations
		pass
class Reservierung(Resource):
	def get(self):
		#TODO: get a single reservation
		pass
	def post(self):
		#TODO: add reservation
		pass
	def put(self):
		#TODO: update/add reservation
		pass
