-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.title = tv_show_genres.genre_id;
