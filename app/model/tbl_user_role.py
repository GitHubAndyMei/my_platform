
"""
table t_user_role data model.
"""

import enum
from app.model.base import Base
from sqlalchemy import Column, Integer, SmallInteger, BigInteger, String, JSON, Text, UniqueConstraint, Index,text


class EnumTblUserRoleIsAdmin(enum.Enum):
    IS_ADMIN_NORMAL_USER = '0'  # 普通用户
    IS_ADMIN_ADMIN = '1'  # 管理员用户

    @classmethod
    def get_desc(cls, enum_value: str):
        '''
        获取是否是管理员 值描述
        '''
        desc_dict = {
            '0': '普通用户',
            '1': '管理员用户',
        }

        return desc_dict.get(enum_value, '未知状态')

class EnumTblUserRoleDeleted(enum.Enum):
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

class TblUserRole(Base):
    '''
    用户角色关联表
    '''
    # 表名
    __tablename__ = 't_user_role'

    # 字段定义
    id = Column(Integer, name='F_id', comment='', primary_key=True, autoincrement=True)
    role_code = Column(String(64), name='F_role_code', comment='组织代码', nullable=False, default='')
    user_account = Column(String(64), name='F_user_account', comment='用户账号', nullable=False, default='')
    is_admin = Column(String(1), name='F_is_admin', comment='是否是管理员 enum:0,normal_user,普通用户|1,admin,管理员用户', nullable=False, default='')
    remark = Column(Text(1), name='F_remark', comment='备注', nullable=False, default=text(''))
    deleted = Column(String(1), name='F_deleted', comment='删除标记 enum:0,no,否#1,yes,是', nullable=False, default='0')
    operator = Column(String(32), name='F_operator', comment='操作员', nullable=False, default='')
    create_time = Column(BigInteger, name='F_create_time', comment='创建时间戳 单位秒', nullable=False, default=0)
    modify_time = Column(BigInteger, name='F_modify_time', comment='更新时间戳 单位秒', nullable=False, default=0)

    # 唯一索引
    __table_args__ = (
        UniqueConstraint('F_role_code', name='F_role_code'),
    )

    # 普通索引
    Index('index_t_org_role_modify_time', 'F_modify_time')  # 普通索引
    Index('index_t_user_role_modify_time', 'F_modify_time')  # 普通索引

    # 字段别名
    ID = 'id'  # 
    ROLE_CODE = 'role_code'  # 组织代码
    USER_ACCOUNT = 'user_account'  # 用户账号
    IS_ADMIN = 'is_admin'  # 是否是管理员 enum:0,normal_user,普通用户|1,admin,管理员用户
    REMARK = 'remark'  # 备注
    DELETED = 'deleted'  # 删除标记 enum:0,no,否#1,yes,是
    OPERATOR = 'operator'  # 操作员
    CREATE_TIME = 'create_time'  # 创建时间戳 单位秒
    MODIFY_TIME = 'modify_time'  # 更新时间戳 单位秒

    # 可更新的字段
    UP_COLUMNS = [
        'id',
        'role_code',
        'user_account',
        'is_admin',
        'remark',
        'deleted',
        'operator',
        'modify_time',
    ]

