-- calculates the average temperature of a city
SELECT city, AVG(values) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY city DESC;
