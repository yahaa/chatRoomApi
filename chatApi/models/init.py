# encoding=utf-8
from mongoengine import connect
from chatApi.models.entity import CUser

connect('chatapi')


def create_user():
    admin = CUser(username='zihua4', password='123456').save()


if __name__ == '__main__':
    create_user()
