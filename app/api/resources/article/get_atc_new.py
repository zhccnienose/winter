from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.api.models import r
from app.api.models.articles import ArticleModel


class GetAtcNew(Resource):
    @jwt_required()
    def get(self):
        list_new = r.lrange("list_new", 0, -1)
        print(list_new)
        data_article = []
        if list_new is not None:
            for i in range(len(list_new)):
                atc_id = list_new[i]
                # print("-----------------")
                # print(int(atc_id.decode("utf-8").split("_")[-1]))
                # print("-----------")
                article = ArticleModel.get_by_id(int(atc_id.decode("utf-8").split("_")[-1]))
                data = article.data()

                data_article.append(data)
        else:
            pass
        return jsonify(code=200, msg="success", data=data_article)
