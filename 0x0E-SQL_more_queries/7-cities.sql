-- A script that creates the database hbtn_0d_usa and the table cities 
-- (in the database hbtn_0d_usa)

-- To create the Database - hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- To create the table 'cities' in the database 'hbtn_0d_usa'
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) 
    REFERENCES hbtn_0d_usa.state(id)),
    type = InnoDB;