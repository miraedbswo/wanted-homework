from http import HTTPStatus

from app.context import context_property
from app.models.company_tag_mapping import CompanyTagMapping
from flask_restful import Resource

from app.decorators.validation import PayloadLocation, data_type_validate, TAGGING_POST, TAGGING_DELETE


class Tagging(Resource):
    @data_type_validate(TAGGING_POST, PayloadLocation.JSON)
    def post(self):
        payload = context_property.request_payload
        company_id: int = payload.get('company_id')
        tag_group_id: int = payload.get('tag_id')

        if CompanyTagMapping.get_company_tag_mapping(company_id, tag_group_id):
            return {'msg': 'tag is already exist.'}, HTTPStatus.CONFLICT

        CompanyTagMapping(company_id, tag_group_id).save()
        return {'msg': 'Tag creation succeeded.'}, HTTPStatus.CREATED

    @data_type_validate(TAGGING_DELETE, PayloadLocation.JSON)
    def delete(self):
        payload = context_property.request_payload
        company_id: int = payload.get('company_id')
        tag_group_id: int = payload.get('tag_id')

        if (company := CompanyTagMapping.get_company_tag_mapping(company_id, tag_group_id)) is None:
            return {'msg': 'tag is not exist.'}, HTTPStatus.CONFLICT

        company.delete()
        return {'msg': 'Tag deletion succeeded.'}, HTTPStatus.OK
