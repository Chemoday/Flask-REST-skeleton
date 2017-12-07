import os
from app import create_app


from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)



def connect_db():
    from peewee import SqliteDatabase
    db_lite = SqliteDatabase(app.config['DATABASE']['name'])
    return db_lite

@manager.command
def generate_db_tables():
    from app.models.models import MODELS_LIST
    db_lite = connect_db()
    for model in MODELS_LIST:
        db_lite.create_table(model, safe=True)
    print("Db tables created")

@manager.command
def test_data():
    from app import db
    from app.models.models import User
    from config import TestingConfig
    print(User)
    db.initialize(TestingConfig.DATABASE)
    db.database.connect()
    User.create()
    try:
        User.create()
        print("User created")
        pass
    except:
        return



if __name__ == '__main__':
    manager.run()

