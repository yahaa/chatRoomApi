# encoding=utf-8
from mongoengine import *
from datetime import datetime
from chatApi.tools.const.const import DESCRIPTION
from werkzeug import security
from flask import current_app


class User(Document):
    username = StringField(max_length=30)
    nickname = StringField(max_length=30)
    email = EmailField()
    phone_number = StringField(max_length=11)
    password = StringField(max_length=200)
    description = StringField(default=DESCRIPTION, max_length=400)
    meta = {'allow_inheritance': True}

    @staticmethod
    def check_password(user, raw):
        pwd = '{raw}{api}'.format(raw=raw, api=current_app.config['PASS_SECRET_KEY'])
        return security.check_password_hash(user.password, pwd)

    @staticmethod
    def create_password(raw):
        pwd = '{raw}{api}'.format(raw=raw, api=current_app.config['PASS_SECRET_KEY'])
        return security.generate_password_hash(pwd)


class CUser(User):
    friends = ListField(ReferenceField(User, reverse_delete_rule=DENY))


class Msg(Document):
    time = DateTimeField()
    author = ReferenceField(CUser, reverse_delete_rule=CASCADE)
    send_to = ReferenceField(CUser, reverse_delete_rule=CASCADE)
    time = DateTimeField(default=datetime.today)
    meta = {'allow_inheritance': True}


class TextMsg(Msg):
    content = StringField()
