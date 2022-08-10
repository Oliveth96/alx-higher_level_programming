-- A script that lists all genres from the DB and 
-- displays the number of shows linked to each
SELECT x.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS x
     INNER JOIN  `tv_show_genres` AS y
     ON x.`id` = y.`genre_id`
GROUP BY x.`name`
ORDER BY `number_of_shows` DESC;