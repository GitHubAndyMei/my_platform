# 					Sanity CT Platform数据库设计
## 1.用户表(t_user)


| 代码 | 数据类型 | 主键 | 备注 | 默认值 |
| - | - | - | - | - |
| F_id|int|Y|唯一id|None|
| F_name|varchar(64)||用户姓名||
| F_age|tinyint||权限代码|0|
| F_deleted|tinyint||删除标记 enum:0,no,否#1,yes,是|0|
| F_operator|varchar(64)||操作员||
| F_create_time|bigint||创建时间戳 单位秒|0|
| F_modify_time|bigint||更新时间戳 单位秒|0|


唯一索引:  F_id

唯一索引:  F_name

普通索引:  F_modify_time



