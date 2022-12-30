
"""
table t_permission data model.
"""

import enum
from app.model.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text, UniqueConstraint, Index


class TblPermission(Base):
    '''
    权限表
    '''
    # 表名
    __tablename__ = 't_permission'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    permission_code = Column(String(64), name='F_permission_code', comment='权限代码', nullable=False, default='')
    permission_name = Column(String(64), name='F_permission_name', comment='权限名称', nullable=False, default='')
    parent_per_code = Column(String(64), name='F_parent_per_code', comment='父权限代码', nullable=False, default='')
    url = Column(String(128), name='F_url', comment='路径地址', nullable=False, default='')
    sort = Column(Integer, name='F_sort', comment='排序位置，默认最后一个', nullable=False, default=999)
    deleted = Column(String(1), name='F_deleted', comment='删除标记 0-否 1-是', nullable=False, default='0')
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_permission_code', name='F_permission_code'),
    )

    # 普通索引
    Index('index_t_permission_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    PERMISSION_CODE = 'permission_code'  # 权限代码
    PERMISSION_NAME = 'permission_name'  # 权限名称
    PARENT_PER_CODE = 'parent_per_code'  # 父权限代码
    URL = 'url'  # 路径地址
    SORT = 'sort'  # 排序位置，默认最后一个
    DELETED = 'deleted'  # 删除标记 0-否 1-是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'permission_code',
        'permission_name',
        'parent_per_code',
        'url',
        'sort',
        'deleted',
        'operator',
        'modify_time',
    ]

