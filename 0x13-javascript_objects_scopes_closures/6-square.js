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

  charPrint (c) {
    if (c !== 'C') {
      super.print();
    } else {
      let string = '';
      for (let i = 0; i < this.width; i++) {
        string += 'C';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(string);
      }
    }
  }
}
module.exports = Square;
