#!/usr/bin/node

/* script that computes
and prints a factorial */

function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(process.argv[2]));
