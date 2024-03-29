#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and
// computes a dictionary of user ids by occurrence

const occurrencesByUser = require('./101-data').dict;
const usersByOccurrence = {};
let user;
let occurrence;
for (user in occurrencesByUser) {
  occurrence = occurrencesByUser[user];
  if (usersByOccurrence[occurrence] === undefined) {
    usersByOccurrence[occurrence] = [user];
  } else {
    usersByOccurrence[occurrence].push(user);
  }
}
console.log(usersByOccurrence);
