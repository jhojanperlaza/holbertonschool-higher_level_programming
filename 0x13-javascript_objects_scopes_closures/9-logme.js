#!/usr/bin/node

let items = 0;
exports.logMe = function (item) {
  string = items + ': ' + item;
  console.log(string);
  items++;
};
