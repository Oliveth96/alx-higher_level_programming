-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa)
-- To create the Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- To create the Table
CREATE TABLE IF NOT EXISTS states (
    PRIMARY KEY(id),
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);