#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) { return undefined; }
    if (w <= 0 || h <= 0) { return undefined; }
    this.width = w;
    this.height = h;
  }
};
