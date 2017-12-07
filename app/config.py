import os
import peewee
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    DATABASE_INFO = 'test.db'
    DATABASE = peewee.SqliteDatabase(DATABASE_INFO)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE = {
        'name': 'test.db',
        'engine': 'peewee.SqliteDatabase'
    }

    @property
    def database_type(self):
        return peewee.SqliteDatabase('test.db')

class ProductionConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE = {
        'name': 'test.db',
        'engine': 'peewee.SqliteDatabase'
    }

config_select = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}