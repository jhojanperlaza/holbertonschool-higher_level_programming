-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
