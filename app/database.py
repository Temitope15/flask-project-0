from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

# the code below will activate the sqlAlchemy db and Marshmallow for schema validation, serialization and deserialization


def init_db(app):
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()  # to create the tables as specified in the model
