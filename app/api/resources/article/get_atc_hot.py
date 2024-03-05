from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.models.users import UserModel
from app.api.models import r
from app.api.models.articles import ArticleModel
from app.api.common.res import res


class GetAtcHot(Resource):
    @jwt_required()
    def get(self):
        try:
            user = UserModel.find_by_username(get_jwt_identity())

            # 按点击量降序
            list_hot = r.zrevrange("list_hot", 0, -1)
            # print(list_hot)
            data_article = []

            if list_hot is not None:
                # print(list_hot)
                # 按点击量降序
                for i in range(len(list_hot)):
                    article = ArticleModel.get_by_id(int(list_hot[i].decode("utf-8").split("_")[-1]))
                    data = article.data(user)

                    data_article.append(data)
            else:
                pass
            return res(code=200, msg="success", data=data_article)
        except Exception as e:

            return res(code=500, msg=str(e))
