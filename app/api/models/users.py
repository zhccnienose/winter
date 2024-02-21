import os
from app.config import UPLOAD_FOLDER

from ..models import db
from ..common.utils import pil_base64


# 用户类
class UserModel(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, doc="uid")  # 用户ID
    username = db.Column(db.String(50), nullable=False, doc="username")  # 用户名
    password = db.Column(db.String(255), nullable=False, doc="password")  # 用户密码
    salt = db.Column(db.String(255), nullable=False, doc="salt")
    headimage = db.Column(db.Text, nullable=False, doc="image")  # 用户头像名称

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def data(self):
        head_image_path = os.path.join(UPLOAD_FOLDER, self.headimage)
        head_image = pil_base64(head_image_path)
        
        return {
            "uid": self.uid,
            "username": self.username,
            "head_image": head_image
        }

    def get_pwd(self):
        return {
            "pwd": self.password,
            "salt": self.salt,
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_uid(cls, uid):
        return db.session.execute(db.select(cls).filter_by(uid=uid)).first()

    @classmethod
    def get_all_user(cls):
        return db.session.query(cls).all()
