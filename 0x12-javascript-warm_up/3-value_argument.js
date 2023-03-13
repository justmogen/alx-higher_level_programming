#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);
/*
 * script checks whether the first element of the args array is truth
 * (i.e., not null, undefined, false, 0, or an empty string).
 * If it is, we print the first argument using console.log(...).
 * Otherwise, we print "No argument".
 */

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No arguments');
}
