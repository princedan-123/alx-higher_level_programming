#!/usr/bin/node
const num = process.argv;
function factorial (n) {
  if (n === 1 || isNaN(n)) return 1;
  return n * factorial(n - 1);
}
const result = factorial(num[2]);
console.log(result);
