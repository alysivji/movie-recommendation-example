from flask import request
from flask.views import View

from app import db
from app.models import Movie
from app.schemas.movies import movies_list_schema, movies_post_schema
from app.utilities import deserialize_request, send_response, serialize_response


class MoviesList(View):
    methods = ["GET"]

    def dispatch_request(self):
        movies = db.query(Movie).all()
        return serialize_response(movies_list_schema, movies)


class MoviesPost(View):
    """Movie Post View
    ---
    summary: Add new movie to database
    tags:
        - Movie
    parameters:
        - in: body
            schema: MovieSchema
    consumes:
        - application/json
    produces:
        - application/json
    responses:
        201:
            description: Movie created successfully
            schema: MovieSchema
        422:
            description: Input body formatting issue
    """

    methods = ["POST"]

    def dispatch_request(self, injected_data=None):
        movie_data = request.json.copy() if injected_data is None else injected_data
        movie = deserialize_request(movies_post_schema, movie_data)

        db.session.add(movie)
        db.session.commit()

        serialized_result = serialize_response(movies_post_schema, movie)
        return send_response(200, data=serialized_result)
