from marshmallow import (
    fields,
    post_dump,
    post_load,
    Schema,
    validates,
    validates_schema,
    ValidationError,
)
from marshmallow.validate import Email

from app.constants import DEFAULT_PAGE_SIZE
from app.models import User


class UserListSchema(Schema):
    # Fields
    page = fields.Int(load_only=True, default=1)
    limit = fields.Int(load_only=True, default=DEFAULT_PAGE_SIZE)

    # Validators
    def validate_page(self, data):
        if data < 1:
            raise ValidationError('Expecting page to be larger than 0')

    @validates('limit')
    def validate_limit(self, data):
        if data < 1 or data > 100:
            raise ValidationError('Expecting limit to be between 1-100')

    # Loaders
    @post_dump
    def get_users(self, data):
        users_query = User.query.all()
        return users_query


class UserSchema(Schema):
    # Fields
    email = fields.Email(required=True, validate=Email())
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    middle_name = fields.Str()
    password = fields.Str(required=True)

    # Validators

    # Loaders
    @post_load
    def make_user(self, data):
        return User(**data)


user_list_schema = UserSchema(many=True)
user_post_schema = UserSchema()
