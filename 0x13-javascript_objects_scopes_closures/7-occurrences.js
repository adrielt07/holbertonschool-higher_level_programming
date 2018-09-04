#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  var ret = 0;
  var len = list.length;
  for (let index = 0; index < len; index++) {
    if (searchElement === list[index]) { ret++; }
  }
  return ret;
};
