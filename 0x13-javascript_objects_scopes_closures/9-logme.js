#!/usr/bin/node
/* A script that uses closure to print an argument */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
