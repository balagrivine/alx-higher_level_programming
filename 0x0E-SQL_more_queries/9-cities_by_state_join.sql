-- lists all cities contained in the db hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

SELECT cities.id, cities.name, states.name 
FROM cities JOIN states on cities.state_id=states.id
ORDER BY cities.id ASC;
