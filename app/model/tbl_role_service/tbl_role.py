
"""
table t_role data model.
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


class EnumTblRoleDeleted(enum.Enum):
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

class TblRole(Base):
    '''
    角色表
    '''
    # 表名
    __tablename__ = 't_role'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    role_code = Column(String(64), name='F_role_code', comment='角色代码', nullable=False, default='')
    role_name = Column(String(64), name='F_role_name', comment='角色名称', nullable=False, default='')
    deleted = Column(SmallInteger, name='F_deleted', comment='删除标记 enum:0,no,否#1,yes,是', nullable=False, default=0)
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_role_code', name='unique_index_t_role_role_code'),
    )

    # 普通索引
    Index('index_t_role_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    ROLE_CODE = 'role_code'  # 角色代码
    ROLE_NAME = 'role_name'  # 角色名称
    DELETED = 'deleted'  # 删除标记 enum:0,no,否#1,yes,是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'role_code',
        'role_name',
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