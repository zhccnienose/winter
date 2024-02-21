from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required

from ...models.users import UserModel
from ...models.comments import CommentModel

from ...schema.comment_sha import reg_args_vaild


class AtcComment(Resource):
    # 创建评论
    @jwt_required()
    def post(self, id):
        parser = reqparse.RequestParser()
        reg_args_vaild(parser)
        data = parser.parse_args()

        # print(data)
        try:
            user = UserModel.find_by_username(get_jwt_identity())
            data["uid"] = user.uid  # 用户id
            data["atc_id"] = id  # 文章id

            comment = CommentModel(**data)
            comment.add_comment()

            return jsonify(code=200, msg="评论成功")
        except Exception as e:
            return jsonify(code=500, msg=str(e))

    # 获取该文章的评论列表
    def get(self, id):
        last_cid = 0
        comments = CommentModel.query.filter_by(atc_id=id, last_cid=last_cid).all()
        data_comment = []

        data_comment = CommentModel.get_comments(atc_id=id, last_cid=0, level=1)
        return jsonify(code=200, msg="success", data=data_comment)
