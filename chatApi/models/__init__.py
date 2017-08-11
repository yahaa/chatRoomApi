# encoding=utf-8
from entity import *
from mongoengine import connect


def register_database(app):
    database = app.config['MONGODB_SETTINGS']['DB']
    connect(database)
