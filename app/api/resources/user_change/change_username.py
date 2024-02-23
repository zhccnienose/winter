from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.users import UserModel
from app.api.models import db
from app.api.common.res import res


class ChangeUsername(Resource):
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, location="args")
        data = parser.parse_args()

        username = get_jwt_identity()
        try:
            user = UserModel.query.filter_by(username=username).first()

            user.username = data['username']

            db.session.add(user)
            db.session.commit()

            return res(code=200, msg="success")
        except Exception as e:
            return res(code=500, msg=str(e))
