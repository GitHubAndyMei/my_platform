#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_role"

mycmd="mysql -h$host -u$user_name -p$password -P$port --default-character-set=utf8mb4"
for i in `seq 1 $table_sum`;
do
table_index=`expr $i - 1`
table_name=${table_base_name}_$table_index
if [ $table_sum -eq 1 ];then
	table_name=$table_base_name
fi

$mycmd -e "drop table if exists $db.$table_name;"
sql="
create table $db.$table_name (
  F_id                  int(11)      NOT NULL AUTO_INCREMENT,
  F_role_code           varchar(64)  NOT NULL DEFAULT ''  COMMENT '角色代码',
  F_role_name           varchar(64)  NOT NULL DEFAULT ''  COMMENT '角色名称',
  F_is_admin            tinyint(1)   NOT NULL DEFAULT 0   COMMENT '是否是管理员 enum:0,no,否#1,yes,是',
  F_status              tinyint(1)   NOT NULL DEFAULT 1   COMMENT '角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用',
  F_deleted             tinyint(1)   NOT NULL DEFAULT 0   COMMENT '删除标记 enum:0,no,否#1,yes,是',
  F_operator            varchar(32)  NOT NULL DEFAULT ''  COMMENT '操作员',
  F_create_time         bigint(20)   NOT NULL DEFAULT '0' COMMENT '创建时间戳 单位秒',
  F_modify_time         bigint(20)   NOT NULL DEFAULT '0' COMMENT '更新时间戳 单位秒',
  PRIMARY KEY (F_id),
  UNIQUE KEY unique_index_${table_name}_role_code (F_role_code),
  INDEX index_${table_name}_modify_time (F_modify_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done