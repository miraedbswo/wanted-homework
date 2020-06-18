from __future__ import annotations
from typing import List, Optional

from app.extension import db
from app.models.base import BaseModel, BaseMixin


class CompanyName(BaseModel, BaseMixin):
    __tablename__ = 'company_name'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    name = db.Column(db.String(63))
    language = db.Column(db.String(32))

    def __init__(self, company_id: int, name: str, language: str):
        self.company_id = company_id
        self.name = name
        self.language = language

    @staticmethod
    def get_companies_by_similar_name(name: str) -> Optional[List[CompanyName], None]:
        if not name:
            return None

        search = f'%{name}%'
        companies = CompanyName.query.filter(CompanyName.name.like(search)).all()
        return companies
