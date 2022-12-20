#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from mako.template import Template
from template_param import *
from config import DATABASE, MODEL_OUTDIR, MODEL_TEMP, MODEL_INIT_TEMP, MODEL_README_TEMP
from table import *

def gen_code(table_name):
    table_info_tuple = Table.show_table(table_name)
    tableInit = Table_init(table_info_tuple)
    # 生成__init__.py
    f_init = open(os.path.join(MODEL_OUTDIR, "__init__.py"), 'wb+')
    init_temp = Template(filename=MODEL_INIT_TEMP, input_encoding='UTF-8')
    f_init.write(init_temp.render(TEMPLATE_PARAM=tableInit).encode("utf-8"))
    f_init.close()
    del init_temp

    # 生成model.py
    for table_info in table_info_tuple:
        table = Table(table_info)
        fp = open(os.path.join(MODEL_OUTDIR, f'tbl_{table.name[2:]}.py'), 'wb+')
        template = Template(filename=MODEL_TEMP, input_encoding='UTF-8')
        fp.write(template.render(TABLE=table).encode("utf-8"))
        fp.close()
        del template

    table_list = []
    table_name_sorted_list = sorted([table_name for table_name in table_info_tuple],key=lambda i: i)
    for table_info in table_name_sorted_list:
        table_list.append(Table(table_info))

    # 生成readme文件
    fp = open(os.path.join(MODEL_OUTDIR, "README.md"), 'wb+')
    template = Template(filename=MODEL_README_TEMP, input_encoding='UTF-8')
    fp.write(template.render(TABLES=table_list).encode("utf-8"))
    fp.close()
    del template

if __name__ == '__main__':
    gen_code(DATABASE)
