from flask import request
from flask.views import View

from app import db
from app.models import User
from app.schemas.users import user_list_schema, user_post_schema


class UsersList(View):
    methods = ["GET"]

    def dispatch_request(self):
        users = User.query.all()
        result = user_list_schema.dumps(users)
        return result.data


class CreateUser(View):
    methods = ["POST"]

    def dispatch_request(self):
        user_data = request.json.copy()
        result = user_post_schema.load(user_data)
        user = result.data

        db.session.add(user)
        db.session.commit()

        return user_post_schema.dumps(user)
