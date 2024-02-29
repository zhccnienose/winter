import os
from flask import send_from_directory
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import NotFound

from app.config import UPLOAD_FOLDER


class UsersHeadImage(Resource):
    @jwt_required()
    def get(self, image_name):
        if os.path.exists(os.path.join(UPLOAD_FOLDER + image_name)):
            return send_from_directory(UPLOAD_FOLDER, image_name)
        else:
            raise NotFound("Image not found")
