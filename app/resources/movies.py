from flask import request
from flask.views import View

from app import db
from app.models import Movie
from app.schemas.movies import movie_list_schema, movie_post_schema


class MoviesList(View):
    methods = ["GET"]

    def dispatch_request(self):
        movies = Movie.query.all()
        result = movie_list_schema.dumps(movies)
        return result.data


class CreateMovie(View):
    methods = ["POST"]

    def dispatch_request(self):
        movie_data = request.json.copy()
        result = movie_post_schema.load(movie_data)
        movie = result.data

        db.session.add(movie)
        db.session.commit()

        return movie_post_schema.dumps(movie)
