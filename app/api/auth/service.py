# -*- coding: utf-8 -*-
from common.exception import MyException
from common.result_code import ERR_USER_NOT_FOUND, ERR_PASSWORD, ERR_USER_EXISTS
from common.token import hash_password, encode_jwt
from flask import g
from app.model.tbl_user_service.tbl_user_service import TblUserService
from app.model.tbl_role_service.tbl_role_service import TblRoleService
from app.model.tbl_user_role_service.tbl_user_role_service import TblUserRoleService

from external.protocol.python.get_user_info_request import GetUserInfoRequest
from external.protocol.python.get_user_info_response import GetUserInfoResponse
from external.protocol.python.login_request import LoginRequest
from external.protocol.python.login_response import LoginResponse
from external.protocol.python.register_request import RegisterRequest
from external.protocol.python.register_response import RegisterResponse
from external.protocol.python.role_detail import RoleDetail


class AuthService(object):
    """
    示例服务
    """

    @classmethod
    def login(cls, request: LoginRequest, response: LoginResponse):
        """
        登录
        """
        # 校验用户是否已经存在
        tbl_user = TblUserService.query_user_by_username(request.username)
        if not tbl_user:
            raise MyException(ERR_USER_NOT_FOUND)

        # 哈希密码
        password = hash_password(request.password)

        # 校验密码是否正确
        if password != tbl_user.password:
            raise MyException(ERR_PASSWORD)

        # 签发token
        jwt = encode_jwt({
            "user_account": tbl_user.user_account
        }, user_account=tbl_user.user_account)
        response.set_token(jwt)

    @classmethod
    def register(cls, request: RegisterRequest, response: RegisterResponse):
        """
        注册
        """
        # 校验用户是否已经存在
        tbl_user = TblUserService.query_user_by_username(request.username)
        if tbl_user:
            raise MyException(ERR_USER_EXISTS)

        # 哈希密码
        password = hash_password(request.password)
        TblUserService.add_user(request.username,password)


    @classmethod
    def get_user_info(cls, request: GetUserInfoRequest, response: GetUserInfoResponse):
        """
        获取用户信息
        """
        tbl_user = TblUserService.query_user_by_account(g.user_account)

        tbl_user_roles = TblUserRoleService.query_roles_by_user_account(g.user_account)
        if not tbl_user_roles:
            raise MyException(ERR_USER_NOT_FOUND)

        role_codes = [t.role_code for t in tbl_user_roles]
        tbl_roles = TblRoleService.query_roles_by_code(role_codes)

        roles = []
        for t in tbl_roles:
            role = RoleDetail()
            role.set_role_code(t.role_code)
            role.set_role_name(t.role_name)
            roles.append(role)

        response.set_roles(roles)
        response.set_desc(tbl_user.desc)
        response.set_username(tbl_user.username)
