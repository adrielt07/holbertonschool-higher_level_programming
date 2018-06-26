-- Creates the Database 'hbtn_0d_usa' and table 'cities' on your MySQL server
-- Cities Description
-- id: INT auto generated, can't be null and Primary Key
-- state_id: INT, can't be null, Foreign key from 'states' table
-- name: VARCHAR(256) can't be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
