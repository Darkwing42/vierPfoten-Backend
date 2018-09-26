from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class KundenListe(Resource):
	def get(self):
		#TODO:get all customers
		pass

class Kunden(Resource):
	def get(self):
		#TODO: get a single customer
		pass
	def post(self):
		#TODO: add a customer
		pass
	def put(self):
		#TODO: change/add customer data
		pass
	def delete(self):
		#TODO: delete customer data
		pass
