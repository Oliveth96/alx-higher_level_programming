#!/usr/bin/node
//A script that reads and prints the contents of a file

const rf = require('rf');

rf.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
