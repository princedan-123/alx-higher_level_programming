#!/usr/bin/node
/* converts a number to another base */
exports.converter = function (base) {
  return function convertion (number) {
    return number.toString(base);
  };
};
