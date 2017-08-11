# encoding: utf-8
from flask.ext.restful import fields

login_success = {
    'code': fields.String,
    'msg': fields.String,
}

regist_success = {
    'message': fields.String,
}
