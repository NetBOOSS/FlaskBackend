#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   api_demo.py
@Time    :   2023/07/30 12:50:54
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''

from flask_restful import Resource, request
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import get_jwt_identity
from lib import response_code, pretty_result
from lib.auth_token import user_power
from core.core_demo import DemoCore

class DemoApiResource(Resource):
    """下载数据"""

    def __init__(self):
        self.parser = RequestParser()

    @user_power()
    def post(self):
        """
            name:string
            age:int
        """
        args = request.json
        if not args.__contains__("name"):
            return pretty_result(response_code.PARAM_ERROR, "必填参数不能为空！")
        else:
            if type(args["name"]) !=str:
                return pretty_result(response_code.PARAM_TYPE_ERROR, "name参数类型错误！")
        if not args.__contains__("age"):
            return pretty_result(response_code.PARAM_ERROR, "必填参数不能为空！")
        else:
            if type(args["age"]) !=int:
                return pretty_result(response_code.PARAM_TYPE_ERROR, "age参数类型错误！")
        instantiation = DemoCore(args)
        result = instantiation.demo_post()
        return result