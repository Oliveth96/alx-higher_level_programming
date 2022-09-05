#!/usr/bin/node
// A script that prints x times “C is fun”

const progLanguages = 'C is fun';

if (isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
        console.log(progLanguages);
    }
}
