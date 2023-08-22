-- calculates the average temperature of a city
SELECT AVG(values) as avg_temp
FROM temperatures
ORDER BY city DESC;
