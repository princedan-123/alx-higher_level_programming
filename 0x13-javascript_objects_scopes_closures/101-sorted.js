#!/usr/bin/node
/* computing a new Object from an imported object */

const oldObject = require('./101-data.js').dict;
const values = Object.values(oldObject);
const keys = Object.keys(oldObject);
const newObject = {};

for (const value of values) {
  const list = [];
  for (const key of keys) {
    if (oldObject[key] === value) {
      list.push(key);
    }
  }
  const property = value.toString(10);
  newObject[property] = list;
}
console.log(newObject);
