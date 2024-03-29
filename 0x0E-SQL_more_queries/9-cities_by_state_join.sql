-- ists all cities contained in the database hbtn_0d_usa
/*Each record should display: cities.id - cities.name - states.name
 Results must be sorted in ascending order by cities.id
 You can use only one SELECT statement
*/

SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s ON c.states_id = s.id
ORDER BY c.id;
