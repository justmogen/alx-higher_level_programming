#!/usr/bin/env node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Error: Both file path and content should be provided');
  process.exit(1);
}
fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log('File write successful.');
  }
});
