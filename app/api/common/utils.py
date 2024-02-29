import json
from ..models import r
from base64 import b64encode

# 公共response
def res(data=None, code=200, msg="success"):
    return json.dumps(
        {
            "code": code,
            "msg": msg,
            "data": data,
        })


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


def find_pos(list_hot, list_hot_hit, lside, rside, hits):
    if lside > rside:
        hot_value = list_hot[rside].decode("utf-8")
        value = list_hot_hit[rside]
        print("-----------", hot_value, value)
        return hot_value, value

    mid = (lside + rside) // 2

    if list_hot_hit[mid] >= hits:
        return find_pos(list_hot, list_hot_hit, lside, mid - 1, hits)
    else:
        return find_pos(list_hot, list_hot_hit, mid + 1, rside, hits)


def pil_base64(head_image_path):
    with open(head_image_path, "rb") as image:
        image_data = image.read()
    return b64encode(image_data).decode("utf-8")
