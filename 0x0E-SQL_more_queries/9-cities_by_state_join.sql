-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
