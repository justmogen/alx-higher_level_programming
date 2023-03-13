#!/usr/bin/node

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));

/*
const args = process.argv.slice(2);
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (isNaN(num1) || isNaN(num2)) {
  console.log("Missing or invalid numbers");
} else {
  const sum = num1 + num2;
  console.log(sum);
}
*/
