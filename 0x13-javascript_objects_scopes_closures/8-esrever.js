#!/usr/bin/node
/* A script that reverses an array without the use of in-built reverse. */

exports.esrever = function (list) {
  let item;
  const newArray = [];
  for (item of list) {
    newArray.unshift(item);
  }
  return newArray;
};
