from ..models import db
from .users import UserModel
from app.config import SERVER_URL, IMAGE_PATH


class CommentModel(db.Model):
    __tablename__ = 'comments'

    cid = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, doc="cid")  # 评论的id
    last_cid = db.Column(db.Integer, nullable=False, doc="last_cid")  # 上一级评论的id
    time = db.Column(db.String(40), nullable=False, doc="time")  # 评论时间
    comment = db.Column(db.Text, nullable=False, doc="comment")  # 评论内容
    atc_id = db.Column(db.Integer, nullable=False, doc="atc_id")  # 文章的id
    level = db.Column(db.Integer, nullable=False)  # 评论的级别
    uid = db.Column(db.Integer, nullable=False)  # 评论用户的id

    # 返回评论信息
    def data(self):
        return {"cid": self.cid,
                "time": self.time,
                "comment": self.comment}

    # 添加评论
    def add_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, atc_id, last_cid, level):
        comments = cls.query.filter_by(atc_id=atc_id, last_cid=last_cid, level=level).all()
        if len(comments) == 0:
            return []
        data_comments = []
        for comment in comments:
            data = comment.data()
            user = UserModel.find_by_uid(comment.uid)
            data["username"] = user.username
            data["head_image"] = SERVER_URL + IMAGE_PATH + user.headimage

            data["kid_comments"] = cls.get_comments(atc_id=atc_id, last_cid=data["cid"], level=level + 1)

            data_comments.append(data)

        return data_comments
