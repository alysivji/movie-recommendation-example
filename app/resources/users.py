from flask import request
from flask.views import View

from app import db
from app.models import User
from app.schemas.users import user_list_schema, user_post_schema
from app.utilities import deserialize_request, send_response, serialize_response


class UsersList(View):
    methods = ["GET"]

    def dispatch_request(self):
        users = db.query(User).all()
        return serialize_response(user_list_schema, users)


class UsersPost(View):
    methods = ["POST"]

    def dispatch_request(self):
        user_data = request.json.copy()
        user = deserialize_request(user_post_schema, user_data)

        db.session.add(user)
        db.session.commit()

        serialized_result = serialize_response(user_post_schema, user)
        return send_response(200, data=serialized_result)
