from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.api.models import r
from app.api.models.articles import ArticleModel

from ...common.find_pos import find_pos
from app.api.common.res import res


class AtcHit(Resource):
    @jwt_required()
    def put(self, id):
        try:
            # 获取文章信息
            article = ArticleModel.get_by_id(id=id)
            # data = article.data()
            uid = article.uid

            username = get_jwt_identity()
            # 文章点击量+1(间隔三十秒及以上有效）
            if r.get(f"atc_{uid}_{id}_{username}_hits") is None:
                r.set(f"atc_{uid}_{id}_{username}_hits", 1, ex=30)
                r.hincrby(f"atc_{uid}_{id}", "hits", 1)

                hits = r.hget(f"atc_{uid}_{id}", "hits")

                if hits is None:
                    hits = 0
                else:
                    hits = int(hits.decode("utf-8"))

                # print("-------", hits, "----------")
                list_hot = r.lrange("list_hot", 0, -1)
                list_hot_hit = r.lrange("list_hot_hit", 0, -1)

                for atc_id in list_hot:
                    atc_id = atc_id.decode("utf-8")
                for i in range(len(list_hot_hit)):
                    list_hot_hit[i] = int(list_hot_hit[i].decode("utf-8"))

                # 小于最小值
                if list_hot_hit[0] >= hits:
                    pass
                elif list_hot_hit[-1] < hits:
                    # 移除数量=1，该值存在
                    if r.lrem("list_hot", 1, f"atc_{uid}_{id}") == 1:
                        r.lrem("list_hot_hit", 1, hits - 1)
                    # 该值不存在，则移除最小值
                    else:
                        r.lpop("list_hot")
                        r.lpop("list_hot_hit")

                    r.rpush("list_hot", f"atc_{uid}_{id}")
                    r.rpush("list_hot_hit", hits)
                else:
                    # hot_value:第一篇点击数小于该文章的文章编号，value:第一篇小于该文章的点击数
                    hot_value, value = find_pos(list_hot, list_hot_hit, 0, len(list_hot_hit) - 1, hits)

                    if r.lrem("list_hot", 1, f"atc_{uid}_{id}") == 1:
                        r.lrem("list_hot_hit", 1, hits - 1)
                    else:
                        r.lpop("list_hot")
                        r.lpop("list_hot_hit")

                    r.linsert("list_hot", "after", hot_value, f"atc_{uid}_{id}")
                    r.linsert("list_hot_hit", "after", value, hits)

            else:
                pass

            return res(code=200, msg="success")

        except Exception as e:
            return res(code=500, msg=str(e))
