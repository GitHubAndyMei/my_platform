# 					my Platform数据库设计
## 1.菜单表(t_menu)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_menu_code|varchar(64)||菜单代码||
| F_parent_menu_code|varchar(64)||父菜单代码||
| F_menu_name|varchar(64)||菜单名称||
| F_sort|int(11)||排序位置, 默认最后一个|999|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_menu_menu_code  索引字段: F_menu_code

普通索引:unique_index_t_menu_menu_code  索引字段: F_menu_code



## 2.权限表(t_permission)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_permission_code|varchar(64)||权限代码||
| F_permission_name|varchar(64)||权限名称||
| F_url|varchar(128)||路径地址||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_permission_permission_code  索引字段: F_permission_code

普通索引:unique_index_t_permission_permission_code  索引字段: F_permission_code



## 3.角色表(t_role)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||角色代码||
| F_role_name|varchar(64)||角色名称||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_role_role_code  索引字段: F_role_code

普通索引:unique_index_t_role_role_code  索引字段: F_role_code



## 4.角色菜单表(t_role_menu)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||角色代码||
| F_menu_code|varchar(64)||菜单代码||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_role_menu_role_code_menu_code  索引字段: F_role_code,F_menu_code

普通索引:unique_index_t_role_menu_role_code_menu_code  索引字段: F_role_code,F_menu_code



## 5.角色权限表(t_role_permission)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||角色代码||
| F_permission_code|varchar(64)||权限代码||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_role_permission_role_code_permission_code  索引字段: F_role_code,F_permission_code

普通索引:unique_index_t_role_permission_role_code_permission_code  索引字段: F_role_code,F_permission_code



## 6.用户表(t_user)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y|唯一id|None|
| F_user_account|varchar(64)||用户账号||
| F_username|varchar(64)||用户名称||
| F_password|varchar(64)||用户密码||
| F_desc|varchar(64)||用户描述||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(64)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_user_user_account  索引字段: F_user_account

唯一索引:unique_index_t_user_user_name  索引字段: F_username

普通索引:unique_index_t_user_user_name  索引字段: F_user_account

普通索引:unique_index_t_user_user_name  索引字段: F_username



## 7.用户角色表(t_user_role)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_user_account|varchar(64)||用户账号||
| F_role_code|varchar(64)||角色代码||
| F_deleted|varchar(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:unique_index_t_user_role_user_account_role_code  索引字段: F_user_account,F_role_code

普通索引:unique_index_t_user_role_user_account_role_code  索引字段: F_user_account,F_role_code



