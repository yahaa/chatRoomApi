# encoding=utf-8
from chatApi.models.entity import User
from flask import abort


def login(username, password):
    user = User.objects(username=username).first()
    if user is None:
        return {'message': 'this user does not exist !'}
    if User.check_password(user, password):
        return {
            'code': '1',
            'msg': 'success',
            'token': 'asdfghjkl'
        }
    return {
        'message': 'password does not true !'
    }


def create_user(username, password, email, nickname):
    if not username:
        return abort(403)

    if is_exits(username):
        return {
            'message': 'user exited !'
        }

    user = User(
        username=username,
        password=User.create_password(password),
        email=email,
        nickname=nickname
    ).save()

    return {
        'message': 'regist success !'
    }


def is_exits(username):
    user = User.objects(username=username).first()
    if user:
        return True
    return False
