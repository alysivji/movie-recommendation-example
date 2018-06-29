from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, index=True, nullable=False, default=datetime.utcnow
    )
    date_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class User(BaseModel):
    """
    User table
    """

    ############
    # Attributes
    ############
    email = db.Column(db.String(255), index=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    middle_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
