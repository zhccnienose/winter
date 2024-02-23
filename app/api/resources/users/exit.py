from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt

from app.api.models.revoked_tokens import TokenModel
from app.api.common.res import res


class Exit(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']

        try:
            revoked_token = TokenModel(jti=jti)
            revoked_token.add()

            return res(code=200, msg="退出成功")

        except Exception as e:
            return res(code=500, msg=str(e))
