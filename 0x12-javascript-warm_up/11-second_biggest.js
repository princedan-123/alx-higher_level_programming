#!/usr/bin/node
// returns the second largest number of an array

let list = process.argv;
if (list.length <= 2) {
  console.log(0);
} else if (list.length === 3) {
  console.log(0);
} else {
  list = list.sort((a, b) => b - a);
  console.log(list[3]);
}
