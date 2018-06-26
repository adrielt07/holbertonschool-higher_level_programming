-- Creates the table unique_id on your MySQL server
-- id: INT default 1 and Unique, name VARCHAR(256)
-- database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
