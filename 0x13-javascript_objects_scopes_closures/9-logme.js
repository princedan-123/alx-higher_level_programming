#!/usr/bin/node
// keeps count of the number of times argument is logged
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}:`, item);
  count++;
};
