#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''
import inspect

from service import *
from request import *
from response import *
from common import *

class Api:
    '''
    接口
    '''
    def __init__(self) -> None:
        self.type = ""
        self.url  = ""
        self.comment = ""
        self.request  = Request()
        self.response = Response()
        
        self.function = "" # api调用的method

def api(method: str, url: str, comment: str, function=None):
    obj = Api()
    obj.method = method
    obj.url = url
    obj.comment = comment
    obj.function =  function if function else url.split('/')[-1] # 设置url最后一个分割为api调用方法名
    obj.request.name = get_camel_style_name(obj.function)+"Request"
    obj.request.comment = comment
    obj.response.name = get_camel_style_name(obj.function)+"Response"
    obj.response.comment = comment
    
    service_name = inspect.stack()[1][3]
    G_SERVICE_DEFINE_DICT[service_name].api_list.append(obj)
    G_PARAM_OWN["type"] = 1 # 首次调用api,参数类型归属于request
    
def API(api, request, response):
    pass