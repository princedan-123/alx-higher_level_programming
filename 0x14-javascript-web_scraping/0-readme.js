#!/usr/bin/node
/* a script that reads and logs the content of a file */

const fs = require('fs');

if (process.argv.length === 3) {
  const filePath = process.argv[2];
  fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
}
