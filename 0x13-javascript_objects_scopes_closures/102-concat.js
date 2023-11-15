#!/usr/bin/node
/* A script that concatnates the content of two files.
 * the path to both files are passed as command line arguments
 */
const fs = require('fs');
const fileOne = process.argv[2];
const fileTwo = process.argv[3];
const destFile = process.argv[4];
let contentOne = fs.readFileSync(fileOne, 'utf8')
let contentTwo = fs.readFileSync(fileTwo, 'utf8')
fs.appendFileSync(destFile, contentOne, 'utf8')
fs.appendFileSync(destFile, contentTwo, 'utf8')
