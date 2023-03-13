#!/usr/bin/node

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));

/*
const args = process.argv.slice(2);
const num = parseInt(args[0]);

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(num));
*/
