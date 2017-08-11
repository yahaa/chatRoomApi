# encoding=utf-8
import datetime

MONGODB_SETTINGS = {'DB': 'chatapi'}
SECRET_KEY = 'yuanzihua@@@auhiznauy'
JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=3000)
JWT_AUTH_URL_RULE = '/api/login'
PASS_SECRET_KEY = 'chatapi'
