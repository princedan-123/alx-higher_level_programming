#!/usr/bin/node

/* Write a script that prints two arguments passed to it,
 * in the following format: “ is ”
 */

const arg = process.argv;
let i = 2;
let output = '';
let init = '';
const undef = undefined;
while (i < arg.length) {
  if (i === 2) {
    init += `${arg[i]}` + ' is';
    output += init;
    if (arg.length === 3) {
      output += ' ';
      output += undef;
    }
  } else {
    output += ' ';
    output += arg[i];
  }
  i++;
}
console.log(output);
