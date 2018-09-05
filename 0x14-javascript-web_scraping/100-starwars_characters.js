#!/usr/bin/node

const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2].toString();

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let parsed = JSON.parse(body);
    for (let i in parsed.characters) {
      request(parsed.characters[i], function (error, response, body) {
        if (error) { console.log(error); } else { console.log(JSON.parse(body).name); }
      });
    }
  }
});
