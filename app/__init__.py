import logging.config

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

# create and config app
app = Flask(__name__)
app.config.from_object(Config)

logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))

# set up plugins
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from .models import User  # , Product, Inventory, Price # noqa
from app import routes  # noqa

# beef up flask shell
app.config.update(
    {
        "KONCH_CONTEXT": {
            "db": db,
            "User": User,
            # 'Product': Product,
            # 'Inventory': Inventory,
            # 'Price': Price,
        }
    }
)
