#!/usr/bin/node

const request = require('request');
let url;
let Wedge = 'https://swapi.co/api/people/18/';
let count = 0;

if (url === undefined) {
  url = 'http://swapi.co/api/films';
} else {
  url = process.argv[2];
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let parsed = JSON.parse(body);
    for (let i in parsed.results) {
      if (parsed.results[i].characters.includes(Wedge)) {
        count++;
      }
    }
  }
  console.log(count);
});
