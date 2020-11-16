import json
from flask import Flask
import flask
"""
1. 导入：import flask,json
2. 实例化：api = flask.Flask(__name__)
3. 定义接口访问路径及访问方式：@api.route('/index',methods=['get/post/PUT/DELETE'])
4. 定义函数，注意需与路径的名称一致，设置返回类型并支持中文：def index(): return json.dumps(ren,ensure_ascii=False)
5. 三种格式入参访问接口：
5.1 url格式入参：flask.request.args.get('id')
5.2 form-data格式入参：pwd = flask.request.values.get('pwd')
5.3 josn格式入参：pwd = flask.request.json.get('pwd')
6. 启动服务：api.run(port=8888,debug=True,host='127.0.0.1')，开启服务之后，就可以通过ip+端口+路径+入参访问接口

"""
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__)


# 'index'是接口路径，methods不写，默认get请求
@api.route('/index', methods=['get'])
def index():
    response = {'msg': '成功访问首页', 'msg_code': 200}
    # json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
    return json.dumps(response, ensure_ascii=False)


# #  post入参访问方式一：url格式参数
# @api.route('/article', methods=['post'])
# def article():
#     ids = flask.request.args.get('id')
#     if ids:
#         if ids == '123456':
#             res = {'msg': '成功访问文章', 'msg_code': 200}
#         else:
#             res = {'msg': '找不到文章', 'msg_code': 400}
#     else:
#         res = {'msg': '请输入文章id参数', 'msg_code': -1}
#     return json.dumps(res, ensure_ascii=False)
#
#
# # post入参访问方式二：from-data（k-v）格式参数
# @api.route('/login', methods=['post'])
# def login():
#     # from-data格式参数
#     usrname = flask.request.values.get('username')
#     pwd = flask.request.values.get('123456')
#     if usrname and pwd:
#         if usrname == 'username' and pwd == '123456':
#             ren = {'msg': '登录成功', 'msg_code': 200}
#         else:
#             ren = {'msg': '用户名或密码错误', 'msg_code': -1}
#     else:
#         ren = {'msg': '用户名或密码为空', 'msg_code': 1001}
#     return json.dumps(ren, ensure_ascii=False)
#
#
# #  post入参访问方式二：josn格式参数
# @api.route('/loginjosn', methods=['post'])
# def loginjosn():
#     # from-data格式参数
#     usrname = flask.request.json.get('username')
#     pwd = flask.request.json.get('pwd')
#     if usrname and pwd:
#         if usrname == 'root' and pwd == 'root':
#             ren = {'msg': '登录成功', 'msg_code': 200}
#         else:
#             ren = {'msg': '用户名或密码错误', 'msg_code': -1}
#     else:
#         ren = {'msg': '用户名或密码为空', 'msg_code': 1001}
#     return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8866, debug=False)





