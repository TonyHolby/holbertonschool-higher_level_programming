-- A script that creates the database hbtn_0d_1 and the user user_0d_1.
CREATE DATABASE IF NOT EXISTS hbtn_0d_1;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';
GRANT SELECT ON hbtn_0d_1.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
