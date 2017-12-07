from flask import request, abort, jsonify, url_for
from . import auth_api

from app.models.models import User

@auth_api.route('/auth_http/register-user', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.select().where(User.username == username).exists():
        abort(400) # existing user
    user = User.create(username=username,
                       password_hash=password)
    res= jsonify({'username': user.username})
    res.status.code = 200
    return res