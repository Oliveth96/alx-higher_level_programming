#!/usr/bin/node
// A script that prints "" if the first argument can be converted to an intege

if (isNaN(process.argv[2])) {
    console.log('Not a number');
} else {
    console.log('Mu number: ' + parseInt(process.argv[2]));
}
