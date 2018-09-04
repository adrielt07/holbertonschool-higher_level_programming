#!/usr/bin/node

exports.esrever = function (list) {
  let newlist = [];
  let i = list.length - 1;
  for (let index = 0; i >= 0; i--) {
    newlist[index] = list[i];
    index++;
  }
  return newlist;
};
