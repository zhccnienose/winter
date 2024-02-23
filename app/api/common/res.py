from flask import jsonify


# 返回信息
def res(code: int, msg: str, data=None):
    if data is None:
        response = jsonify({'code': code, 'msg': msg})
        response.status_code = code
    else:
        response = jsonify({'code': code, 'msg': msg, 'data': data})
        response.status_code = code

    return response
