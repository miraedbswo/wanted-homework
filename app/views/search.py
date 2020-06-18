from http import HTTPStatus
from typing import Optional

from app.context import context_property
from app.models import Tag, CompanyTagMapping
from app.models.company_name import CompanyName
from flask_restful import Resource

from app.decorators.validation import (
    PayloadLocation,
    data_type_validate,
    SEARCH_GET,
)


class Search(Resource):
    @staticmethod
    def get_korean_name_of_company_by_tag(tag: str):
        return CompanyName.query \
            .join(CompanyTagMapping, CompanyTagMapping.company_id == CompanyName.company_id) \
            .join(Tag, Tag.tag_group_id == CompanyTagMapping.tag_group_id) \
            .filter(Tag.name == tag) \
            .filter(CompanyName.language == 'ko') \
            .all()

    @data_type_validate(SEARCH_GET, PayloadLocation.ARGS)
    def get(self):
        payload = context_property.request_payload
        company_name: Optional[str] = payload.get('name')
        tag: Optional[str] = payload.get('tag')

        if company_name:
            if (companies := CompanyName.get_companies_by_similar_name(company_name)) is None:
                return '', HTTPStatus.NO_CONTENT

        else:
            if (companies := Search.get_korean_name_of_company_by_tag(tag)) is None:
                return '', HTTPStatus.NO_CONTENT

        return {'companies': [company.name for company in companies]}, HTTPStatus.OK

