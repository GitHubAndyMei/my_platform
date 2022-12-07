CREATE USER 'momenta'@'127.0.0.1' IDENTIFIED BY 'momenta';
CREATE USER 'momenta'@'%' IDENTIFIED BY 'momenta';

GRANT ALL ON *.* TO 'momenta'@'127.0.0.1' WITH GRANT OPTION;
GRANT ALL ON *.* TO 'momenta'@'%' WITH GRANT OPTION;