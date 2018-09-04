#!/usr/bin/node

const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  // Inheriting from Square class from 5-square
  constructor (size) {
    super(size);
  }

  // Method charPrint(c) - takes a Character that replaces 'X' when using print method
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    super.print(c);
  }
};
