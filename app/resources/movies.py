from flask import request
from flask.views import View

from app import db
from app.models import Movie
from app.schemas.movies import movies_list_schema, movies_post_schema
from app.utilities import send_response


class MoviesList(View):
    methods = ["GET"]

    def dispatch_request(self):
        movies = Movie.query.all()
        result = movies_list_schema.dumps(movies)
        return result.data


class CreateMovie(View):
    methods = ["POST"]

    def dispatch_request(self, injected_data=None):
        movie_data = request.json.copy() if injected_data is None else injected_data
        unserialized_result = movies_post_schema.load(movie_data)

        if unserialized_result.errors:
            return send_response(422, error=unserialized_result.errors)

        movie = unserialized_result.data
        db.session.add(movie)
        db.session.commit()

        serialized_result = movies_post_schema.dumps(movie)

        if serialized_result.errors:
            # log what error we had, also send it back
            return send_response(500, error=serialized_result.errors)

        return send_response(200, data=serialized_result.data)
