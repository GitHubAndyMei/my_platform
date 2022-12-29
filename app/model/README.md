# 					Sanity CT Platform数据库设计
## 1.用户表(t_user)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int|Y|唯一id|None|
| F_username|varchar(64)||用户账号||
| F_password|varchar(64)||用户密码||
| F_deleted|tinyint||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(64)||操作员||
| F_create_time|bigint||创建时间戳 单位秒|0|
| F_modify_time|bigint||更新时间戳 单位秒|0|


唯一索引:unique_index_t_user_username  索引字段: F_username

普通索引:unique_index_t_user_username  索引字段: F_username



