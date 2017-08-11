# encoding=utf-8
from flask import Blueprint
from flask.ext.restful import Api
from chatApi.resources.register import Register

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Register, '/register')
