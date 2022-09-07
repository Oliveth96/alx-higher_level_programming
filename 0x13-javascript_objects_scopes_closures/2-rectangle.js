#!/usr/bin/node
// A a class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
