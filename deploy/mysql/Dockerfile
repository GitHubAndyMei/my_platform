FROM mysql:8.0
COPY my.cnf               /etc/mysql/conf.d/my.cnf
COPY init/create_user.sql /docker-entrypoint-initdb.d/create_user.sql