from flask import Blueprint
from flask_restful import Api

from app.api.resources.users.register import Register
from app.api.resources.users.login import Login
from app.api.resources.users.exit import Exit
from app.api.resources.users.get_user import GetUser

from app.api.resources.users.head_image.image_file import UsersHeadImage

from app.api.resources.user_change.change_headimage import ChangeHeadimage
from app.api.resources.user_change.change_username import ChangeUsername
from app.api.resources.user_change.change_password import ChangePassword

from app.api.resources.article.add_articles import Articles
from app.api.resources.article.del_article import DelArticle

from app.api.resources.article.get_atc_mine import GetMyArticles
from app.api.resources.article.get_atc_like import GetAtcLike
from app.api.resources.article.get_atc_collect import GetAtcCollect
from app.api.resources.article.get_atc_new import GetAtcNew
from app.api.resources.article.get_atc_hot import GetAtcHot

from app.api.resources.atc_hclc.atc_hit import AtcHit
from app.api.resources.atc_hclc.atc_like import AtcLike
from app.api.resources.atc_hclc.atc_collect import AtcCollect
from app.api.resources.atc_hclc.atc_comment import AtcComment

# 用户蓝图
user_bp = Blueprint('users', __name__, url_prefix='/users')
user_change_bp = Blueprint('user_change', __name__, url_prefix='/users/changes')
article_bp = Blueprint('artilce', __name__, url_prefix='/articles')

# 初始化蓝图
user = Api(user_bp)
user_change = Api(user_change_bp)
article = Api(article_bp)

# 用户信息
user.add_resource(Register, '/register/')
user.add_resource(Login, '/login/')
user.add_resource(Exit, "/exit/")
user.add_resource(GetUser, "/information/")

# 用户头像
user.add_resource(UsersHeadImage, "/images/files/<image_name>")

# 用户信息修改
user_change.add_resource(ChangeHeadimage, '/head/')
user_change.add_resource(ChangeUsername, "/username/")
user_change.add_resource(ChangePassword, "/password/")

# 文章编辑
article.add_resource(Articles, "/editor/")

# 文章删除
article.add_resource(DelArticle, "/<int:id>")

# 文章列表
article.add_resource(GetMyArticles, "/mine")  # 我写的
article.add_resource(GetAtcLike, "/likes")  # 我点赞的
article.add_resource(GetAtcCollect, "/collections")  # 我收藏的
article.add_resource(GetAtcNew, "/new")  # 最新的
article.add_resource(GetAtcHot, "/hot")  # 热门的（点击量最多）

# 文章内容页
article.add_resource(AtcHit, "/<id>/hits/")  # 点击
article.add_resource(AtcLike, "/<id>/likes/")  # 点赞
article.add_resource(AtcCollect, "/<id>/collections/")  # 收藏
article.add_resource(AtcComment, "/<id>/comments/")  # 评论
