from werkzeug.datastructures import FileStorage


def reg_args_vaild(parser):
    parser.add_argument('username', type=str, required=True, help="username error", location='args')
    parser.add_argument('password', type=str, required=True, help="pasword", location='args')
    parser.add_argument('head_image', dest='headimage', type=FileStorage, help="head_image error", required=True,
                        location='files')
