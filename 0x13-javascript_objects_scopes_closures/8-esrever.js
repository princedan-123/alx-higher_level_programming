#!/usr/bin/node
// reverses an array without using inbuilt method reverse

exports.esrever = function (list) {
  newArray = [];
  for (let last = list.length - 1; last >= 0; last--) {
    newArray.push(list[last]);
  }
  return newArray;
};
