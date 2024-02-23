from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.models import db
from app.api.models.users import UserModel
from app.api.common.res import res


class ChangePassword(Resource):

    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('old_password', type=str, required=True, location='args')
        parser.add_argument('new_password', type=str, required=True, location='args')
        data = parser.parse_args()

        username = get_jwt_identity()
        try:
            user = UserModel.find_by_username(username=username)
            if user is None:
                return res(code=400, msg="该用户不存在")
            else:
                password, salt = user.get_pwd().get('pwd'), user.get_pwd().get('salt')
                if check_password_hash(password, "{}{}".format(salt, data['old_password'])):
                    user.password = generate_password_hash("{}{}".format(salt, data['new_password']))

                    db.session.add(user)
                    db.session.commit()
                    return res(code=200, msg="success")
                else:
                    return res(code=400, msg="与原密码不同")
        except Exception as e:
            return res(code=500, msg=str(e))
