from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required
from Backend.models.kunden import Kunde

class KundenListe(Resource):
	def get(self):
		try:
			data = Kunde.objects()
		except:
			return {"message": "Keine Kunden vorhanden"}, 404

		if data:
			kunden = []

			for k in data:
				tiere = []
				for tier in k.tiere:
					besonderheiten =[]
					medHistory = []
					tier_template = {
						"name": tier.name,
						"tierart": tier.tierart,
						"rasse": tier.rasse,
						"created_at": str(u.created_at),
						"modified_at": str(u.modified_at),
						"medHistory": medHistory.append(x for x in tier.medHistory),
						"besonderheiten": besonderheiten.append(x for x in tier.besonderheiten)
					}
					tiere.append(tier_template)

				template = {
					"kundennumer": k.kundennummer,
					"titel": k.titel,
					"anrede": k.anrede,
					"nachname": k.nachname,
					"vorname": k.vorname,
					"email": k.email,
					"besonderheiten": k.besonderheiten,
					"rabatt": k.rabatt,
					"created_at": str(k.created_at),
					"modified_at": str(k.modified_at),
					"tiere": tiere
				}
				kunden.append(template)
			return kunden, 201
		return {"message": "Keine Kunden gefunden"}, 404

class Kunde(Resource):
	def get(self, kundennummer):
		#TODO: get a single customer
		pass
	def post(self):

		#TODO: add a customer
		data = request.get_json()
		kunde = Kunde(
			kundennummer=101,
			titel=data['titel']
		)




		return {'message': 'Kunde erfolgreich gespeichert', 'data': data}, 201

	def put(self, kundennummer):
		#TODO: change/add customer data
		pass
	def delete(self, kundennummer):
		#TODO: delete customer data
		pass
