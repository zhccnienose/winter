from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.users import UserModel
from app.api.common.res import res


class GetUser(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        user = UserModel.find_by_username(username)
        if user is None:
            return res(404,"User not found")
        try:
            data = user.data()
            del data['uid']
            return res(code=200, msg="success", data=data)
        except Exception as e:
            return res(code=500, msg=str(e))
