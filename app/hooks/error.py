from http import HTTPStatus

from flask import current_app, jsonify
from werkzeug.exceptions import HTTPException


def http_exception_handler(e: Exception):
    if isinstance(e, HTTPException):
        message = e.description
        code = e.code

    else:
        message = str(e)
        code = HTTPStatus.INTERNAL_SERVER_ERROR

        if current_app.debug:
            import traceback

            traceback.print_exc()

    return jsonify({"error": message}), code
