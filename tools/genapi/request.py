#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''
from common import G_PARAM_OWN, G_INFO_DEFINE_DICT, G_SERVICE_DEFINE_DICT

class Request:
    '''
    请求
    '''
    def __init__(self) -> None:
        self.name = ""
        self.comment    = ""          #对象备注
        self.fields  = []
        self.include_str_set = set()  # 包引入信息
        
    def clear_include(self):
        self.include_str_set.clear()

def request(*args, **kwargs):
    G_PARAM_OWN["type"] = 2 # request调用结束,参数类型归属于response