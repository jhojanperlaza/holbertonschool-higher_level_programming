#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const NumOccurences = list.filter(function (num) {
    return num === searchElement;
  }).length;
  return NumOccurences;
};
