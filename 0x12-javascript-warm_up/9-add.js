#!/usr/bin/node

//  a script that prints the addition of 2 integers

const arg = process.argv;
const first = parseInt(arg[2]);
const second = parseInt(arg[3]);
function add (a, b) {
  console.log(a + b);
}
add(first, second);
