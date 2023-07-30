#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   api_file.py
@Time    :   2023/07/30 12:57:15
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''


from flask_restful import Resource, request
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import get_jwt_identity
from lib import response_code, pretty_result
from lib.auth_token import user_power
from core.core_file import FileCore

class FileUploadResource(Resource):
    """上传数据"""

    def post(self):
        # 定义参数解析器
        if not request.form.__contains__("name"):
            return pretty_result(response_code.PARAM_ERROR, "必填参数不能为空！")
        # request.form获取到的所有参数都是str，如果需要转码的话需要自己操作一下
        args = {
            "name": int(request.form.get("name")),
        }
        file = request.files.get("file")
        if not file:
            return pretty_result(response_code.PARAM_ERROR, "文件上传，你不传文件，你是瓜皮么")

        instantiation = FileCore(args)
        result = instantiation.upload_file(file)
        return result