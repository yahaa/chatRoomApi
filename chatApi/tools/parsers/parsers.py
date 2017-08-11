# encoding=utf-8
from flask.ext.restful import reqparse

# ------------ login parser ------------
login_parser = reqparse.RequestParser()
login_parser.add_argument(
    'username', dest='username',
    type=str, location='form',
    required=True, help='This is username',
)

login_parser.add_argument(
    'password', dest='password',
    type=str, location='form',
    required=True, help='This is password',
)

# ------------ register parser ------------
register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'username', dest='username',
    type=str, location='json',
    required=True, help='This is username',
)

register_parser.add_argument(
    'password', dest='password',
    type=str, location='json',
    required=True, help='This is password',
)

register_parser.add_argument(
    'email', dest='email',
    type=str, location='json',
    required=True, help='This is email',
)

register_parser.add_argument(
    'nickname', dest='nickname',
    type=str, location='json',
    required=True, help='This is nickname',
)
