#!/usr/bin/node

/* script that searches
the second biggest integer
in the list of arguments. */

if (process.argv[3] === undefined || process.argv[3] === 1) {
  console.log('0');
} else {
  const len = process.argv.length;
  const array = process.argv.slice(2, len);
  array.sort(function (a, b) { return b - a; }); /* sort for numbers */
  array.shift(); /* delete first element */
  console.log(array[0]);
}
