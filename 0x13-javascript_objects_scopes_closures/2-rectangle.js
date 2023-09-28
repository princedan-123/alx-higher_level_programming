#!/usr/bin/node
// creating a Rectangle class

class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;