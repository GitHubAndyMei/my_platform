#!/bin/bash
#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_user"

mycmd="mysql -h$host -u$user -p$password -P$port --default-character-set=utf8mb4"
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
    F_id                     int           AUTO_INCREMENT             COMMENT '唯一id',
    F_username               varchar(64)   NOT NULL DEFAULT ''        COMMENT '用户账号',
    F_password               varchar(64)   NOT NULL DEFAULT ''        COMMENT '用户账号',
    F_deleted                tinyint       NOT NULL DEFAULT 0         COMMENT '删除标记 enum:0,no,否#1,yes,是',
    F_operator               varchar(64)   NOT NULL DEFAULT ''        COMMENT '操作员',
    F_create_time            bigint        NOT NULL DEFAULT 0         COMMENT '创建时间戳 单位秒',
    F_modify_time            bigint        NOT NULL DEFAULT 0         COMMENT '更新时间戳 单位秒',
    PRIMARY KEY (F_id),
    UNIQUE KEY (F_username),
    INDEX index_${table_name}_modify_time (F_modify_time)
)ENGINE=InnoDB COMMENT '用户表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done