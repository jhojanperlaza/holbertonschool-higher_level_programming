-- script that creates the table unique_id on your MySQL server.
-- If the table force_name already exists, script not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(256) NOT NULL);
