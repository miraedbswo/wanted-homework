from app.extension import db
from app.models.base import BaseModel, BaseMixin


class CompanyTagMapping(BaseModel, BaseMixin):
    __tablename__ = 'company_tag_mapping'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    tag_group_id = db.Column(db.Integer, db.ForeignKey('tag_group.id', ondelete='CASCADE'))

    def __init__(self, company_id: int, tag_group_id: int):
        self.company_id = company_id
        self.tag_group_id = tag_group_id

    @staticmethod
    def get_company_tag_mapping(company_id: int, tag_group_id: int):
        return CompanyTagMapping.query.filter_by(
            company_id=company_id,
            tag_group_id=tag_group_id
        ).first()
