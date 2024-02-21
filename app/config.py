import os
from datetime import timedelta

UPLOAD_FOLDER = 'D:\\pyprojects\\winter\\static\\headimages\\'
# UPLOAD_FOLDER = '/root/warmup/static/headimages/'


class Config(object):
    DEBUG = True

    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:310257813@47.115.212.55:3306/winter?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    JWT_SECRET_KEY = "jwt_secret_key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_RESFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLOCKLIST_TOKEN_CHECKS = ['access']
