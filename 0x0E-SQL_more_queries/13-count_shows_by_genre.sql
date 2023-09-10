-- joins <TV Show genre and Number of shows linked to this genre
SELECT gen.name AS genre, COUNT(show.show_id) As number_of_shows
FROM tv_genres gen
INNER JOIN  tv_shows_genres show
ON show.genre_id = gen.id
GROUP BY gen.name
HAVING
COUNT(show.show_id) > 0
ORDER BY number_of_shows DESC;
