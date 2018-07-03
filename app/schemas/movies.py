from datetime import datetime

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

CURRENT_YEAR = datetime.now().year


class MovieSchema(Schema):
    # Fields
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    release_year = fields.Int(required=True)
    description = fields.Str(required=True)

    # Validators
    @validates('release_year')
    def validate_release_year(self, data):
        if data > CURRENT_YEAR:
            raise ValidationError("Cannot insert unrelease movie")

    # Loaders
    @post_load
    def make_user(self, data):
        return Movie(**data)


movies_list_schema = MovieSchema(many=True)
movies_post_schema = MovieSchema()
