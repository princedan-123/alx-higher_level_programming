#!/usr/bin/node
// creating a child class of Square class

const parentSquare = require('./5-square');
class Square extends parentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === 'C') {
	    for (let i = 0; i < this.height; i++) {
		    let wide = '';
		    for (let j = 0; j < this.width; j++) {
			    wide += 'C';
		    }
		    console.log(wide);
	    }
    } else {
	    for (let i = 0; i < this.height; i++) {
		    let wide = '';
		    for (let j = 0; j < this.width; j++) {
			    wide += 'X';
		    }
		    console.log(wide);
	    }
    }
  }
}
module.exports = Square;
