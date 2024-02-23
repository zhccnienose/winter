def reg_args_vaild(parser):
    # 评论内容
    parser.add_argument('comment', type=str, required=True, help="content error", location="args")
    # 评论时间
    parser.add_argument('time', type=str, required=True, help="time error", location="args")
    # 评论级别
    parser.add_argument('level', type=int, required=True, help="level error", location="args")
    # 上级评论id
    parser.add_argument('last_cid', type=int, required=True, help="last_cid error", location="args")
