-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa.
USE hbtn_0d_usa;
SET @state_id = SELECT id FROM states WHERE name = 'California' LIMIT 1;
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;
