from flask import send_from_directory
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.config import UPLOAD_FOLDER


class HeadImageFile(Resource):
    @jwt_required()
    def get(self, image_name):
        return send_from_directory(UPLOAD_FOLDER, image_name)
