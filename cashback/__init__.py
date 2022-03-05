from flask import Flask
from flask_migrate import Migrate


from .settings import DATABASE_PATH
from .models import configure as config_db
from .serializers import configure as config_ma
from .cashback import bp_cashback

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    config_db(app)
    config_ma(app)
    Migrate(app, app.db)
    app.register_blueprint(bp_cashback)

    return app
