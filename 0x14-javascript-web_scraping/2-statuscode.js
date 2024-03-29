#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');

request
    .get(process.argv[2])
    .on('response', function(response) {
        console.log('code:', response.statusCode);
    });
