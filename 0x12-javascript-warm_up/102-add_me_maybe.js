#!/usr/bin/node
// a function that increments and calls a function

const addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
exports.addMeMaybe = addMeMaybe;
