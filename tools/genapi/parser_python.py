# -*- coding: UTF-8 -*-

from common import G_INFO_DEFINE_DICT, G_SERVICE_DEFINE_DICT, PARAM_TYPE_DICT,PYTHON_VAR_TYPE_DICT, get_camel_style_name, get_lower_underline_name

class ParserPython:
    @staticmethod
    def _parse_field(field, field_own_obj):
        if field.type not in PARAM_TYPE_DICT: # 自定义类
            if "vector" in field.type: # 自定义类数组
                field.init_value = "[]"
                reference_type = field.type.replace("vector", "").replace("<", "").replace(">", "") # 引用类型
                # 自定义类需要导入自定义类的包文件
                if reference_type not in PARAM_TYPE_DICT:
                    field_own_obj.include_str_set.add("from %s import *"%get_lower_underline_name(reference_type))
            else:
                field.init_value = field.type+"()"
                field_own_obj.include_str_set.add("from %s import *"%get_lower_underline_name(field.type))
        else: # 基本数据类型
            field.init_value = field.init_value if field.init_value else PYTHON_VAR_TYPE_DICT[field.type][1]
            
            # 设置参数字段检查标志
            if field.min != "MIN" and field.type != "bool":
                field.min_check = True
            if field.max != "MAX" and field.type != "bool":
                field.max_check = True

    
    @staticmethod
    def parse():
        # 解析普通类
        for info_name,info in G_INFO_DEFINE_DICT.items():
            for field in info.fields:
                ParserPython._parse_field(field, info)
            
        # 解析request,response类
        for service_name,service in G_SERVICE_DEFINE_DICT.items():
            for api in service.api_list:
                # 解析参数字段
                for field in api.request.fields:
                    ParserPython._parse_field( field,  api.request)
                for field in api.response.fields:
                    ParserPython._parse_field( field, api.response)
                    
                # 将request,response中导入的包加到service导入中
                for node in api.request.include_str_set:
                    service.include_str_set.add(node)
                for node in api.response.include_str_set:
                    service.include_str_set.add(node)
            
            # 导入request,response包
            for api in service.api_list:     
                import_str = "from {}_request import {}Request".format(api.function, get_camel_style_name(api.function))
                service.include_str_set.add( import_str )
                import_str = "from {}_response import {}Response".format(api.function, get_camel_style_name(api.function))
                service.include_str_set.add( import_str )