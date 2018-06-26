-- Lists all the cities that can be found in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- states table contains only one record where name = California but the id can be different
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id;
