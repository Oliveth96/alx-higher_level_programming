<h1>0x14. JavaScript - Web scraping</h1>

<h6></h6>
RESOURCES

[Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)<br>[Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)<br>[request module](https://github.com/request/request)<br>[The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)

<br>

| TASKS | FILES | DESCRIPTION |
| ----- | ----- | ----------- |
| 0. Readme |[0-readme.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/0-readme.js)|<p>Write a script that reads and prints the content of a file.</p><li>The first argument is the file path</li><li>The content of the file must be read in utf-8</li><li>If an error occurred during the reading, print the error object</li>|
| 1. Write me |[1-writeme.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/1-writeme.js)| <p>Write a script that writes a string to a file.</p><li>The first argument is the file path</li><li>The second argument is the string to write</li><li>If an error occurred during while writing, print the error object</li>|
| 2. Status code |[2-statuscode.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/2-statuscode.js)| <p>Write a script that display the status code of a GET request.</p><li>The first argument is the URL to request (GET)</li><li>The status code must be printed like this: code: status code</li><li>You must use the module request</li>|
| 3. Star wars movie title |[3-starwars_title.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/3-starwars_title.js)|<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p><li>The first argument is the movie ID</li><li>You must use the Star wars API with the [endpoint](https://swapi-api.hbtn.io/api/films/:id)</li><li>You must use the module request</li>|
| 4. Star wars Wedge Antilles |[4-starwars_count.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/4-starwars_count.js)|<p>Write a script that prints the number of movies where the character “Wedge Antilles” is present.</p><li>The first argument is the API URL of the [Star wars API] (https://swapi-api.hbtn.io/api/films/)</li><li>Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the AP</li><li>You must use the module request</li>|
| 5. Loripsum |[5-request_store.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/5-request_store.js)| <p>Write a script that gets the contents of a webpage and stores it in a file.</p><li>The first argument is the URL to request</li><li>The second argument the file path to store the body response</li><li>The file must be UTF-8 encoded</li><li>You must use the module request</li>|
| 6. How many completed? |[6-completed_tasks.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/6-completed_tasks.js)|<p>Write a script that computes the number of tasks completed by user id.</p><li>The first argument is the [API URL](https://jsonplaceholder.typicode.com/todos)</li><li>Only print users with completed task</li><li>You must use the module request</li>|
| 7. Who was playing in this movie? |[100-starwars_characters.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/100-starwars_characters.js)| <p>Write a script that prints all characters of a Star Wars movie:</p><li>The first argument is the Movie ID - example: 3 = “Return of the Jedi”</li><li>Display one character name by line</li><li>You must use the [Star wars API](https://swapi-api.hbtn.io/)</li><li>You must use the module request</li>|
| 8. Right order |[101-starwars_characters.js](https://github.com/Oliveth96/alx-higher_level_programming/0x14-javascript-web_scraping/101-starwars_characters.js)| <p>Write a script that prints all characters of a Star Wars movie:</p><li>The first argument is the Movie ID - example: 3 = “Return of the Jedi”</li><li>Display one character name by line in the same order of the list “characters” in the /films/ response</li><li>You must use the [Star wars API](https://swapi-api.hbtn.io/)</li><li>You must use the module request</li>|


AUTHOR
<br>
[Oliveth Ndubuka](https://github.com/Oliveth96)