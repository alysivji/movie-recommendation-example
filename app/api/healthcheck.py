from flask import jsonify
from flask.views import View


class HealthCheck(View):
    def dispatch_request(self):
        msg = {"message": "ping"}
        return jsonify(msg)
