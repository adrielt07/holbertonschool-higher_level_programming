#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ret = 0;
  let len = list.length;
  for (let index = 0; index < len; index++) {
    if (searchElement === list[index]) { ret++; }
  }
  return ret;
};
