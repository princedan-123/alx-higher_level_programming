#!/usr/bin/node
/* Checks the number of occurrence in an array */

exports.nbOccurences = function (list, searchElement) {
  let item;
  let count = 0;
  for (item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return count;
};
