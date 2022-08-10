0x0E. SQL - More queries


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION


FILES
0-privileges.sql; Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server


1-create_user.sql; Write a script that creates the MySQL server user user_0d_1.


2-create_read_user.sql; Write a script that creates the database hbtn_0d_2 and the user user_0d_2.


3-force_name.sql; Write a script that creates the table force_name on your MySQL server.


4-never_empty.sql; Write a script that creates the table id_not_null on your MySQL server.


5-unique_id.sql; Write a script that creates the table unique_id on your MySQL server.


6-states.sql; Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.



7-cities.sql; Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.


8-cities_of_california_subquery.sql; Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.



9-cities_by_state_join.sql; Write a script that lists all cities contained in the database hbtn_0d_usa.

Each record should display: cities.id - cities.name - states.name
Results must be sorted in ascending order by cities.id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command



10-genre_id_by_show.sql; Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.



11-genre_id_all_shows.sql; Write a script that lists all shows contained in the database hbtn_0d_tvshows.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
If a show doesn’t have a genre, display NULL
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command


12-no_genre.sql; Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command



13-count_shows_by_genre.sql; Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

Each record should display: <TV Show genre> - <Number of shows linked to this genre>
First column must be called genre
Second column must be called number_of_shows
Don’t display a genre that doesn’t have any shows linked
Results must be sorted in descending order by the number of shows linked
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command


14-my_genres.sql; Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.


15-comedy_only.sql; Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

The tv_genres table contains only one record where name = Comedy (but the id can be different)
Each record should display: tv_shows.title
Results must be sorted in ascending order by the show title
You can use only one SELECT statement


16-shows_by_genre.sql; Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

If a show doesn’t have a genre, display NULL in the genre column
Each record should display: tv_shows.title - tv_genres.name
Results must be sorted in ascending order by the show title and genre name
You can use only one SELECT statement


100-not_my_genres.sql; Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

The tv_shows table contains only one record where title = Dexter (but the id can be different)
Each record should display: tv_genres.name
Results must be sorted in ascending order by the genre name
You can use a maximum of two SELECT statement



101-not_a_comedy.sql; Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

The tv_genres table contains only one record where name = Comedy (but the id can be different)
Each record should display: tv_shows.title
Results must be sorted in ascending order by the show title
You can use a maximum of two SELECT statement


102-rating_shows.sql; rite a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

Each record should display: tv_shows.title - rating sum
Results must be sorted in descending order by the rating
You can use only one SELECT statement



103-rating_genres.sql; Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

Each record should display: tv_genres.name - rating sum
Results must be sorted in descending order by their rating
You can use only one SELECT statement