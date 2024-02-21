from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from app.api.models.revoked_tokens import TokenModel


class Exit(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']

        try:
            revoked_token = TokenModel(jti=jti)
            revoked_token.add()

            return jsonify(code=200, msg="退出成功")

        except Exception as e:
            return jsonify(code=500, msg=str(e))
