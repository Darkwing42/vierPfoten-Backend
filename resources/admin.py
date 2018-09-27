from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required
from Backend.models.users import User
import uuid

class Users(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True,
		help="Dieses Feld kann nicht leer bleiben."
	)

	def get(self):
		#TODO: check if requesting user is Admin else return error message
		data = User.objects()
		if data:
			users = []
			for u in data:
				template = {
					"user_id": str(u.user_id),
					"username": u.username,
					"email": u.email,
					"edit": u.edit,
					"first_name": u.first_name,
					"last_name": u.last_name,
					"role": u.role,
					"created_at": str(u.created_at),
					"modified_at": str(u.modified_at)

				}
				users.append(template)
			return users
		return {"message": "No Users found"}, 404


	def post(self):

		create_id = uuid.uuid4()
		#data = Admin.parser.parse_args()
		data = request.get_json()

		admin = User(
			user_id=create_id,
			username=data['username'],
			password=User.hash_password(data['password']),
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			role=data['role'],
			edit=data['edit']
		)
		admin.save()

		return {'message': "User successfully registered"}, 201

	def put(self):
		#TODO: change/add admin dat
		pass
