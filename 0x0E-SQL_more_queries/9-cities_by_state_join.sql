-- lists all cities contained in the db hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

SELECT id, name 
FROM cities INNER JOIN states
ORDER BY id ASC;
