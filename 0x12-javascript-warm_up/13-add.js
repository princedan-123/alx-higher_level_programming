#!/usr/bin/node
// creating a function that is 'visible from outside'

function add (num1, num2) {
  return num1 + num2;
}
module.exports.add = add;
