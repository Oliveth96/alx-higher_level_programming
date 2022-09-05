#!/usr/bin/node
// A script that prints the addition of 2 integers

function add (a, b) {
    return a + b;
}

const x = process.argv[2];
const y = process.argv[3];
console.log(add(parseInt(x + y)));
