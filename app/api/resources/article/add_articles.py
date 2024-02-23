from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.schema.add_atc_sha import reg_args_vaild
from app.api.models import r
from app.api.models.users import UserModel
from app.api.models.articles import ArticleModel
from app.api.common.res import res


class Articles(Resource):
    # 添加文章
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        reg_args_vaild(parser)
        data = parser.parse_args()

        username = get_jwt_identity()
        if username is None:
            return res(code=404, msg="该用户不存在")
        else:
            try:
                user = UserModel.find_by_username(username=username)
                data['uid'] = user.data().get('uid')
                # 获取当前文章id最大值并+1 作新文章的id
                max_id = ArticleModel.query.with_entities(ArticleModel.id).order_by(-ArticleModel.id).first()
                if max_id is None:
                    data['id'] = 1
                else:
                    max_id = max_id.id
                    data['id'] = max_id + 1

                article = ArticleModel(**data)
                article.add()

                # 文章序号 atc_uid_id
                r.hmset("atc_" + str(article.uid) + "_" + str(article.id),
                        {"likes": 0,
                         "collects": 0,
                         "comments": 0,
                         "hits": 0})

                # 维护最新列表
                new_lens = 2000
                lr = r.lpush("list_new", f"atc_{article.uid}_{article.id}")
                if lr > new_lens:
                    r.rpop("list_new")

                # 补充热门列表
                if r.llen("list_hot") < 200:
                    r.lpush("list_hot", f"atc_{article.uid}_{article.id}")
                    r.lpush("list_hot_hit", 0)

                return res(code=200, msg="添加成功")
            except Exception as e:
                return res(code=500, msg=str(e))
