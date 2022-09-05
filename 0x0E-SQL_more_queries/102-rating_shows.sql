-- A script that lists all shows from the DB by their rating
SELECT `tv_shows`.`title`, SUM(`tv_show_ratings`.`rate`) AS `rating`
FROM `tv_shows`
JOIN `tv_show_ratings`
ON `tv_shows`.`id` = `tv_show_ratings`.`show_id`
GROUP BY `tv_show_ratings`.`show_id`
ORDER BY `rating` DESC;