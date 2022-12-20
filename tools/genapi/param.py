#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''
import inspect

from common import G_PARAM_OWN, G_INFO_DEFINE_DICT, G_SERVICE_DEFINE_DICT

class Field:
    '''
    参数
    '''
    def __init__(self) -> None:
        self.name = ""       # 字段名称
        self.type = ""       # 字段类型
        self.min  = ""       # 下限值 对数值类型有效
        self.max  = ""       # 上限值 对数值类型有效
        self.comment = ""    # 字段备注
        
        self.var_type = ""   # 变量类型
        self.min_check = False
        self.max_check = False
        self.init_value = ""

def param(name, type, min, max, comment, default=""):
    '''
    获取参数属性
    '''

    field = Field()
    field.name = name
    field.type = type
    field.min = min
    field.max = max
    field.comment = comment
    field.init_value = default
    field.default = default

    class_name = inspect.stack()[1][3]

    if G_PARAM_OWN["type"] == 0:
        G_INFO_DEFINE_DICT[class_name].fields.append(field)
    elif G_PARAM_OWN["type"] == 1:
        G_SERVICE_DEFINE_DICT[class_name].api_list[-1].request.fields.append(field)
    else:
        G_SERVICE_DEFINE_DICT[class_name].api_list[-1].response.fields.append(field)
