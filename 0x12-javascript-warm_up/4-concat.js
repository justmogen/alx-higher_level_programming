#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

if (args.length === 2) {
  const formatArgs = args.join(' is ');
  console.log(formatArgs);
} else {
  console.log('Two arguments are required');
}
