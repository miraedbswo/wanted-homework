from flask import Blueprint
from flask_restful import Api

from app.views.search import Search
from app.views.tagging import Tagging

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# - route
api.add_resource(Tagging, "/tag")
api.add_resource(Search, '/search')
