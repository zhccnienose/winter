def reg_args_vaild(parser):
    # 文章内容
    parser.add_argument('title', type=str, required=True, help="title error", location='args')
    parser.add_argument('content', type=str, required=True, help="content error", location='args')
    # 创建时间
    parser.add_argument("create_time", type=str, required=True, help="create-time error", location='args')
