from ..models import db, r
from .users import UserModel
from ..common.get_hclc import get_hclc
from app.config import SERVER_URL, IMAGE_PATH


# 文章类
class ArticleModel(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # 文章id
    title = db.Column(db.String(50), nullable=False)  # 文章标题
    content = db.Column(db.Text, nullable=False)  # 文章内容
    create_time = db.Column(db.String(50), nullable=False)  # 文章创建时间
    uid = db.Column(db.Integer, nullable=False)  # 用户ID

    # 创建文章
    def add(self):
        db.session.add(self)
        db.session.commit()

    # 获取文章信息
    def data(self, user):
        info = {"id": self.id,
                "title": self.title,
                "content": self.content,
                "time": self.create_time,
                "uid": self.uid}

        author = UserModel.find_by_uid(uid=self.uid)
        info["author"] = {"username": author.username, "head_image": SERVER_URL + IMAGE_PATH + author.headimage}

        hits, likes, collects, comments = get_hclc(self.uid, self.id)

        # 是否点赞
        if r.sismember(str(user.uid) + "_like", f"atc_{str(self.uid)}_{str(self.id)}"):
            like_status = 1
        else:
            like_status = 0
        # 是否收藏
        if r.sismember(str(user.uid) + "_collect", f"atc_{str(self.uid)}_{str(self.id)}"):
            collect_status = 1
        else:
            collect_status = 0

        info.update(like_status=like_status, collect_status=collect_status,
                    hits=hits, collects=collects, likes=likes, comments=comments)

        del info["uid"]
        return info

    # 获取该用户的文章
    @classmethod
    def get_by_user(cls, user):
        data_tuple = cls.query.filter_by(uid=user.uid).all()
        list_mine = []

        for item in data_tuple:
            data = item.data(user)
            list_mine.append(data)

        return list_mine

    # 根据id返回文章对象
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def delete_by_id(self, id):
        uid = self.uid

        r.delete(f"atc_{uid}_{id}")  # 删除数据记录
        r.lrem("list_new", 1, f"atc_{uid}_{id}")  # 从最新列表中移除
        r.lrem("list_hot", 1, f"atc_{uid}_{id}")  # 从热门列表中移除

        db.session.delete(self)
        db.session.commit()
