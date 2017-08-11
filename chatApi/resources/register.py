# encoding=utf-8
from flask.ext.restful import Resource, request, marshal_with
from chatApi.tools.parsers.parsers import *
from chatApi.tools.fields.result import *
from chatApi.handler.user_opt import login, create_user
from flask_jwt import jwt_required, current_identity


class Login(Resource):
    decorators = [jwt_required()]

    @marshal_with(login_success)
    def post(self):
        print current_identity.username
        login_args = login_parser.parse_args()
        return login(login_args.username, login_args.password)


class Register(Resource):
    @marshal_with(regist_success)
    def post(self):
        regist_args = register_parser.parse_args()
        return create_user(regist_args.username,
                           regist_args.password,
                           regist_args.email,
                           regist_args.nickname)
