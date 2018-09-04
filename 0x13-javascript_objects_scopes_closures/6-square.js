#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  // Inheriting from Rectangle
  constructor (size) {
    super(size, size);
  }

  // Method charPrint(c) - takes a Character that replaces 'X' when using print method
  charPrint (c) {
    if (c === undefined) { c = 'X' };
    super.print(c);
  }
};
