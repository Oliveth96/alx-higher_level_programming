-- A script that creates the MySQL server user user_0d_1
-- To create the User
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- To grant the User all provileges
GRANT ALL PRIVILEGES 
ON *.* TO 'user_0d_1'@'localhost';