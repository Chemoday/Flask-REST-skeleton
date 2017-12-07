from flask import Blueprint

auth_api = Blueprint('auth_http', __name__)


from . import views, errors


