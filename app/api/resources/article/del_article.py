from flask_restful import Resource, reqparse

from ...models.articles import ArticleModel
from app.api.common.res import res


class DelArticle(Resource):
    def delete(self, id):
        article = ArticleModel.get_by_id(id)

        if article is None:
            return res(code=404, msg="该文章不存在")

        try:
            article.delete()
            return res(code=200, msg="删除成功")
        except Exception as e:
            return res(code=500, msg=str(e))
