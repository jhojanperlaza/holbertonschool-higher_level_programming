#!/usr/bin/node

let items = 0;
exports.logMe = function (item) {
  const string = items + ': ' + item;
  console.log(string);
  items++;
};
