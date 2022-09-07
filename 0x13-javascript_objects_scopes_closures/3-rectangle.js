#!/usr/bin/node
// A a class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
