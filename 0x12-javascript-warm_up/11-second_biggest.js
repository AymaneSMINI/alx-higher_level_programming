#!/usr/bin/node
const numbers = process.argv.slice(2);
if (numbers.length <= 1) {
  console.log(0);
} else { 
  console.log(numbers.sort().reverse()[1]);
}
