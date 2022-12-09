# -*- coding: utf-8 -*-
"""
redis api module
"""
import sys
sys.path.append("..")

import redis
from config import CONF

class MyRedis:
    def __init__(self, db=CONF.get("redis").get("db")):
        _pool = redis.ConnectionPool(
            db=db,
            host=CONF.get("redis").get("host"),
            port=CONF.get("redis").get("port"),
            password=CONF.get("redis").get("password"),
            decode_responses=CONF.get("redis").get("decode_response")
        )
        self._redis_cli = redis.Redis(connection_pool=_pool, charset=CONF.get("redis").get("charset"))

    def sadd(self, name, val):
        return self._redis_cli.sadd(name, val)

    def srem(self, name, *args):
        return self._redis_cli.srem(name, *args)

    def hsetnx(self, name: str, key: str, val: str):
        """
        Redis Hsetnx 命令
        哈希表中不存在的的字段赋值,
        如果哈希表不存在, 一个新的哈希表被创建并进行HSET操作
        如果字段已经存在于哈希表中, 操作无效
        如果key不存在, 一个新哈希表被创建并执行HSETNX命令
        @return success return 1, fail return 0
        @rtype int
        """
        return self._redis_cli.hsetnx(name, key, val)  # 1成功 0失败

    def set(self, name: str, val, *args, **kwargs):
        """
        set key value
        """
        return self._redis_cli.set(name, val, *args, **kwargs)

    def get(self, name):
        """
        get key
        """
        return self._redis_cli.get(name)

    def delete(self, *names: str):
        """
        del key
        """
        self._redis_cli.delete(*names)

    def hget(self, name: str, key: str):
        """
        hash get
        """
        return self._redis_cli.hget(name, key)

    def hdel(self, name: str, key: str):
        """
        hash delete
        """
        self._redis_cli.hdel(name, key)

    def expire(self, name: str, seconds: int):
        """
        set expire time
        """
        return self._redis_cli.expire(name, seconds)


if __name__ == '__main__':
    redis_obj = MyRedis()
    redis_obj.set("test", 123456)
    print(redis_obj.get("test"))