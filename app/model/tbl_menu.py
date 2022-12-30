
"""
table t_menu data model.
"""

import enum
from app.model.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text, UniqueConstraint, Index,text


class TblMenu(Base):
    '''
    菜单表
    '''
    # 表名
    __tablename__ = 't_menu'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    menu_code = Column(String(64), name='F_menu_code', comment='菜单代码', nullable=False, default='')
    menu_name = Column(String(64), name='F_menu_name', comment='菜单名称', nullable=False, default='')
    icon = Column(String(64), name='F_icon', comment='菜单图标', nullable=False, default='')
    sort = Column(Integer, name='F_sort', comment='排序位置，默认最后一个', nullable=False, default=999)
    parent = Column(String(64), name='F_parent', comment='父级菜单 0-否 1-是', nullable=False, default='0')
    is_link = Column(String(1), name='F_is_link', comment='是否外链 0-否 1-是', nullable=False, default='0')
    deleted = Column(String(1), name='F_deleted', comment='删除标记 0-否 1-是', nullable=False, default='0')
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_menu_code', name='F_menu_code'),
    )

    # 普通索引
    Index('index_t_menu_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    MENU_CODE = 'menu_code'  # 菜单代码
    MENU_NAME = 'menu_name'  # 菜单名称
    ICON = 'icon'  # 菜单图标
    SORT = 'sort'  # 排序位置，默认最后一个
    PARENT = 'parent'  # 父级菜单 0-否 1-是
    IS_LINK = 'is_link'  # 是否外链 0-否 1-是
    DELETED = 'deleted'  # 删除标记 0-否 1-是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'menu_code',
        'menu_name',
        'icon',
        'sort',
        'parent',
        'is_link',
        'deleted',
        'operator',
        'modify_time',
    ]

