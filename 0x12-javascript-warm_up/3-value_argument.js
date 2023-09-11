#!/usr/bin/node
// Write a script that prints the first argument passed to it:

const arg = process.argv;
let length = 0;
let i = 0;
for (; i !== undefined; i++) {
  if (arg[i] === undefined) break;
  else length++;
}
if (length <= 2) console.log('No argument');
else if (length > 2) console.log(arg[2]);
