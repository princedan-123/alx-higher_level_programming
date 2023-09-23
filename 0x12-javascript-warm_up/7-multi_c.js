#!/usr/bin/node

const arg = process.argv;
let i = 0;
const first = parseInt(arg[2]);
if (isNaN(first)) console.log('Missing number of occurrences');
else {
  for (; i < first; i++) console.log('C is fun');
}
