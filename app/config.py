from datetime import timedelta

UPLOAD_FOLDER = '/root/warmup/static/headimages/'

SERVER_URL = "http://47.115.212.55:5000/"

IMAGE_PATH = '/root/warmup/static/headimages/'


class Config(object):
    DEBUG = True

    SECRET_KEY = "secret_key"

    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    JWT_SECRET_KEY = "jwt_secret_key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_RESFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLOCKLIST_TOKEN_CHECKS = ['access']
