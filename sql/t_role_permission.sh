#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_role_permission"

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
  F_id                  int(11)                                   NOT NULL AUTO_INCREMENT,
  F_role_code           varchar(64)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '角色代码',
  F_permission_code     varchar(64)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '权限代码',
  F_display_url         varchar(1)    COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '路径是否展示 enum:0,display,展示路径|1,not_display,不展示路径',
  F_deleted             varchar(1)    COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT '0' COMMENT '删除标记 0-否 1-是',
  F_operator            varchar(32)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '操作员',
  F_create_time         bigint(20)                                NOT NULL DEFAULT '0' COMMENT '创建时间戳 单位秒',
  F_modify_time         bigint(20)                                NOT NULL DEFAULT '0' COMMENT '更新时间戳 单位秒',
  PRIMARY KEY (F_id) USING BTREE,
  UNIQUE KEY F_org_code (F_org_code,F_role_code) USING BTREE,
  KEY index_t_org_role_modify_time (F_modify_time) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色权限表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done