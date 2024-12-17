from flask import Flask
from app.database import init_db
from app.routes import user_bp
from flask_uuid import FlaskUUID


# DevelopmentConfig - is the configuration for development, it can be changed to TestingConfig if we want to test, can be Productiononfig if we are set for  production
def create_app(config_objects='config.DevelopmentConfig'):
    app = Flask(__name__)  # to register the name of the project
    # to load configurations in the config file
    app.config.from_object(config_objects)

    init_db(app)  # to initialize the database
    FlaskUUID(app)
    # this is to register the blueprints of the user  , it simply adds user_bp to the application, if i have more than one blueprint i can also add it in similar fashion
    # here /api/v1 is used becaus eof versioning and it is considered a best practice
    app.register_blueprint(user_bp, url_prefix='/api/v1')

    return app
