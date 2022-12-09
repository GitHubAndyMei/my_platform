
"""
table t_user data model.
"""

import enum
from models.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text

class EnumTblUserDeleted(enum.Enum):
    DELETED_NO = 0 # 否
    DELETED_YES = 1 # 是

    @classmethod
    def get_desc(cls, enum_value: int):
        '''
        获取删除标记 值描述
        '''
        desc_dict = {
            0:'否',
            1:'是',
        }

        return desc_dict.get(enum_value, '未知状态')

class TblUser(Base):
    '''
    用户表
    '''
    __tablename__ = 't_user'

    id = Column(Integer, name='F_id', comment='唯一id', primary_key=True, autoincrement=True)
    name = Column(String(64), name='F_name', comment='用户姓名', nullable=False, default='')
    age = Column(SmallInteger, name='F_age', comment='权限代码', nullable=False, default=0)
    deleted = Column(SmallInteger, name='F_deleted', comment='删除标记 enum:0,no,否#1,yes,是', nullable=False, default=0)
    operator = Column(String(64), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    ID = 'id' # 唯一id 字段别名
    NAME = 'name' # 用户姓名 字段别名
    AGE = 'age' # 权限代码 字段别名
    DELETED = 'deleted' # 删除标记 enum:0,no,否#1,yes,是 字段别名
    OPERATOR = 'operator' # 操作员 字段别名
    CREATE_TIME = 'create_time' # 创建时间戳 单位秒 字段别名
    MODIFY_TIME = 'modify_time' # 更新时间戳 单位秒 字段别名

    # 所有可更新的字段
    UP_COLUMNS = [
        'name',
        'age',
        'deleted',
        'operator',
        'modify_time',
    ]