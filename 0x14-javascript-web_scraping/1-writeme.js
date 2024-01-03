#!/usr/bin/node
/* a script that writes a string to a file */

const fs = require('fs');

const callback = (error) => {
  if (error) {
    console.log(error);
  }
};

if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const data = process.argv[3];
  fs.writeFile(filePath, data, 'utf-8', callback);
}
