#!/usr/bin/node

let a = 1;
exports.logMe = function (item) {
  console.log(a + ': ' + item);
  a++;
};
