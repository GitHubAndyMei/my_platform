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
from .tbl_user_role import TblUserRole


# third package
class TblUserRoleService:
    @classmethod
    def query_roles_by_user_account(cls, user_account):
        tbl_user_roles = mydb.query(TblUserRole).filter(TblUserRole.user_account == user_account).all()
        return tbl_user_roles

