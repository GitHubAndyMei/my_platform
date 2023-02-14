# 					my Platform数据库设计
## 1.菜单表(t_menu)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_menu_code|varchar(64)||菜单代码||
| F_menu_name|varchar(64)||菜单名称||
| F_icon|varchar(64)||菜单图标||
| F_sort|int(11)||排序位置，默认最后一个|999|
| F_parent|varchar(64)||父级菜单 enum:0,no,否#1,yes,是|0|
| F_is_link|tinyint(1)||是否外链 enum:0,no,否#1,yes,是|0|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_menu_F_menu_code  索引字段: F_menu_code

普通索引:t_menu_F_menu_code  索引字段: F_menu_code



## 2.权限表(t_permission)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_permission_code|varchar(64)||权限代码||
| F_permission_name|varchar(64)||权限名称||
| F_parent_per_code|varchar(64)||父权限代码||
| F_url|varchar(128)||路径地址||
| F_sort|int(11)||排序位置，默认最后一个|999|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_permission_F_permission_code  索引字段: F_permission_code

普通索引:t_permission_F_permission_code  索引字段: F_permission_code



## 3.角色表(t_role)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||组织代码||
| F_role_name|varchar(64)||角色名||
| F_is_admin|tinyint(1)||是否是管理员 enum:0,normal_user,普通用户#1,admin,管理员用户|0|
| F_status|tinyint(1)||角色状态 enum:0,normal,正常#1,ensure,待审核#2,stop,禁用|0|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_role_F_role_code  索引字段: F_role_code

普通索引:t_role_F_role_code  索引字段: F_role_code



## 4.角色权限表(t_role_menu)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||角色代码||
| F_menu_code|varchar(64)||菜单代码||
| F_is_show|tinyint(1)||路径是否展示 enum:0,display,展示路径#1,not_display,不展示路径|0|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_role_menu_F_role_code_idx  索引字段: F_role_code

普通索引:t_role_menu_F_role_code_idx  索引字段: F_role_code



## 5.角色权限表(t_role_permission)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_role_code|varchar(64)||角色代码||
| F_permission_code|varchar(64)||权限代码||
| F_is_show|tinyint(1)||路径是否展示 enum:0,display,展示路径#1,not_display,不展示路径|0|
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_role_permission_F_role_code  索引字段: F_role_code

普通索引:t_role_permission_F_role_code  索引字段: F_role_code



## 6.用户表(t_user)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y|唯一id|None|
| F_username|varchar(64)||用户名称||
| F_user_account|varchar(64)||用户账号||
| F_password|varchar(64)||用户密码||
| F_deleted|tinyint(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(64)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_user_F_user_account  索引字段: F_user_account

普通索引:t_user_F_user_account  索引字段: F_user_account



## 7.用户角色关联表(t_user_role)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int(11)|Y||None|
| F_user_account|varchar(64)||用户账号||
| F_role_code|varchar(64)||组织代码||
| F_is_admin|varchar(1)||是否是管理员 enum:0,normal_user,普通用户#1,admin,管理员用户||
| F_remark|text||备注|None|
| F_deleted|varchar(1)||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(32)||操作员||
| F_create_time|bigint(20)||创建时间戳 单位秒|0|
| F_modify_time|bigint(20)||更新时间戳 单位秒|0|


唯一索引:t_user_role_F_role_code  索引字段: F_role_code

普通索引:t_user_role_F_role_code  索引字段: F_role_code



