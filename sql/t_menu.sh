#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_menu"

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
  F_menu_code           varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '菜单代码',
  F_menu_name           varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '菜单名称',
  F_icon                varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '菜单图标',
  F_sort                int(11)                                    NOT NULL DEFAULT '999' COMMENT '排序位置，默认最后一个',
  F_parent              varchar(64)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '0' COMMENT '父级菜单 enum:0,no,否#1,yes,是',
  F_is_link             tinyint(1)   COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT 0   COMMENT '是否外链 enum:0,no,否#1,yes,是',
  F_deleted             tinyint(1)   COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT 0   COMMENT '删除标记 enum:0,no,否#1,yes,是',
  F_operator            varchar(32)  COLLATE utf8mb4_unicode_ci    NOT NULL DEFAULT '' COMMENT '操作员',
  F_create_time         bigint(20)                                 NOT NULL DEFAULT '0' COMMENT '创建时间戳 单位秒',
  F_modify_time         bigint(20)                                 NOT NULL DEFAULT '0' COMMENT '更新时间戳 单位秒',
  PRIMARY KEY (F_id) USING BTREE,
  UNIQUE KEY ${table_name}_F_menu_code (F_menu_code),
  INDEX index_${table_name}_modify_time (F_modify_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='菜单表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done