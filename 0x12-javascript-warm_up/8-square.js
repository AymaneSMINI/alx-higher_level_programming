#!/usr/bin/node
const size = process.argv[2];
if (size === undefined && isNaN(size) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let i = 0; i < size; i++) {
      row += 'X';
    }
    console.log(row);
  }
}
