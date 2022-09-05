#!/usr/bin/node
// A script tat computes and prints a factorial

const x = process.argv[2];

function computeFactorial (n) {
    if ((isNaN(n)) || (n === 1)) {
        return 1;
    } else {
        return n * computeFactorial(n - 1);
    }
}

console.log(computeFactorial(parseInt(x)));
