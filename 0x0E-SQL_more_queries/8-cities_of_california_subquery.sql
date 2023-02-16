-- lists all the cities of California that can be found in the database hbtn_0d_usa
/* states table contains only one record where name = California
	Results must be sorted in ascending order by cities.id
*/
SELECT cities*.
FROM cities, states
WHERE cities.`state_id` IN (
	SELECT `id`
	FROM `states`
	WHERE `name` = 'California'
)
ORDER BY cities.`id`; --ASC is by default even if we not initialize it
