"""Application Level Exceptions

Implemented pattern described in Flask documentation
    http://flask.pocoo.org/docs/1.0/patterns/apierrors/
"""


class DeserializationError(Exception):
    status_code = 422

    def __init__(self, payload):
        super().__init__()
        self.message = "Marshmallow Deserialization Error"
        self.payload = payload

    def to_dict(self):
        return self.payload.copy()


class SerializationError(Exception):
    status_code = 500

    def __init__(self, payload):
        super().__init__()
        self.message = "Marshmallow Serialization Error"
        self.payload = payload

    def to_dict(self):
        return self.payload.copy()
