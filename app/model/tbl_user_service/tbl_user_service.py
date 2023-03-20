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
from .tbl_user import TblUser


# third package
class TblUserService:
    @classmethod
    def query_user_by_account(cls, user_account):
        tbl_user = mydb.query(TblUser).filter(TblUser.user_account == user_account).first()
        return tbl_user

    @classmethod
    def query_user_by_username(cls, username):
        tbl_user = mydb.query(TblUser).filter(TblUser.username == username).first()
        return tbl_user

    @classmethod
    def add_user(cls, username, password):
        tbl_user = TblUser()
        tbl_user.password = password
        tbl_user.user_name = username
        mydb.add(tbl_user)
        mydb.commit()
