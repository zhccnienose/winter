from ..models import db


# 已过期的token表
class TokenModel(db.Model):
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jti = db.Column(db.String(255))

    # token注销
    def add(self):
        db.session.add(self)
        db.session.commit()

    # 查询token是否注销
    @classmethod
    def check(cls, jti):
        return bool(cls.query.filter_by(jti=jti).first())
