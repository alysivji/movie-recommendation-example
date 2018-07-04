import json
from typing import Union

from flask import Response


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
