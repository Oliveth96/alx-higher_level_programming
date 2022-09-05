#!/usr/bin/node
// A script that prints "" if the first argument can be converted to an intege

if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(process.argv[2]));
  }
