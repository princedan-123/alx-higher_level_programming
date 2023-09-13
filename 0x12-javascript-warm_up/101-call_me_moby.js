#!/usr/bin/node
// a function that executes x times a function

const callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
exports.callMeMoby = callMeMoby; // this could also be module.export
