from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models import db
from app.api.models.users import UserModel


class ChangeHeadimage(Resource):
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('head_image', type=str, required=True, location='args')
        data = parser.parse_args()

        username = get_jwt_identity()
        try:
            user = UserModel.query.filter_by(username=username).first()
            # print(data)
            user.headimage = data["head_image"]

            db.session.add(user)
            db.session.commit()

            return jsonify(code=200, msg="success")
        except Exception as e:
            return jsonify(code=500, msg=str(e)), 500
