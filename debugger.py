#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   debugger.py
@Time    :   2023/07/30 12:49:36
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''


import logging.handlers
from app import create_app
from config import config
from flask_jwt_extended import JWTManager

app = create_app(config)
jwt = JWTManager(app)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user


@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    if token_type=='access':

        return {
            'status': 401,
            'code': 401,
            'msg': ' {} token 过期了'.format(token_type)
        }
    else:
        return {
            'status': 409,
            'code': 409,
            'msg': ' {} token 过期了'.format(token_type)
        }


def debug():
    """
    debug模式启动命令函数
    To use: python3 manager.py debug
    """
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, port=9999)


def run():
    """
    run模式启动命令函数
    To use: python3 manager.py debug
    """
    app.logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=9988)

if __name__ == '__main__':
    run()