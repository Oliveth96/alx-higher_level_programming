<h1>0x15. JavaScript - Web jQuery</h1>


<h3> RESOURCES </h3>

<p> Read or watch:</p>

<span>[what is JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)</span><br>
<span>[Selectors](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)</span><br>
<span>[Get and Set contents](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)</span><br>
<span> [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)</span><br>
<span>[Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)</span><br>
<span>[API](https://oscarotero.com/jquery/)</span><br>
<span>[Introduction to AJAX](https://jquery-tutorial.net/ajax/introduction/)</span><br>
<span>[GET & POST REQUEST](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)</span><br>
<span>[JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)</span><br>
<span>[What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)</span><br>
<span>[JQuery](https://jquery.com/)</span><br>
<span>[JQuery API](https://api.jquery.com/)</span><br>
<span>[JQuery AJAX](https://learn.jquery.com/ajax/)</span><br>

<br>
<h6>MORE INFO</h6>
<p>Import JQuery</p>
<code>
    <head>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    </head>
</code>

<br>
<h3>TASKS</h3>

| TASKS | FILES | DESCRIPTION |
| ----- | ----- | ----------- |
| 0. No JQuery | [0-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/0-script.js)| <p>Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):</p><li>You must use document.querySelector to select the HTML tag</li><li>You can’t use the JQuery API</li>|
| 1. With JQuery | [1-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/1-script.js) | <p>Write a JavaScript script that updates the text color of the header element to red (#FF0000):</p><li>You must use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 2. Click and turn red |[2-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/2-script.js)| <p>Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag DIV#red_header:</p><li>You must use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 3. Add `.red` class |[3-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/3-script.js)| <p>Write a JavaScript script that adds the class red to the header element when the user clicks on the tag DIV#red_header</p><li>You must use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 4. Toggle classes |[4-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/4-script.js)| <p>Write a JavaScript script that toggles the class of the header element when the user clicks on the tag DIV#toggle_header:</p><li>The header element must always have one class: red or green, never both in the same time and never empty.</li><li>If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.</li><li>You must use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 5. List of elements | [5-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/5-script.js)| <p>Write a JavaScript script that adds a 'li' element to a list when the user clicks on the tag DIV#add_item:</p><li>The new element must be: "li-Item-li"</li><li>The new element must be added to UL.my_list</li><li>You can’t use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 6. Change the text| [6-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/6-script.js)| <p>Write a JavaScript script that updates the text of the header element to New Header!!! when the user clicks on DIV#update_header</p><li>You can’t use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 7. Star wars character |[7-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/7-script.js)| <p>Write a JavaScript script that fetches the character name from this [URL:] (https://swapi-api.hbtn.io/api/people/5/?format=json)</p><li>The name must be displayed in the HTML tag DIV#character</li><li>You can’t use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 8. Star Wars movies |[8-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/8-script.js)| <p>Write a JavaScript script that fetches the character title from this [URL:] (https://swapi-api.hbtn.io/api/films/?format=json)</p><li>All movie titles must be list in the HTML tag UL#list_movies</li><li>You can’t use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li> |
| 9. Say Hello!| [9-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/9-script.js)| <p>Write a JavaScript script that fetches [from] (https://fourtonfish.com/hellosalut/?lang=fr )and displays the value of hello from that fetch in the HTML tag DIV#hello.</p><li>The translation of “hello” must be displayed in the HTML tag DIV#hello</li><li>You can’t use document.querySelector to select the HTML tag</li><li>You must use the JQuery API</li><li>Your script must work when it is imported from the head tag</li> |
| 10. No jQuery - document loaded |[](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/)|<p>Write a JavaScript script that updates the text color of the header element to red (#FF0000):</p><li>You must use document.querySelector to select the HTML tag</li><li>You can’t use the jQuery API</li><li>Note: Your script must be imported from the head tag, not at the end of the HTML</li> |
| 11. List, add, remove|[101-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/101-script.js)| <p>Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:</p><li>The new element must be: li-Item-li</li><li>The new element must be added to UL.my_lis</li><li>When the user clicks on DIV#add_item: a new element is added to the list</li><li>When the user clicks on DIV#remove_item: the last element is removed from the list</li><li>You can't use document.querySelector to select the HTML tag</li><li>You can’t use the jQuery API</li> |
| 12. Say hello to everybody! |[102-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/102-script.js)| <p>Write a JavaScript script that fetches and prints how to say “Hello” depending on the language</p><li>You should use this [API service]( https://www.fourtonfish.com/hellosalut/hello/)</li><li>The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)</li><li>The translation must be fetched when the user clicks on INPUT#btn_translate</li><li>The translation of “Hello” must be displayed in the HTML tag DIV#hello</li><li>You can't use document.querySelector to select the HTML tag</li><li>You must use the jQuery API</li><li> You script must work when imported from the head tag</li> |
| 13. And press ENTER |[103-script.js](https://github.com/Oliveth96/alx-higher_level_programming/0x15-javascript-web_jquery/103-script.js)| <p>Write a JavaScript script that fetches and prints how to say “Hello” depending on the language</p><li>You should use this [API service](https://www.fourtonfish.com/hellosalut/hello/)</li><li>The language code will be the value entered in the tag INPUT#language_code eg: es, fr, en etc.</li><li>The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code</li><li>The translation of “Hello” must be displayed in the HTML tag DIV#hello</li><li>You can't use document.querySelector to select the HTML tag</li><li>You can’t use the jQuery API</li><li> You script must work when imported from the head tag</li> |

<br>

<h4>AUTHOR</h4>

[Oliveth Ndubuka](https://github.com/Oliveth96)