from werkzeug.security import check_password_hash
from vierPfoten.models.users import User

def authenticate(username, password):
    user = User.objects(username=username).first()
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.objects(user_id=user_id).first()
