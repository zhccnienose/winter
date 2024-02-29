import os
from datetime import datetime
from werkzeug.datastructures import FileStorage

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.config import UPLOAD_FOLDER
from app.api.models import db
from app.api.models.users import UserModel
from app.api.common.res import res


class ChangeHeadimage(Resource):
    @jwt_required()
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('head_image', type=FileStorage, required=True, location='files')
        data = parser.parse_args()

        username = get_jwt_identity()
        try:
            user = UserModel.find_by_username(username=username)
            os.remove(os.path.join(UPLOAD_FOLDER, user.headimage))

            image_name = datetime.now().strftime('%Y%m%d%H%M%S.%f') + ".jpg"
            data['head_image'].save(os.path.join(UPLOAD_FOLDER, image_name))  # 保存
            user.headimage = image_name

            db.session.add(user)
            db.session.commit()

            return res(code=200, msg="success")
        except Exception as e:
            return res(code=500, msg=str(e))
