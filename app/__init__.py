import logging.config

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .exceptions import DeserializationError, SerializationError
from .utilities import send_response

# create and config app
app = Flask(__name__)
app.config.from_object(Config)

logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))

# set up plugins
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import User  # noqa
from . import routes  # noqa

# beef up flask shell
app.config.update({"KONCH_CONTEXT": {"db": db, "User": User}})


# error handling
@app.errorhandler(DeserializationError)
@app.errorhandler(SerializationError)
def handle_validation_error(error):
    return send_response(error.status_code, error=error.payload)
