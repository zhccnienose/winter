from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.articles import ArticleModel
from app.api.models.users import UserModel


# 获取自己写的文章
class GetMyArticles(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        try:
            user = UserModel().find_by_username(username=username)
            uid = user.data().get("uid")

            data_articles = ArticleModel.get_by_uid(uid=uid)

            return jsonify(code=200, msg="success", data=data_articles)
        except Exception as e:
            # print(e)
            return jsonify(code=500, msg=str(e))
