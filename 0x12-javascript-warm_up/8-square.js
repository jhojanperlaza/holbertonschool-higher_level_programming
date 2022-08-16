#!/usr/bin/node

/* script that prints a square */

const y = parseInt(process.argv[2]);

if (isNaN(y)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < y; x++) {
    console.log('X'.repeat(y));
  }
}
