#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_permission"

mycmd="mysql -h$host -u$username -p$password -P$port --default-character-set=utf8mb4"
for i in seq 1 $table_sum;
do
table_index=expr $i - 1
table_name=${table_base_name}_$table_index
if [ $table_sum -eq 1 ];then
	table_name=$table_base_name
fi

$mycmd -e "drop table if exists $db.$table_name;"
sql="
create table $db.$table_name (
  F_id                  int(11)                                    NOT NULL AUTO_INCREMENT,
  F_permission_code     varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '权限代码',
  F_permission_name     varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '权限名称',
  F_parent_per_code     varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '父权限代码',
  F_url                 varchar(128) COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '路径地址',
  F_sort                int(11)                                    NOT NULL DEFAULT '999' COMMENT '排序位置，默认最后一个',
  F_deleted             varchar(1)   COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '0' COMMENT '删除标记 0-否 1-是',
  F_operator            varchar(32)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '操作员',
  F_create_time         bigint(20)                                 NOT NULL DEFAULT '0' COMMENT '创建时间戳 单位秒',
  F_modify_time         bigint(20)                                 NOT NULL DEFAULT '0' COMMENT '更新时间戳 单位秒',
  PRIMARY KEY (F_id) USING BTREE,
  UNIQUE KEY F_app_code (F_app_code,F_permission_code) USING BTREE,
  INDEX index_${table_name}_modify_time (F_modify_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='权限表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done