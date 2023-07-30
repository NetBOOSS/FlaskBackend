#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   api_user.py
@Time    :   2023/07/30 13:39:37
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''


from flask_restful import Resource, request
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import get_jwt_identity
from lib import response_code, pretty_result
from lib.auth_token import user_power
from core.core_user import UserCore