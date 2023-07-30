#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2023/07/30 12:47:22
@Author  :   NetB0SS
@Version :   1.0
@Desc    :   None
'''



import os
from datetime import timedelta


config_mode = "development"


class DevelopConfig(object):
    """
    开发配置
    """

    BIND = "0.0.0.0:9999"
    WORKERS = 2
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30
    LOG_LEVEL = "DEBUG"
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), "logs")
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = "run.pid"
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://xxxxx:xxxxx@xxxxxx/xxxxxxx"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_MAX_OVERFLOW = 40
    SQLALCHEMY_POOL_RECYCLE = 60
    SQLALCHEMY_POOL_TIMEOUT = 180
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "eB3p7/P7J912QWE@##$6V}a6BKgy*.Xc(F"
    JWT_TOKEN_LOCATION = "headers"
    JWT_HEADER_TYPE = "jwt"
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=3600 * 24)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=3600 * 24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=3600 * 72)
    JWT_ALGORITHM = "HS256"
class ProductConfig(object):
    """
    生产配置
    """

    BIND = "0.0.0.0:9999"
    WORKERS = 4
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30
    LOG_LEVEL = "DEBUG"
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), "logs")
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = "run.pid"


if config_mode == "development":
    config = DevelopConfig()
else:
    config = ProductConfig()


a = 0
