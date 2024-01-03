#!/usr/bin/node
/* a script that uses request module to send a get request */

const request = require('request');

const callBack = (error, response, body) => {
  console.log('code:', response.statusCode);
  if (error) {
    console.log('');
  }
};

if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, callBack);
}
