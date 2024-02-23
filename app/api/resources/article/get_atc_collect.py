from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.api.models import r
from app.api.models.users import UserModel
from app.api.models.articles import ArticleModel
from app.api.common.res import res


class GetAtcCollect(Resource):
    @jwt_required()
    def get(self):
        username = get_jwt_identity()
        user = UserModel.find_by_username(username)
        uid = user.data().get('uid')

        try:
            # 获取该用户点赞的文章
            atcs = list(r.smembers(str(uid) + "_collect"))
            if atcs is None:
                return res(code=200, msg="success", data=[])

            list_collects = []

            for id in atcs:
                id = int(id.decode('utf-8').split('_')[-1])  # 按下划线分割后取出id
                atc = ArticleModel.get_by_id(id)  # 文章对象

                if atc is not None:
                    data = atc.data(user)
                    list_collects.append(data)

            return res(code=200, msg="success", data=list_collects)
        except Exception as e:
            return res(code=500, msg=str(e))
