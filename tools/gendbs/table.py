#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pymysql
from config import IP, PORT, user_name, PASSWORD, DATABASE


class Field(object):
    def __init__(self, name, data_type,default, comment, is_pk, which_table):
        self.name = name
        self.data_type = data_type
        self.default = default
        self.comment = comment
        self.is_pk = is_pk
        self.which_table = which_table

class TableIndex:
    '''
    数据库索引对象
    '''
    def __init__(self) -> None:
        self.key_name     = "" # 索引名称
        self.unique_flag  = False # 唯一索引
        self.column_names = [] # 索引字段名称 按字段序号排序

class Table(object):
    def __init__(self, table_info):
        self.name = table_info[0]
        self.comment = table_info[1]
        self.fields = []
        self.primary_index = TableIndex()
        self.unique_index_dict = {} #  {"key_name":["DbIndex"]}
        self.index_dict = {}        #  {"key_name":["DbIndex"]}
        self.all_index_field_names = []
        index_infos = self.show_index_from_table(self.name)
        for index in index_infos:
            non_unique   = index[1]
            key_name     = index[2]
            seq_in_index = index[3]
            column_name  = index[4]

            if key_name == 'PRIMARY':
                self.primary_index.key_name = key_name
                self.primary_index.unique_flag = True
                self.primary_index.column_names.append(column_name)
                self.all_index_field_names.append(column_name)
            elif non_unique == 0: # 唯一索引
                if key_name not in self.unique_index_dict.keys():
                    self.unique_index_dict[key_name] = TableIndex()
                self.unique_index_dict[key_name].key_name = key_name
                self.unique_index_dict[key_name].unique_flag = True
                self.unique_index_dict[key_name].column_names.append(column_name)
                self.all_index_field_names.append(column_name)
            else:
                if key_name not in self.index_dict.keys():
                    self.index_dict[key_name] = TableIndex()
                self.index_dict[key_name].key_name = key_name
                self.index_dict[key_name].unique_flag = True
                self.index_dict[key_name].column_names.append(column_name)
                self.all_index_field_names.append(column_name)

        for record in self.show_full_fields_from_table(self.name):
            is_pk = False
            if record[4] == "PRI":
                is_pk = True
            if record[0] != 'id':
                self.fields.append(Field(record[0], record[1], record[5], record[8], is_pk, table_info))

    @staticmethod
    def show_full_fields_from_table(name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=user_name,
                             password=PASSWORD,
                             database=DATABASE,
                             charset="utf8")
        cursor = db.cursor()
        # 获取表的所有字段信息
        '''
        mysql字段定义类：show full fields from name
        字段信息格式如下
        Field: Fdevice_id
        Type: int
        Collation: NULL
        Null: NO
        Key: PRI
        Default: NULL
        Extra: auto_increment
        Privileges: select,insert,update,references
        Comment: 设备id
        '''
        sql = "show full fields from %s" % name
        cursor.execute(sql)
        records = cursor.fetchall()
        db.close()
        return records

    @staticmethod
    def show_table(name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=user_name,
                             password=PASSWORD,
                             database=DATABASE)
        cursor = db.cursor()
        sql = f"""
        SELECT
            TB.TABLE_NAME,      -- 表名
            TB.TABLE_COMMENT   -- 表名注释
        FROM
            INFORMATION_SCHEMA.TABLES TB
        Where TB.TABLE_SCHEMA = '{name}' -- 数据库名
        """
        cursor.execute(sql)
        records = cursor.fetchall()

        db.close()

        return records

    @staticmethod
    def show_index_from_table(table_name):
        db = pymysql.connect(host=IP,
                             port=PORT,
                             user=user_name,
                             password=PASSWORD,
                             database=DATABASE)
        cursor = db.cursor()
        sql = f"show index from {table_name}"
        cursor.execute(sql)
        records = cursor.fetchall()

        db.close()

        return records


class Table_init(object):
    def __init__(self, name):
        self.name = name
