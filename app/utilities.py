"""Collection of utility functions"""

import hashlib
import json
from typing import Union

from flask import current_app as app, Response
from marshmallow import ValidationError

from .exceptions import SerializationError, DeserializationError


def generate_password_hash(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def deserialize_request(schema, data):
    """Wrapper for Marhsmallow's schema.loads"""
    try:
        deserialized_result = schema.load(data)
        return deserialized_result
    except ValidationError as exc:
        app.logger.exception("Deserialization error", exc.messages)
        raise DeserializationError(payload=exc.messages)


def serialize_response(schema, data):
    """Wrapper for Marhsmallow's schema.dumps"""
    try:
        serialized_result = schema.dumps(data)
        return serialized_result
    except ValidationError as exc:
        app.logger.exception("Serialization error", exc.messages)
        raise SerializationError(payload=exc.messages)


def send_response(
    status_code: int = 200,
    *,
    headers: dict = {},
    data: Union[dict, str] = {},
    error: dict = {},
):
    """Send response, error param trumps data param"""
    if data:
        output = data if isinstance(data, str) else json.dumps(data)

    if error:
        error_dict = {}
        error_dict["error"] = error
        output = json.dumps(error_dict)

    return Response(
        response=output,
        status=status_code,
        headers=headers,
        content_type="application/json",
    )
