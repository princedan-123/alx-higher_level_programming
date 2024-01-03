#!/usr/bin/node
/* a script that makes a request and writes the response to a file */

const fs = require('fs');
const request = require('request');

const filePath = process.argv[3];
const callback = (error, response, body) => {
  if (error === null) {
    const result = body;
    fs.writeFile(filePath, result, 'utf-8', (error) => {
      if (error) {
        console.log('');
      }
    });
  }
};

if (process.argv.length === 4) {
  const url = process.argv[2];
  request(url, callback);
}
