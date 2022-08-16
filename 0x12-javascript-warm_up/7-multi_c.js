#!/usr/bin/node

/* script that prints
x times “C is fun” */

let x = 0;
const y = parseInt(process.argv[2]);

if (y !== undefined) {
  while (x < y) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
