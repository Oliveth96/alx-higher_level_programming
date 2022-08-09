-- use hbtn_0c_0 database
USE hbtn_0c_0;
-- A script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
ALTER DATABASE
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- To convert first_table table to UTF-8
ALTER TABLE `first_table`
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- To convert the name column of first_table to UTF-8
ALTER TABLE `first_table` CONVERT TO
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;