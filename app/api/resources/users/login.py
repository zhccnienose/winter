from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from werkzeug.security import check_password_hash

from app.api.schema.login_sha import reg_args_vaild
from app.api.models.users import UserModel


# 用户登录
class Login(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        reg_args_vaild(parser)
        data = parser.parse_args()

        username = data['username']
        user = UserModel.find_by_username(username=username)

        if user:
            try:
                password, salt = user.get_pwd().get("pwd"), user.get_pwd().get("salt")
                vaild = check_password_hash(password, "{}{}".format(salt, data['password']))

                if vaild:
                    response_data = generate_token(username)
                    return jsonify(code=200,
                                   msg="success",
                                   access_token=response_data.get('access_token'),
                                   refresh_token=response_data.get('refresh_token'))
                else:
                    return jsonify(code=400, msg="密码错误")

            except Exception as e:
                return jsonify(code=500, msg=str(e))
        else:
            return jsonify(code=404, msg="该用户不存在")

    @jwt_required(refresh=True)
    def get(self):
        current_username = get_jwt_identity()
        access_token = create_access_token(identity=current_username)
        return jsonify(data={"access_token": 'Bearer ' + access_token})


def generate_token(username):
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return {
        'access_token': 'Bearer ' + access_token,
        'refresh_token': 'Bearer ' + refresh_token,
    }
