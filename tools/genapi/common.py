# -*- coding: UTF-8 -*-
G_INFO_DEFINE_DICT = {}
G_SERVICE_DEFINE_DICT = {}
G_PARAM_OWN = {"type": 0} # 参数归属 0-info 1-request 2-response

PARAM_TYPE_DICT = {
        "int":      "0",
        "uint32_t": "0",
        "int64_t":  "0",
        "uint64_t": "0",
        "float":    "0.0",
        "double":   "0.0",
        "bool":     "false",
        "string":   "\"\"",
        "dict":     {}
    }

PYTHON_VAR_TYPE_DICT = {
        "int":      ["int", "0"],
        "uint32_t": ["int", "0"],
        "int64_t":  ["int", "0"],
        "uint64_t": ["int", "0"],
        "float":    ["float", "0.0"],
        "double":   ["float", "0.0"],
        "bool":     ["bool", "False"],
        "string":   ["str", "\"\""],
        "dict":     ["Dict", "{}"]
    }

def get_camel_style_name(name):
    '''
    下划线转驼峰
    '''
    if name != None:
        tmp = ""
        segs = name.split('_')
        for seg in segs:
            part = ( seg[0].upper() + seg[1:len(seg)] if len(seg) >= 1 else seg )
            tmp = tmp + part
        return tmp
    return name

def get_lower_underline_name(name):
    '''
    把非首字符为大小前加"_",并将大写转小写
    '''
    name_new = name[0]
    for i in range(1,len(name)):
        if name[i].isupper():
            name_new += "_" + name[i]
        else:
            name_new += name[i]
            
    return name_new.lower()