-- Joins two related tables together within hbtn_0d_usa database
SELECT cities.id, cities.name, states.name
	FROM cities INNER JOIN states ON cities.id = states.id
	ORDER BY cities.id ASC;
