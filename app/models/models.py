from peewee import *

from app import db



class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(default='none', max_length=20)

    class Meta:
        db_table = 'users'





MODELS_LIST = [User]