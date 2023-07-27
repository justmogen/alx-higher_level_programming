#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error: Both URL and file path must be provided.');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log('File write successful.');
      }
    });
  }
});
