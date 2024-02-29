from flask_restful import Resource, reqparse

from ...models.articles import ArticleModel
from app.api.common.res import res


class DelArticle(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id error')
        data = parser.parse_args()

        id = data['id']
        article = ArticleModel.get_by_id(id)

        if article is None:
            return res(code=404, msg="该用户不存在")

        try:
            article.delete_by_id(id)
            return res(code=200, msg="删除成功")
        except Exception as e:
            return res(code=500, msg=str(e))
