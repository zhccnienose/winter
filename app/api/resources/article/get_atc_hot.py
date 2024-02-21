from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.api.models import r
from app.api.models.articles import ArticleModel


class GetAtcHot(Resource):
    @jwt_required()
    def get(self):
        list_hot = r.lrange("list_hot", 0, -1)
        data_article = []

        if list_hot is not None:
            print(list_hot)
            for i in range(len(list_hot) - 1, -1, -1):
                atc_id = list_hot[i]
                article = ArticleModel.get_by_id(int(atc_id.decode("utf-8").split("_")[-1]))
                data = article.data()

                data_article.append(data)
        else:
            pass
        return jsonify(code=200, msg="success", data=data_article)
