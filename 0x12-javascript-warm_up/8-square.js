#!/usr/bin/node
// A script that prints a square

const b = process.argv[2];

if (isNaN(b)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < parseInt(b); i++) {
        console.log('X'.repeat(parseInt(b)));
    }
}
