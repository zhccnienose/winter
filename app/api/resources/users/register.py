import uuid
import os
from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from app.config import UPLOAD_FOLDER
from app.api.models.users import UserModel
from app.api.schema.register_sha import reg_args_vaild


class Register(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        reg_args_vaild(parser)
        data = parser.parse_args()

        image_name = datetime.now().strftime('%Y%m%d%H%M%S.%f') + ".jpg"
        data['headimage'].save(os.path.join(UPLOAD_FOLDER, image_name))
        data['headimage'] = image_name
        user = UserModel.find_by_username(data.get("username"))

        if user is not None:
            return jsonify(code=400, msg="该用户已存在")
        else:
            try:
                data['salt'] = uuid.uuid4().hex
                data['password'] = generate_password_hash(f"{data['salt']}{data['password']}")
                user = UserModel(**data)
                user.add_user()

                return jsonify(code=200, msg="注册成功")
            except Exception as e:
                return jsonify(code=500, msg=str(e))
