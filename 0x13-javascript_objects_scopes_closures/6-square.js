#!/usr/bin/node
/* creating a subclass Square that inherits from the super class Rectangle */
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let string = '';
      for (let i = 0; i < this.width; i++) {
        string += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(string);
      }
    }
  }
}
module.exports = Square;
