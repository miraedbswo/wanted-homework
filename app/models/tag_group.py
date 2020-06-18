from app.extension import db
from app.models.base import BaseModel, BaseMixin


class TagGroup(BaseModel, BaseMixin):
    __tablename__ = 'tag_group'
    id = db.Column(db.Integer, primary_key=True)
