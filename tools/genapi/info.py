#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''

import inspect
from common import G_PARAM_OWN, G_INFO_DEFINE_DICT

class Info:
    '''
    服务
    '''
    def __init__(self) -> None:
        self.name       = ""                    #对象名称
        self.comment    = ""                    #对象备注
        self.fields = []                    #字段列表
        
        self.include_str_set = set()            # 包引入信息
        
    def clear_include(self):
        self.include_str_set.clear()
    
def info(comment):
    service_obj = Info()
    service_obj.name = inspect.stack()[1][3]
    service_obj.comment = comment
    G_INFO_DEFINE_DICT[service_obj.name] = service_obj
    G_PARAM_OWN["type"] = 0 # 首次调用info,参数类型归属于info