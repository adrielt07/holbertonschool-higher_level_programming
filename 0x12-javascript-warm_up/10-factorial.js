#!/usr/bin/node

function factorial (x) {
  if (isNaN(x) || x === 1) { return 1; } else { return x * factorial(x - 1); }
}

const num1 = parseInt(process.argv[2], 10);

console.log(factorial(num1));
