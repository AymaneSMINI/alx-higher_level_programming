#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === undefined) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const a = process.argv[2];
console.log(factorial(a));
