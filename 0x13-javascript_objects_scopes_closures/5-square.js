#!/usr/bin/node
// creating a Subclass square that inherits from parent Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size >= 1) {
      this.width = size; this.height = size;
    }
  }
}
module.exports = Square;
