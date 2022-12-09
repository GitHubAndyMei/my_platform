# -*- coding: utf-8 -*-
"""
project config module
"""
import os
import yaml

PROJECT_NAME = 'ct_platform'
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

LOG_PATH  = os.path.join(PROJECT_PATH, "log")
CONF_PATH = os.path.join(PROJECT_PATH, "config")

def load_config():
    """获取配置文件"""
    env = os.environ.get('ct_env', 'dev')
    config_filepath = os.path.join(CONF_PATH, f'{env}.yml')

    with open(config_filepath, "r") as f:  
        conf_dict = yaml.load(f.read(), Loader=yaml.SafeLoader)
    print(f"env: {env}, config: {conf_dict}")
    return conf_dict

CONF = load_config()