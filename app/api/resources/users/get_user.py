from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.users import UserModel


class GetUser(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        user = UserModel.find_by_username(username)
        try:
            data = user.data()
            del data['uid']
            return jsonify(code=200, msg="success", data=data)
        except Exception as e:
            return jsonify(code=500, msg=str(e))
