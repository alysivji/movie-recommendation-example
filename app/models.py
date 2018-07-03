from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        onupdate=db.func.current_timestamp(),
        default=db.func.current_timestamp(),
    )

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class User(BaseModel):
    """
    User table
    """

    # Attributes
    email = db.Column(db.String(255), index=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    middle_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    # Relationships
    ratings = db.relationship("Rating", back_populates="user")


class Movie(BaseModel):
    """
    Movies Details Table
    """

    def __repr__(self):
        return f"<Movie: {self.title}>"

    # Attributes
    description = db.Column(db.Text())
    title = db.Column(db.String(255))
    release_year = db.Column(db.Integer())

    # Relationships
    ratings = db.relationship("Rating", back_populates="movie")


class Rating(BaseModel):
    """
    Movie Ratings for user
    """

    # Attributes
    movie_id = db.Column(
        db.Integer(), db.ForeignKey("movie.id", name="fk_rating_movie_id")
    )
    rating = db.Column(db.Integer())
    user_id = db.Column(
        db.Integer(), db.ForeignKey("user.id", name="fk_rating_user_id")
    )

    # Relationships
    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")
