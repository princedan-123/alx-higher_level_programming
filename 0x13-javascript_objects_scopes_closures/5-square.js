#!/usr/bin/node
/* creating a subclass Square that inherits from the super class Rectangle */
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }
}
module.exports = Square;
