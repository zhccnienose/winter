from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.articles import ArticleModel
from app.api.models.users import UserModel
from app.api.common.res import res


# 获取自己写的文章
class GetMyArticles(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        try:
            user = UserModel().find_by_username(username=username)

            data_articles = ArticleModel.get_by_user(user)

            return res(code=200, msg="success", data=data_articles)
        except Exception as e:
            return res(code=500, msg=str(e))
