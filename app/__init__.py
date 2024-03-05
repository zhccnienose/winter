from flask import Flask, send_file
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from .config import Config

from .api.models import db, r
from .api import user_bp, article_bp, user_change_bp
from .manage import migrate
from .api.models.users import UserModel
from .api.models.revoked_tokens import TokenModel


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    app.register_blueprint(user_change_bp)

    jwt = JWTManager(app)
    register_jwt_hooks(jwt)

    @app.route('/')
    def hello():
        return 'hello world'

    @app.route('/testmysql')
    def test_mysql():
        user = UserModel.query.first()
        return user.username

    @app.route('/testredis')
    def test_redis():
        value = r.get('a')
        return {"value": value.decode('utf-8')}

    @app.route('/testheadimages')
    def test_headimages():
        path = "/static/headimages/20240221224814.383692.jpg"
        return send_file(path, mimetype='image/jpg')

    return app


def register_jwt_hooks(jwt):
    # 检验是否在黑名单中
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, decrypted_token):
        jti = decrypted_token['jti']
        return TokenModel.check(jti)

    # 过期返回信息
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, decrypted_token):
        return {
            'code': 403,
            'message': 'expired token'
        }

    # 验证失败返回信息
    @jwt.invalid_token_loader
    def invalid_token_callback(jwt_header, decrypted_token):
        return {
            'code': 400,
            'message': 'Invalid token'
        }

    # 缺少token返回信息
    @jwt.unauthorized_loader
    def missing_token_callback(decrypted_token):
        return {
            "code": 401,
            "msg": "Missing token"
        }


app = create_app()
