
# -*- coding: utf-8 -*-

class TblUserDto:
    '''
    用户表
    '''
    def __init__(self):
        self._id = None  # 唯一id
        self._id_u = 0
        self._id_in = [] # 唯一id
        self._id_in_u = 0
        self._id_like = None # 唯一id
        self._id_like_u = 0
        self._id_gte = None # 唯一id
        self._id_gte_u = 0
        self._id_lte = None # 唯一id
        self._id_lte_u = 0
        self._username = None  # 用户账号
        self._username_u = 0
        self._username_in = [] # 用户账号
        self._username_in_u = 0
        self._username_like = None # 用户账号
        self._username_like_u = 0
        self._username_gte = None # 用户账号
        self._username_gte_u = 0
        self._username_lte = None # 用户账号
        self._username_lte_u = 0
        self._password = None  # 用户账号
        self._password_u = 0
        self._password_in = [] # 用户账号
        self._password_in_u = 0
        self._password_like = None # 用户账号
        self._password_like_u = 0
        self._password_gte = None # 用户账号
        self._password_gte_u = 0
        self._password_lte = None # 用户账号
        self._password_lte_u = 0
        self._deleted = None  # 删除标记 enum:0,no,否#1,yes,是
        self._deleted_u = 0
        self._deleted_in = [] # 删除标记 enum:0,no,否#1,yes,是
        self._deleted_in_u = 0
        self._deleted_like = None # 删除标记 enum:0,no,否#1,yes,是
        self._deleted_like_u = 0
        self._deleted_gte = None # 删除标记 enum:0,no,否#1,yes,是
        self._deleted_gte_u = 0
        self._deleted_lte = None # 删除标记 enum:0,no,否#1,yes,是
        self._deleted_lte_u = 0
        self._operator = None  # 操作员
        self._operator_u = 0
        self._operator_in = [] # 操作员
        self._operator_in_u = 0
        self._operator_like = None # 操作员
        self._operator_like_u = 0
        self._operator_gte = None # 操作员
        self._operator_gte_u = 0
        self._operator_lte = None # 操作员
        self._operator_lte_u = 0
        self._create_time = None  # 创建时间戳 单位秒
        self._create_time_u = 0
        self._create_time_in = [] # 创建时间戳 单位秒
        self._create_time_in_u = 0
        self._create_time_like = None # 创建时间戳 单位秒
        self._create_time_like_u = 0
        self._create_time_gte = None # 创建时间戳 单位秒
        self._create_time_gte_u = 0
        self._create_time_lte = None # 创建时间戳 单位秒
        self._create_time_lte_u = 0
        self._modify_time = None  # 更新时间戳 单位秒
        self._modify_time_u = 0
        self._modify_time_in = [] # 更新时间戳 单位秒
        self._modify_time_in_u = 0
        self._modify_time_like = None # 更新时间戳 单位秒
        self._modify_time_like_u = 0
        self._modify_time_gte = None # 更新时间戳 单位秒
        self._modify_time_gte_u = 0
        self._modify_time_lte = None # 更新时间戳 单位秒
        self._modify_time_lte_u = 0

    def get_id(self):
        '''
        唯一id
        '''
        return self._id

    def get_id_in(self):
        '''
        唯一id
        '''
        return self._id_in

    def get_id_like(self):
        '''
        唯一id
        '''
        return self._id_like

    def get_id_gte(self):
        '''
        唯一id
        '''
        return self._id_gte

    def get_id_lte(self):
        '''
        唯一id
        '''
        return self._id_gte

    def set_id(self, value):
        '''
        唯一id
        '''
        self._id = value
        self._id_u = 1

    def set_id_in(self, value):
        '''
        唯一id
        '''
        self._id_in = value
        self._id_in_u = 1

    def set_id_like(self, value):
        '''
        唯一id
        '''
        self._id_like = value
        self._id_like_u = 1

    def set_id_gte(self, value):
        '''
        唯一id
        '''
        self._id_gte = value
        self._id_gte_u = 1

    def set_id_lte(self, value):
        '''
        唯一id
        '''
        self._id_lte = value
        self._id_lte_u = 1

    def is_set_id(self):
        '''
        唯一id
        '''
        return self._id_u == 1

    def is_set_id_in(self):
        '''
        唯一id
        '''
        return self._id_in_u == 1

    def is_set_id_like(self):
        '''
        唯一id
        '''
        return self._id_like_u == 1

    def is_set_id_gte(self):
        '''
        唯一id
        '''
        return self._id_gte_u == 1

    def is_set_id_lte(self):
        '''
        唯一id
        '''
        return self._id_lte_u == 1

    def get_username(self):
        '''
        用户账号
        '''
        return self._username

    def get_username_in(self):
        '''
        用户账号
        '''
        return self._username_in

    def get_username_like(self):
        '''
        用户账号
        '''
        return self._username_like

    def get_username_gte(self):
        '''
        用户账号
        '''
        return self._username_gte

    def get_username_lte(self):
        '''
        用户账号
        '''
        return self._username_gte

    def set_username(self, value):
        '''
        用户账号
        '''
        self._username = value
        self._username_u = 1

    def set_username_in(self, value):
        '''
        用户账号
        '''
        self._username_in = value
        self._username_in_u = 1

    def set_username_like(self, value):
        '''
        用户账号
        '''
        self._username_like = value
        self._username_like_u = 1

    def set_username_gte(self, value):
        '''
        用户账号
        '''
        self._username_gte = value
        self._username_gte_u = 1

    def set_username_lte(self, value):
        '''
        用户账号
        '''
        self._username_lte = value
        self._username_lte_u = 1

    def is_set_username(self):
        '''
        用户账号
        '''
        return self._username_u == 1

    def is_set_username_in(self):
        '''
        用户账号
        '''
        return self._username_in_u == 1

    def is_set_username_like(self):
        '''
        用户账号
        '''
        return self._username_like_u == 1

    def is_set_username_gte(self):
        '''
        用户账号
        '''
        return self._username_gte_u == 1

    def is_set_username_lte(self):
        '''
        用户账号
        '''
        return self._username_lte_u == 1

    def get_password(self):
        '''
        用户账号
        '''
        return self._password

    def get_password_in(self):
        '''
        用户账号
        '''
        return self._password_in

    def get_password_like(self):
        '''
        用户账号
        '''
        return self._password_like

    def get_password_gte(self):
        '''
        用户账号
        '''
        return self._password_gte

    def get_password_lte(self):
        '''
        用户账号
        '''
        return self._password_gte

    def set_password(self, value):
        '''
        用户账号
        '''
        self._password = value
        self._password_u = 1

    def set_password_in(self, value):
        '''
        用户账号
        '''
        self._password_in = value
        self._password_in_u = 1

    def set_password_like(self, value):
        '''
        用户账号
        '''
        self._password_like = value
        self._password_like_u = 1

    def set_password_gte(self, value):
        '''
        用户账号
        '''
        self._password_gte = value
        self._password_gte_u = 1

    def set_password_lte(self, value):
        '''
        用户账号
        '''
        self._password_lte = value
        self._password_lte_u = 1

    def is_set_password(self):
        '''
        用户账号
        '''
        return self._password_u == 1

    def is_set_password_in(self):
        '''
        用户账号
        '''
        return self._password_in_u == 1

    def is_set_password_like(self):
        '''
        用户账号
        '''
        return self._password_like_u == 1

    def is_set_password_gte(self):
        '''
        用户账号
        '''
        return self._password_gte_u == 1

    def is_set_password_lte(self):
        '''
        用户账号
        '''
        return self._password_lte_u == 1

    def get_deleted(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted

    def get_deleted_in(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_in

    def get_deleted_like(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_like

    def get_deleted_gte(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_gte

    def get_deleted_lte(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_gte

    def set_deleted(self, value):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        self._deleted = value
        self._deleted_u = 1

    def set_deleted_in(self, value):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        self._deleted_in = value
        self._deleted_in_u = 1

    def set_deleted_like(self, value):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        self._deleted_like = value
        self._deleted_like_u = 1

    def set_deleted_gte(self, value):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        self._deleted_gte = value
        self._deleted_gte_u = 1

    def set_deleted_lte(self, value):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        self._deleted_lte = value
        self._deleted_lte_u = 1

    def is_set_deleted(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_u == 1

    def is_set_deleted_in(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_in_u == 1

    def is_set_deleted_like(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_like_u == 1

    def is_set_deleted_gte(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_gte_u == 1

    def is_set_deleted_lte(self):
        '''
        删除标记 enum:0,no,否#1,yes,是
        '''
        return self._deleted_lte_u == 1

    def get_operator(self):
        '''
        操作员
        '''
        return self._operator

    def get_operator_in(self):
        '''
        操作员
        '''
        return self._operator_in

    def get_operator_like(self):
        '''
        操作员
        '''
        return self._operator_like

    def get_operator_gte(self):
        '''
        操作员
        '''
        return self._operator_gte

    def get_operator_lte(self):
        '''
        操作员
        '''
        return self._operator_gte

    def set_operator(self, value):
        '''
        操作员
        '''
        self._operator = value
        self._operator_u = 1

    def set_operator_in(self, value):
        '''
        操作员
        '''
        self._operator_in = value
        self._operator_in_u = 1

    def set_operator_like(self, value):
        '''
        操作员
        '''
        self._operator_like = value
        self._operator_like_u = 1

    def set_operator_gte(self, value):
        '''
        操作员
        '''
        self._operator_gte = value
        self._operator_gte_u = 1

    def set_operator_lte(self, value):
        '''
        操作员
        '''
        self._operator_lte = value
        self._operator_lte_u = 1

    def is_set_operator(self):
        '''
        操作员
        '''
        return self._operator_u == 1

    def is_set_operator_in(self):
        '''
        操作员
        '''
        return self._operator_in_u == 1

    def is_set_operator_like(self):
        '''
        操作员
        '''
        return self._operator_like_u == 1

    def is_set_operator_gte(self):
        '''
        操作员
        '''
        return self._operator_gte_u == 1

    def is_set_operator_lte(self):
        '''
        操作员
        '''
        return self._operator_lte_u == 1

    def get_create_time(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time

    def get_create_time_in(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_in

    def get_create_time_like(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_like

    def get_create_time_gte(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_gte

    def get_create_time_lte(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_gte

    def set_create_time(self, value):
        '''
        创建时间戳 单位秒
        '''
        self._create_time = value
        self._create_time_u = 1

    def set_create_time_in(self, value):
        '''
        创建时间戳 单位秒
        '''
        self._create_time_in = value
        self._create_time_in_u = 1

    def set_create_time_like(self, value):
        '''
        创建时间戳 单位秒
        '''
        self._create_time_like = value
        self._create_time_like_u = 1

    def set_create_time_gte(self, value):
        '''
        创建时间戳 单位秒
        '''
        self._create_time_gte = value
        self._create_time_gte_u = 1

    def set_create_time_lte(self, value):
        '''
        创建时间戳 单位秒
        '''
        self._create_time_lte = value
        self._create_time_lte_u = 1

    def is_set_create_time(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_u == 1

    def is_set_create_time_in(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_in_u == 1

    def is_set_create_time_like(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_like_u == 1

    def is_set_create_time_gte(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_gte_u == 1

    def is_set_create_time_lte(self):
        '''
        创建时间戳 单位秒
        '''
        return self._create_time_lte_u == 1

    def get_modify_time(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time

    def get_modify_time_in(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_in

    def get_modify_time_like(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_like

    def get_modify_time_gte(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_gte

    def get_modify_time_lte(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_gte

    def set_modify_time(self, value):
        '''
        更新时间戳 单位秒
        '''
        self._modify_time = value
        self._modify_time_u = 1

    def set_modify_time_in(self, value):
        '''
        更新时间戳 单位秒
        '''
        self._modify_time_in = value
        self._modify_time_in_u = 1

    def set_modify_time_like(self, value):
        '''
        更新时间戳 单位秒
        '''
        self._modify_time_like = value
        self._modify_time_like_u = 1

    def set_modify_time_gte(self, value):
        '''
        更新时间戳 单位秒
        '''
        self._modify_time_gte = value
        self._modify_time_gte_u = 1

    def set_modify_time_lte(self, value):
        '''
        更新时间戳 单位秒
        '''
        self._modify_time_lte = value
        self._modify_time_lte_u = 1

    def is_set_modify_time(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_u == 1

    def is_set_modify_time_in(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_in_u == 1

    def is_set_modify_time_like(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_like_u == 1

    def is_set_modify_time_gte(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_gte_u == 1

    def is_set_modify_time_lte(self):
        '''
        更新时间戳 单位秒
        '''
        return self._modify_time_lte_u == 1

