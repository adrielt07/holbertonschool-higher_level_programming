-- Creates the Database 'hbtn_0d_usa' and table 'states' on your MySQL server
-- State Description
-- id: INT auto generated, can't be null and Unique
-- name: VARCHAR(256)
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL,
name VARCHAR(256) NOT NULL);
