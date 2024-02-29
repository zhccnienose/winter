from datetime import timedelta

# 头像保存路径
UPLOAD_FOLDER = 'D:\\pyprojects\\winter\\static\\headimages\\'
# UPLOAD_FOLDER = '/root/warmup/static/headimages/'

# 服务器地址
SERVER_URL = "http://47.115.212.55:5000/"

# 头像文件获取路径
IMAGE_PATH = "user/images/files/"


class Config(object):
    DEBUG = True
    SECRET_KEY = "secret_key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:310257813@47.115.212.55:3306/winter?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:C310257813.@localhost:3306/winter?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    JWT_SECRET_KEY = "jwt_secret_key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_RESFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLOCKLIST_TOKEN_CHECKS = ['access']
