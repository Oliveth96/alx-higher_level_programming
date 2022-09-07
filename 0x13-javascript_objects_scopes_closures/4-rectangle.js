#!/usr/bin/node
// Similar comments as in ./3-rectangle.js
// An instance method called rotate() that exchanges the width and the height of the rectangle
// An instance method called double() that multiples the width and the height of the rectangle by 2

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

  rotate () {
    this.width ^= this.height;
    this.height ^= this.width;
    this.width ^= this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
