from app.api.models import r


# 获取文章点击量，点赞量，收藏量
def get_hclc(uid, id):
    hits = r.hget("atc_" + str(uid) + "_" + str(id), "hits")  # 点击量
    likes = r.hget("atc_" + str(uid) + "_" + str(id), "likes")  # 点赞量
    collects = r.hget("atc_" + str(uid) + "_" + str(id), "collects")  # 收藏量
    comments = r.hget("atc_" + str(uid) + "-" + str(id), "comments")  # 评论量
    if hits is None:
        hits = 0
    else:
        hits = int(hits.decode("utf-8"))

    if likes is None:
        likes = 0
    else:
        likes = int(likes.decode("utf-8"))
    if collects is None:
        collects = 0
    else:
        collects = int(collects.decode("utf-8"))
    if comments is None:
        comments = 0
    else:
        comments = int(comments.decode("utf-8"))

    return hits, likes, collects, comments
