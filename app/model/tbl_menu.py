
"""
table t_menu data model.
"""

import enum
import hashlib
from app.model.base import Base
from sqlalchemy import (
    Column,
    Integer,
    Float,
    SmallInteger,
    BigInteger,
    String,
    JSON,
    Text,
    UniqueConstraint,
    Index,
    text)


class EnumTblMenuDeleted(enum.Enum):
    DELETED_NO = '0'  # 否
    DELETED_YES = '1'  # 是

    @classmethod
    def get_desc(cls, enum_value: str):
        '''
        获取删除标记 值描述
        '''
        desc_dict = {
            '0': '否',
            '1': '是',
        }

        return desc_dict.get(enum_value, '未知状态')

class TblMenu(Base):
    '''
    菜单表
    '''
    # 表名
    __tablename__ = 't_menu'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    menu_code = Column(String(64), name='F_menu_code', comment='菜单代码', nullable=False, default='')
    parent_menu_code = Column(String(64), name='F_parent_menu_code', comment='父菜单代码', nullable=False, default='')
    menu_name = Column(String(64), name='F_menu_name', comment='菜单名称', nullable=False, default='')
    sort = Column(Integer, name='F_sort', comment='排序位置, 默认最后一个', nullable=False, default=999)
    deleted = Column(SmallInteger, name='F_deleted', comment='删除标记 enum:0,no,否#1,yes,是', nullable=False, default=0)
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_menu_code', name='unique_index_t_menu_menu_code'),
    )

    # 普通索引
    Index('index_t_menu_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    MENU_CODE = 'menu_code'  # 菜单代码
    PARENT_MENU_CODE = 'parent_menu_code'  # 父菜单代码
    MENU_NAME = 'menu_name'  # 菜单名称
    SORT = 'sort'  # 排序位置, 默认最后一个
    DELETED = 'deleted'  # 删除标记 enum:0,no,否#1,yes,是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'menu_code',
        'parent_menu_code',
        'menu_name',
        'sort',
        'deleted',
        'operator',
        'modify_time',
    ]
    def to_json(self):
        value_json = {}
        for column in self.__table__.columns:
            column.name = column.name.replace("F_", "")
            value_json[column.name] = getattr(self, column.name)

        return value_json


    def generate_code(self):
        return self.__tablename__ + hashlib.md5().hexdigest()



w