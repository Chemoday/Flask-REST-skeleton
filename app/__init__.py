from flask import Flask


from app.config import config_select


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_select[config_name])
    config_select[config_name].init_app(app)



    #register blueprints
    from app.blueprint.main import main_bp as main_blueprint

    app.register_blueprint(main_blueprint)


    return app