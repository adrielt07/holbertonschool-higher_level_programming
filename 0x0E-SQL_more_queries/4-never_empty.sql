-- Creates the table id_not_null on your MySQL server
-- id: INT default 1 and name VARCHAR(256)
-- database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1,
name VARCHAR(256));
