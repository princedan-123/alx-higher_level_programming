#!/usr/bin/node

//  a script that prints a square

let width = '';
const arg = process.argv;
const size = parseInt(arg[2]);
let i = 0;
if (isNaN(size)) console.log('Missing size');
else {
  for (; i < size; i++) {
    width = '';
    for (let y = 0; y < size; y++) {
      width += 'X';
    }
    console.log(width);
  }
}
