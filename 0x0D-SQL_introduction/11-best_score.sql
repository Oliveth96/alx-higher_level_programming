-- A script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CHANGE `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;