# encoding=utf-8
from werkzeug.security import safe_str_cmp
from chatApi.models.entity import User
from bson import ObjectId


def serial(dct):
    for k in dct:
        if isinstance(dct[k], ObjectId):
            dct[k] = str(dct[k])
    return dct


def authenticate(username, password):
    user = User.objects(username=username).first()
    user = serial(user)

    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    t = User.objects(id=user_id).first()
    return t
