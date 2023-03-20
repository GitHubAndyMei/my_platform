#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：my_platform 
@File    ：tbl_role_service.py
@Author  ：sadnesspineapple
@Date    ：2023/3/20 15:39 
'''
# built-in package

# project package
from common.mydb import mydb
from .tbl_role import TblRole


# third package
class TblRoleService:
    @classmethod
    def query_roles_by_code(cls, role_codes: list):
        tbl_roles = mydb.query(TblRole).filter(TblRole.role_code.in_(role_codes)).all()
        return tbl_roles
