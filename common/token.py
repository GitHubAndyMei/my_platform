# built-in package
import jwt
import time
import hashlib

# project package
from config import CONF
from config.config import JWT_EXPIRED_TIME
from common.myredis import MyRedis


# third package


def hash_password(password):
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()


def encode_jwt(payload: dict, user_account: str):
    payload.update({
        "user_account": user_account,
        "ex": JWT_EXPIRED_TIME
    })
    encoding_jwt = jwt.encode(payload, CONF["jwt"]["key"], algorithm=CONF["jwt"]["algorithm"])
    r = MyRedis()
    r.set(user_account, "1", ex=JWT_EXPIRED_TIME)
    return encoding_jwt


def decode_jwt(token):
    payload = jwt.decode(token, CONF["jwt"]["key"], algorithms=CONF["jwt"]["algorithm"])
    return payload
