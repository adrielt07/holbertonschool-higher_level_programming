#!/usr/bin/node

const request = require('request');
let id = '18';
let count = 0;
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let parsed = JSON.parse(body);
    for (let i in parsed.results) {
      for (let j in parsed.results[i].characters) {
        if (parsed.results[i].characters[j].search(id) !== -1) { count++; }
      }
    }
  }
  console.log(count);
});
