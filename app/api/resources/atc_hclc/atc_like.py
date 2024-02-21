from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from ...models import r
from ...models.users import UserModel
from ...models.articles import ArticleModel


class AtcLike(Resource):
    @jwt_required()
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("status", type=int, required=True, location="form")
        data = parser.parse_args()

        try:
            # 获取用户id
            user = UserModel.find_by_username(get_jwt_identity())
            uid = user.uid
            # 获取作者id
            article = ArticleModel.query.filter_by(id=id).first()
            author_id = article.uid

            if data["status"] == 1:
                r.sadd(str(uid) + "_like", f"atc_{author_id}_{id}")  # 添加到用户的点赞文章集合
                r.hincrby(f"atc_{uid}_{id}", "likes", 1)  # 文章点赞量+1
            elif data["status"] == 0:
                r.srem(str(uid) + "_like", f"atc_{author_id}_{id}")  # 取消点赞
                r.hincrby(f"atc_{uid}_{id}", "likes", -1)  # 文章点赞量-1
            else:
                return jsonify(code=400, msg="参数错误")

            return jsonify(code=200, msg="点赞成功")
        except Exception as e:
            return jsonify(code=500, msg=str(e))
