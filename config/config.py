# -*- coding: utf-8 -*-
"""
project config module
项目中常用的常量可以配置在这边
"""
import os

PROJECT_NAME = 'ct_platform'
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

LOG_PATH = os.path.join(PROJECT_PATH, "log")
CONF_PATH = os.path.join(PROJECT_PATH, "config")

DAY = 60 * 60 * 24
JWT_EXPIRED_TIME = DAY * 30
ENV = os.environ.get('ct_env', 'dev')