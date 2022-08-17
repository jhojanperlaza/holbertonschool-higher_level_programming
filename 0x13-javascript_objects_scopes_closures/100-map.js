#!/usr/bin/node
const list = require('./100-data').list;
const list2 = list.map(function (currentElement, index) {
    return (currentElement * index);
});

console.log(list);
console.log(list2);