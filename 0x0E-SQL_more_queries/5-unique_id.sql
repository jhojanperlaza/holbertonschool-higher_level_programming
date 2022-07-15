-- script that creates the table unique_id on your MySQL server.
-- If the table force_name already exists, script not fail
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1,name VARCHAR(256) NOT NULL);
