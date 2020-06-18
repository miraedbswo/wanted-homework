from flask import Flask


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)


def register_hooks(flask_app: Flask):
    from app import exception
    from app.hooks.error import http_exception_handler

    flask_app.register_error_handler(Exception, http_exception_handler)


def register_views(flask_app: Flask):
    from app.views import api_blueprint
    flask_app.register_blueprint(api_blueprint)


def create_app(*config_cls) -> Flask:
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    register_extension(flask_app)
    register_hooks(flask_app)
    register_views(flask_app)

    return flask_app

