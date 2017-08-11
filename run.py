# encoding=utf-8
from flask import Flask, g
from chatApi.app import api_bp
from chatApi.models import register_database
from flask_jwt import JWT
from chatApi.handler.auth import authenticate, identity


def create_app(**config):
    app = Flask(__name__)
    register_config(app, config)
    jwt = JWT(app, authenticate, identity)
    register_database(app)
    register_routes(app)
    return app


def register_config(app, config):
    if config.get('debug') is True:
        app.debug = True

    from config import default
    app.config.from_object(default)


def register_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == '__main__':
    create_app(debug=True).run()
