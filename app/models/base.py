from app.extension import db
from app.utils.time import kst_now
from app.exception import BadRequestException


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=kst_now())
    updated_at = db.Column(db.DateTime, default=kst_now(), onupdate=kst_now())


class BaseMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def assert_validation(validate_result: bool):
        if not validate_result:
            raise BadRequestException()
