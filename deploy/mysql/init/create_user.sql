CREATE USER 'my_platform'@'127.0.0.1' IDENTIFIED BY 'my_platform';
CREATE USER 'my_platform'@'%' IDENTIFIED BY 'my_platform';

GRANT ALL ON *.* TO 'my_platform'@'127.0.0.1' WITH GRANT OPTION;
GRANT ALL ON *.* TO 'my_platform'@'%' WITH GRANT OPTION;