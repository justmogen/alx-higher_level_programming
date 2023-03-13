#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < x; n++) {
    console.log('C is fun');
  }
}
