from app.extension import db
from app.models.base import BaseModel, BaseMixin


class Tag(BaseModel, BaseMixin):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    tag_group_id = db.Column(db.Integer, db.ForeignKey('tag_group.id', ondelete='CASCADE'))
    name = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)

    def __init__(self, tag_group, name, language):
        self.tag_group = tag_group
        self.name = name
        self.language = language
