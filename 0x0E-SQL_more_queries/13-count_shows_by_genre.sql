-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_genres.name "genre", COUNT(tv_show_genres.genre_id) "number_of_shows"
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id ORDER BY number_of_shows DESC;
