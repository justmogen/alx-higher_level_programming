-- lists all the cities of California that can be found in the database hbtn_0d_usa
/* states table contains only one record where name = California
	Results must be sorted in ascending order by cities.id
*/
SELECT `id`, `name`
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'

ORDER BY `id` ASC; --ASC is by default even if we not initialize it
