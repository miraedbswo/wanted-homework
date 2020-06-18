from werkzeug.exceptions import HTTPException


class NoContentException(HTTPException):
    code = 204
    description = 'No Content'


class ForbiddenException(HTTPException):
    code = 403
    description = 'Forbidden'


class BadRequestException(HTTPException):
    code = 400
    description = 'Bad Parameter Request'
