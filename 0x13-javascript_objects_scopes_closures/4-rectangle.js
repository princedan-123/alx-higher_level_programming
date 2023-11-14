#!/usr/bin/node

/* Initializing  a class.
 * Adding methods rotate and double
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(string);
    }
  }

  rotate () {
    let tmp = '';
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
