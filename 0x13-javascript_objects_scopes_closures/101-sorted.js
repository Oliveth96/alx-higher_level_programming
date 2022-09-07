#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and
// computes a dictionary of user ids by occurrence

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map(function (e, index) {
  return e * index;
});
console.log(mappedList);
