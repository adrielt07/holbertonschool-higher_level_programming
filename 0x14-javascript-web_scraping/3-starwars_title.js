#!/usr/bin/node

const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2].toString();

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
