# built-in package
import time

# project package
from common.token import decode_jwt, encode_jwt
from common.myredis import MyRedis
from common.exception import MyException
from common.result_code import USER_NO_LOGIN, TOKEN_EXPIRED

# third package
from flask import request, g


def login_require(func):
    def inner(*args, **kwargs):
        """
        登录校验
        1.校验token是否存在
        2.token解码，判断token是否异常
        3.判断token是否过期
        4.如果token过期一半，需要去redis中读取，重新刷新token
        5.设置全局user_account
        """
        token = request.headers.get("Authorization")
        # 校验token准确性
        if not token:
            raise MyException(USER_NO_LOGIN)

        # 对token解码，判断token准确性
        try:
            payload = decode_jwt(token)
        except Exception as e:
            raise MyException(USER_NO_LOGIN)

        # 判断token是否过期
        ex = payload.get("ex")
        user_account = payload.get("user_account")
        if ex < int(time.time()):
            redis = MyRedis()
            flag = redis.get(user_account)
            if flag:
                # 延长token时间
                # 设置全局变量的token,最后在响应头中进行设置
                g.token = encode_jwt(payload, user_account)
            else:
                # token完全过期
                raise MyException(TOKEN_EXPIRED)

        # 设置user_account
        g.user_account = payload.get("user_account")

        # 走正常的视图函数
        result = func(*args, **kwargs)

        return result

    return inner
