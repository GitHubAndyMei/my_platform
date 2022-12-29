
"""
table t_user data model.
"""

import enum
from app.model.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text, UniqueConstraint, Index


class EnumTblUserDeleted(enum.Enum):
    DELETED_NO = 0  # 否
    DELETED_YES = 1  # 是

    @classmethod
    def get_desc(cls, enum_value: int):
        '''
        获取删除标记 值描述
        '''
        desc_dict = {
            0: '否',
            1: '是',
        }

        return desc_dict.get(enum_value, '未知状态')

class TblUser(Base):
    '''
    用户表
    '''
    # 表名
    __tablename__ = 't_user'

    # 字段定义
    id = Column(Integer, name='F_id', comment='唯一id', primary_key=True, autoincrement=True)
    username = Column(String(64), name='F_username', comment='用户账号', nullable=False, default='')
    password = Column(String(64), name='F_password', comment='用户密码', nullable=False, default='')
    deleted = Column(SmallInteger, name='F_deleted', comment='删除标记 enum:0,no,否#1,yes,是', nullable=False, default=0)
    operator = Column(String(64), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint(('F_username',), name='unique_index_t_user_username'),
    )

    # 普通索引
    Index('index_t_user_modify_time', ('F_modify_time',))  # 普通索引

    # 字段别名
    ID = 'id'  # 唯一id
    USERNAME = 'username'  # 用户账号
    PASSWORD = 'password'  # 用户密码
    DELETED = 'deleted'  # 删除标记 enum:0,no,否#1,yes,是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'username',
        'password',
        'deleted',
        'operator',
        'modify_time',
    ]

