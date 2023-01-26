#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''

class Content:
    '''
    应答
    '''
    def __init__(self) -> None:
        self.name = ""
        self.comment    = ""          #对象备注
        self.fields  = []
        self.include_str_set = set()  # 包引入信息

    def clear_include(self):
        self.include_str_set.clear()

def content(*args, **kwargs):
    pass