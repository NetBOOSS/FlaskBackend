#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/07/30 12:40:03
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''


from flask import Flask


app = Flask(__name__)


def _access_control(response):
    """
    解决跨域请求
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Max-Age"] = 86400
    return response


def create_app(conf):
    # 添加配置
    app.config.from_object(conf)
    # 解决跨域
    app.after_request(_access_control)

    from routes import api_v1

    app.register_blueprint(api_v1, url_prefix="/api/v1")
    return app