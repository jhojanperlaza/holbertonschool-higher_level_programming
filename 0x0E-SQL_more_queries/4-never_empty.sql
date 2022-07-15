-- script that creates the table force_name on your MySQL server.
-- If the table force_name already exists, script not fail
CREATE TABLE IF NOT EXISTS id_not_null(id INT SET DEFAULT 1,name VARCHAR(256) NOT NULL);
