#!/usr/bin/node
/* a script that uses request module to send a get request */

const request = require('request');

const callBack = (error, response, body) => {
  if (error === null) {
    const result = JSON.parse(body);
    console.log(result.title);
  }
};

if (process.argv.length === 3) {
  const input = process.argv[2];
  let url = 'https://swapi-api.alx-tools.com/api/films/:id';
  if (input >= '0' && input <= '9') {
    url = `https://swapi-api.alx-tools.com/api/films/${input}`;
    request(url, callBack);
  }
}
