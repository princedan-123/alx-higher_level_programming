#!/usr/bin/node
/* A script that sends a request to starwars api. */

const request = require('request');

const callBack = (error, response, body) => {
  if (error === null) {
    const result = JSON.parse(body);
    const count = result.results.reduce((count, movies) => {
      if (movies.characters.some((url) => url.endsWith('/18/'))) {
        count += 1;
      }
      return count;
    }, 0);
    console.log(count);
  }
};

if (process.argv.length === 3) {
  const url = process.argv[2];
  request(url, callBack);
}
