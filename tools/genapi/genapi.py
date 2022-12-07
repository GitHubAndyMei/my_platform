#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 20220701
@author:andymei
'''
#import system package
import sys
import os
import argparse
from mako.template import Template

#import usr package
from common import *
from parser_python import *

def gen_python_view(obj, pre_str, output_dir):
    template = Template(filename=os.path.join(template_path, '%s.py.template'%pre_str), input_encoding='UTF-8')
    out_file_name = '{}.py'.format( get_lower_underline_name(obj.name.replace("Srv", "View")) )
    fd = open(os.path.join(output_dir, out_file_name), 'wb+')
    fd.write(template.render(CLASS=obj).encode("UTF-8"))
    fd.close()
    del template
    # obj.clear_include()
    print( os.path.join(output_dir, out_file_name) )

def gen_python(obj, pre_str, output_dir):
    template = Template(filename=os.path.join(template_path, '%s.py.template'%pre_str), input_encoding='UTF-8')
    out_file_name = '{}.py'.format( get_lower_underline_name(obj.name) )
    print(out_file_name)
    fd = open(os.path.join(output_dir, out_file_name), 'wb+')
    fd.write(template.render(CLASS=obj).encode("UTF-8"))
    fd.close()
    del template
    print( os.path.join(output_dir, out_file_name) )

if __name__ == '__main__':
    # 解析命令行参数
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--idl_path",   help="数据结构定义文件路径")
    args = arg_parser.parse_args()

    idl_path   = args.idl_path

    # 检查协议文件是否存在
    if not os.path.exists(idl_path):
        print("error:not find file:%s" % idl_path)
        sys.exit(-1)
    
    # 导入协议文件包
    idl_dir, idl_file_name = os.path.split(os.path.abspath(idl_path))
    sys.path.append(idl_dir)
    module = __import__(idl_file_name.split(".")[0])

    ParserPython.parse()
    out_file = "../../app/router.py"
    with open(out_file, 'wb+') as f:
        template = Template(filename='./template/router.py.template', input_encoding='UTF-8')
        f.write(template.render(SERVICE_DICT=G_SERVICE_DEFINE_DICT).encode("UTF-8"))
    print(f"路由文件生成完毕: {out_file}")

    for import_name, info in G_INFO_DEFINE_DICT.items():
        out_file = os.path.join("../../external/protocol/python", f'{get_lower_underline_name(info.name)}.py')
        with open(out_file, 'wb+') as f:
            template = Template(filename='./template/xxo.py.template', input_encoding='UTF-8')
            f.write(template.render(INFO=info).encode("UTF-8"))
        print(f"数据文件生成完毕: {out_file}")

    for import_name, service in G_SERVICE_DEFINE_DICT.items():
        out_file = os.path.join("../../app/api", f'{service.name.lower()}/controller.py')
        with open(out_file, 'wb+') as f:
            template = Template(filename='./template/controller.py.template', input_encoding='UTF-8')
            f.write(template.render(SERVICE=service).encode("UTF-8"))
        print(f"视图文件生成完毕: {out_file}")

        out_file = os.path.join("../../app/api", f'{service.name.lower()}/service.py')
        with open(out_file, 'wb+') as f:
            template = Template(filename='./template/service.py.template', input_encoding='UTF-8')
            f.write(template.render(SERVICE=service).encode("UTF-8"))
        print(f"服务文件生成完毕: {out_file}")

        for api in service.api_list:
            out_file = os.path.join("../../external/protocol/python", f'{get_lower_underline_name(api.request.name)}.py')
            with open(out_file, 'wb+') as f:
                template = Template(filename='./template/xxo.py.template', input_encoding='UTF-8')
                f.write(template.render(INFO=api.request).encode("UTF-8"))
            print(f"接口文件生成完毕: {out_file}")

            out_file = os.path.join("../../external/protocol/python", f'{get_lower_underline_name(api.response.name)}.py')
            with open(out_file, 'wb+') as f:
                template = Template(filename='./template/xxo.py.template', input_encoding='UTF-8')
                f.write(template.render(INFO=api.response).encode("UTF-8"))
            print(f"接口文件生成完毕: {out_file}")

    out_file = os.path.join("../../external/protocol/README.MD")
    with open(out_file, 'wb+') as f:
        template = Template(filename='./template/README.md.template', input_encoding='UTF-8')
        f.write(template.render(SERVICE_DICT=G_SERVICE_DEFINE_DICT).encode("UTF-8"))
    print(f"接口文档生成完毕: {out_file}")