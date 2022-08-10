-- A script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa)
-- To create the Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- To create the Table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE AUTO GENERATED NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);