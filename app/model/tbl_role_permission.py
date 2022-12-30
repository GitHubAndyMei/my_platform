
"""
table t_role_permission data model.
"""

import enum
from app.model.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text, UniqueConstraint, Index,text


class EnumTblRolePermissionDisplayUrl(enum.Enum):
    DISPLAY_URL_DISPLAY = '0'  # 展示路径
    DISPLAY_URL_NOT_DISPLAY = '1'  # 不展示路径

    @classmethod
    def get_desc(cls, enum_value: str):
        '''
        获取路径是否展示 值描述
        '''
        desc_dict = {
            '0': '展示路径',
            '1': '不展示路径',
        }

        return desc_dict.get(enum_value, '未知状态')

class TblRolePermission(Base):
    '''
    角色权限表
    '''
    # 表名
    __tablename__ = 't_role_permission'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    role_code = Column(String(64), name='F_role_code', comment='角色代码', nullable=False, default='')
    permission_code = Column(String(64), name='F_permission_code', comment='权限代码', nullable=False, default='')
    display_url = Column(String(1), name='F_display_url', comment='路径是否展示 enum:0,display,展示路径|1,not_display,不展示路径', nullable=False, default='')
    deleted = Column(String(1), name='F_deleted', comment='删除标记 0-否 1-是', nullable=False, default='0')
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_role_code', name='F_role_code'),
    )

    # 普通索引
    Index('index_t_role_permission_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    ROLE_CODE = 'role_code'  # 角色代码
    PERMISSION_CODE = 'permission_code'  # 权限代码
    DISPLAY_URL = 'display_url'  # 路径是否展示 enum:0,display,展示路径|1,not_display,不展示路径
    DELETED = 'deleted'  # 删除标记 0-否 1-是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'role_code',
        'permission_code',
        'display_url',
        'deleted',
        'operator',
        'modify_time',
    ]

