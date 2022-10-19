#!/usr/bin/node
// A script that prints the title of a Star Wars movie where
// the episode number matches a given integer

const request = require('request');

const movieApi = {
    url: 'https://swapi-api.hbtn.io/api/films' + process.argv[2],
    headers: {
        'User-Agent': 'request'
    }
};

function callback (error, response, body) {
    if (!error && response.statusCode === 200) {
        const info = JSON.parse(body);
        console.log(info['title']);
    }
}


request(movieApi, callback);