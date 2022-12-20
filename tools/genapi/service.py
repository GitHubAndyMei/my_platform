#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''

import inspect

from common import G_PARAM_OWN, G_INFO_DEFINE_DICT, G_SERVICE_DEFINE_DICT

class Service:
    '''
    服务
    '''
    def __init__(self) -> None:
        self.name      = ""                    # 对象名称
        self.comment   = ""                    # 对象备注
        self.owner     = ""                    # 服务所有者
        self.api_list  = []                    # 接口列表
        self.include_str_set = set()           # 包引入信息
        
    def clear_include(self):
        self.include_str_set.clear()
          
def service(comment, owner):
    obj         = Service()
    obj.name    = inspect.stack()[1][3]
    obj.comment = comment
    obj.owner   = owner
    G_SERVICE_DEFINE_DICT[obj.name] = obj