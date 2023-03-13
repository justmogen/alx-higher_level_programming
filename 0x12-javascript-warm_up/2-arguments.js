#!/usr/bin/node

// import { argv } from 'node:process';
const process = require('process');

const args = process.argv.slice(2);
/*
 * The script uses the process.argv array to get the arguments passed to
 * the script. Since the first two elements of process.argv are the path to
 * the node executable and the path to the script, we slice the array starting
 * from index 2 to get only the arguments.
 */
const numArgs = args.length;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
