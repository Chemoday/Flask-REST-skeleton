from werkzeug.security import generate_password_hash, check_password_hash
from peewee import *

from app import db



class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(max_length=20)
    password_hash = CharField(max_length=128)



    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(password, self.password_hash)

    class Meta:
        db_table = 'users'

MODELS_LIST = [User]