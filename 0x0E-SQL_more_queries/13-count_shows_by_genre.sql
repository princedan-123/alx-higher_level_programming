-- joins <TV Show genre and Number of shows linked to this genre
SELECT gen.name, show.show_id
FROM tv_genres gen
INNER JOIN  tv_shows_genres show
ON show.show_id = gen.id
GROUP BY name
HAVING(COUNT(show.show_id) > 0)
ORDER BY show.show_id DESC;
