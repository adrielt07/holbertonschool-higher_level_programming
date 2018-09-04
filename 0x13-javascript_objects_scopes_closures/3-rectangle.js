#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) { return undefined; }
    if (w <= 0 || h <= 0) { return undefined; }
    this.width = w;
    this.height = h;
  }
  // Method
  print () {
    let output = '';
    for (let i = 0; i < this.width; i++) { output += 'X'; }
    for (let j = 0; j < this.height; j++) { console.log(output); }
  }
};
