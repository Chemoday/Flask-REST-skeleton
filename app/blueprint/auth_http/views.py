from flask import request, abort, jsonify, url_for
from . import auth_api

from flask import  Response


from app.models.models import User

@auth_api.route('/auth_http/register', methods = ['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.select().where(User.username == username).exists():
        return Response("{'error':'User with this data is exists'}", status=416, mimetype='application/json')
    user = User.create(username=username,
                       password=password)
    res=jsonify({'username': user.username})

    return res

@auth_api.route('/auth_http/login', methods = ['POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    token = request.json.get('token')

    #Implement token login
    if username is None or password is None:
        abort(406)
    if not User.select().where(User.username == username).exists():
        user = User.get(User.username == username)
        user.verify_password()
        pass
