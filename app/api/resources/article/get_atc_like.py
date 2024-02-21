from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.api.models import r
from app.api.models.users import UserModel
from app.api.models.articles import ArticleModel


class GetAtcLike(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        user = UserModel.find_by_username(username)
        uid = user.data().get('uid')

        try:
            # 获取该用户点赞的文章
            atcs = r.smembers(str(uid) + "_like")

            if atcs is None:
                return jsonify(code=200, msg="success", data=[])

            list_likes = []
            for id in atcs:

                id = int(id.decode().split('_')[-1])  # 按下划线分割后取出id
                atc = ArticleModel.get_by_id(id)  # 文章对象
                # author = UserModel.find_by_uid(atc.uid)  # 文章作者对象

                data = atc.data()

                list_likes.append(data)

                return jsonify(code=200, msg="success", data=list_likes)
        except Exception as e:
            return jsonify(code=500, msg=str(e))
