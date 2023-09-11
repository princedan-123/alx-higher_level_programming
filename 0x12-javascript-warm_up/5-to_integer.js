#!/usr/bin/node

const arg = process.argv;
if (arg.length < 2) console.log('My number: Not a number');
else if (arg.length >= 2) {
  const first = parseInt(arg[2], 10);
  if (isNaN(first)) console.log('My number: Not a number');
  else console.log('My number:', first);
}
