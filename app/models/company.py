from app.extension import db
from app.models.base import BaseModel, BaseMixin


class Company(BaseModel, BaseMixin):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    # TODO: 회사 정보 Column 추가 가능
