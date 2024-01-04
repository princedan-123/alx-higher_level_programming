#!/usr/bin/node
/* a script that makes a request to an API */

const request = require('request');

const task = {};
const id = [];

const callback = (error, response, body) => {
  if (error === null) {
    const result = JSON.parse(body);
    for (const obj of result) {
      if (obj.userId !== null) {
        if (!id.includes(obj.userId)) {
          id.push(obj.userId);
        }
      }
    }
    for (const userid of id) {
      let count = 0;
      for (const obj of result) {
        if (obj.userId === userid && obj.completed === true) {
          count += 1;
        }
      }
      String(userid);
      task[userid] = count;
    }
    console.log(task);
  }
};

if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, callback);
}
