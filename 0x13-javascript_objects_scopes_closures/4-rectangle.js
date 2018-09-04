#!/usr/bin/node

module.exports = class Rectangle {
  // Constructor - Takes two positive intergers
  constructor (w, h) {
    if (w === undefined || h === undefined) { return undefined; }
    if (w <= 0 || h <= 0) { return undefined; }
    this.width = w;
    this.height = h;
  }
  // Method print - prints the shape of the rectangle using 'X' symbol
  print () {
    let output = '';
    for (let i = 0; i < this.width; i++) { output += 'X'; }
    for (let j = 0; j < this.height; j++) { console.log(output); }
  }

  // Method rotate - swap the value of width and hegith
  rotate () {
    let save = this.height;
    this.height = this.width;
    this.width = save;
  }

  // Method double - multiplies the value of width and height by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
