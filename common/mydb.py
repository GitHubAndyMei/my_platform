# -*- coding: utf-8 -*-
"""
db module
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker, scoped_session

from config import CONF


def create_db_url():
    user_name = CONF.get('mysql').get('user_name')
    password = CONF.get('mysql').get('password', '')
    db = CONF.get('mysql').get('db')
    host = CONF.get('mysql').get('host')
    port = CONF.get('mysql').get('port')
    url = make_url(f'mysql+pymysql://{user_name}:{password}@{host}:{port}/{db}')
    db_url = url.update_query_dict({'charset': 'utf8mb4', 'autocommit': 'true'})
    print("db_url", db_url)
    return db_url


def create_session():
    # 初始化数据库连接:
    engine = create_engine(
        create_db_url(),
        pool_size=30,
        max_overflow=10,
        pool_pre_ping=True,
        pool_timeout=2,
        pool_recycle=10,
    )

    # 创建DBSession类型:
    session = sessionmaker(bind=engine)
    session = scoped_session(session)
    return session


mydb = create_session()

import time


def sing(t):
    from app.model.tbl_user.tbl_user import TblUser
    tb = TblUser()
    tb.user_name = f'test{t}'
    tb.password = f'test{t}'
    tb.id = t
    mydb.add(tb)
    # time.sleep(t)
    if t == 20:
        mydb.commit()
        mydb.close()

    print(id(mydb))
    time.sleep(1)


if __name__ == '__main__':
    import threading

    for i in range(0, 5):
        sing_process = threading.Thread(target=sing, args=(i * 5,))
        sing_process.start()

    # print(mydb)
