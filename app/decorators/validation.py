from enum import Enum
from functools import wraps

from flask import request

from app.context import context_property
from app.exception import BadRequestException


class PayloadLocation(Enum):
    ARGS = "args"
    JSON = "json"


def data_type_validate(data_schema: dict, payload_location: PayloadLocation):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            data = {}
            if payload_location is payload_location.JSON:
                data: dict = request.json
            elif payload_location is payload_location.ARGS:
                data: dict = request.args

            if not data:
                raise BadRequestException()

            for key, type_ in data_schema.items():
                value = data.get(key)
                if not value and payload_location is payload_location.ARGS:
                    continue

                if type(value) is not type_:
                    break
            else:
                context_property.request_payload = data
                return fn(*args, **kwargs)
            raise BadRequestException()

        return wrapper

    return decorator


TAGGING_POST = dict(company_id=int, tag_id=int)
TAGGING_DELETE = dict(company_id=int, tag_id=int)
SEARCH_GET = dict(name=str, tag=str)
