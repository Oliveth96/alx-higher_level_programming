#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present

const request = require("request");

const options = {
  url: process.argv[2],
  headers: {
    "User-Agent": "request",
  },
};

function callback(error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let r = /18/;
    const movies = data["results"];
    let i = 0;
    let count = 0;
    for (const i in results) {
        for (const j in results[i].characters) {
          if (results[i].characters[j].endsWith('/18/')) {
            count++;
          }
        }
    }
    console.log(count);
  }
}

request(options, callback);
