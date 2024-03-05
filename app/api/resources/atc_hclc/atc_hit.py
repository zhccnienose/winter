import os
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.api.models import r
from app.api.models.articles import ArticleModel

from app.api.common.res import res
from app.api.common.write_500_error import write_500_error


class AtcHit(Resource):
    @jwt_required()
    def put(self, id):
        try:
            # 获取文章信息
            article = ArticleModel.get_by_id(id=id)
            uid = article.uid

            username = get_jwt_identity()
            # 文章点击量+1(间隔三十秒及以上有效）
            if r.get(f"atc_{uid}_{id}_{username}_hits") is None:
                r.set(f"atc_{uid}_{id}_{username}_hits", 1, ex=30)

                hits = r.hget(f"atc_{uid}_{id}", "hits")
                # print(hits)
                r.hincrby(f"atc_{uid}_{id}", "hits", 1)
                hits = r.hget(f"atc_{uid}_{id}", "hits")
                # print(hits)
                if hits is None:
                    hits = 0
                else:
                    hits = int(hits.decode("utf-8"))

                # 分数最小的元素和其分数值
                min_member = r.zrange("list_hot", 0, 0, withscores=True)  # ((member1,score1))
                min_atc_id = min_member[0][0].decode("utf-8")
                min_score = min_member[0][1]
                # print(min_atc_id, min_score)

                if hits <= min_score:
                    pass
                else:
                    # 不存在与热门列表中，加入并删除最小元素
                    if r.zscore("list_hot", f"atc_{uid}_{id}") is None:
                        r.popmin("list_hot")
                        r.zadd("list_hot", {f"atc_{uid}_{id}": hits})
                        # print(hits)
                    # 存在则分数+1
                    else:
                        r.zincrby("list_hot", 1, f"atc_{uid}_{id}")
                        # print(r.zscore("list_hot", f"atc_{uid}_{id}"))
            else:
                pass

            return res(code=200, msg="success")

        except Exception as e:
            write_500_error(os.getcwd(), str(e))
            return res(code=500, msg=str(e))
