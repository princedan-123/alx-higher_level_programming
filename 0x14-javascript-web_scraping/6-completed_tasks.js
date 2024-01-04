#!/usr/bin/node
/* a script that makes a request to an API */

const request = require('request');

const task = {};
let i = 1;
const callback = (error, response, body) => {
  if (error === null) {
    const result = JSON.parse(body);
    for (; i <= 10; i++) {
      let count = 0;
      for (const element of result) {
        if (element.userId === i && element.completed === true) {
          count += 1;
        }
      }
      String(i);
      task[i] = count;
    }
    console.log(task);
  }
};

if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, callback);
}
