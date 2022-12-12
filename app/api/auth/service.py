# -*- coding: utf-8 -*-
from app.model.tbl_user import TblUser
from common.mydb import mydb
from common.exception import CtException
from common.result_code import ERR_USER_NOT_FOUND,ERR_PASSWORD
from common.utils import hash_password, encode_jwt

from external.protocol.python.login_request import LoginRequest
from external.protocol.python.login_response import LoginResponse


class AccountService(object):
    """
    示例服务
    """

    @classmethod
    def login(cls, request: LoginRequest, response: LoginResponse):
        """
        登录
        """
        # 校验用户是否已经存在
        user = mydb.query(TblUser).filter(TblUser.username == request.username).first()
        if not user:
            raise CtException(ERR_USER_NOT_FOUND)

        # 哈希密码
        password = hash_password(request.password)

        # 校验密码是否正确
        if password != user.password:
            raise CtException(ERR_PASSWORD)

        # 签发token
        jwt = encode_jwt({
            "user_name": user.username
        }, user_id=user.id)
        print(jwt)
        response.set_jwt(jwt)
