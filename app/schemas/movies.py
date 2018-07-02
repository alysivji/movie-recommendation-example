from marshmallow import (
    fields,
    post_dump,
    post_load,
    Schema,
    validates,
    validates_schema,
    ValidationError,
)

from app.models import Movie


class MovieSchema(Schema):
    # Fields
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    release_year = fields.Int(required=True)
    description = fields.Str(required=True)

    # Validators

    # Loaders
    @post_load
    def make_user(self, data):
        return Movie(**data)


movie_list_schema = MovieSchema(many=True)
movie_post_schema = MovieSchema()
