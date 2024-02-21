def reg_args_vaild(parser):
    parser.add_argument('username', type=str, required=True, location='args')
    parser.add_argument('password', type=str, required=True, location='args')