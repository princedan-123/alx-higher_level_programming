#!/usr/bin/node
// converts a number to another base

exports.converter = function (base) {
  function convert (num) {
    return num.toString(base);
  }
  return convert;
};
