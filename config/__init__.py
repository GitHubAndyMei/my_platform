# -*- coding: utf-8 -*-
"""
project config module
"""
import os
import yaml
from config.config import CONF_PATH
from config.config import ENV


def load_config():
    """获取配置文件"""
    config_filepath = os.path.join(CONF_PATH, f'{ENV}.yml')

    with open(config_filepath, "r") as f:
        conf_dict = yaml.load(f.read(), Loader=yaml.SafeLoader)
    # print(f"env: {env}, config: {conf_dict}")
    return conf_dict


# 这里的配置文件读取的是较为隐私的信息
CONF = load_config()

