#!/usr/bin/node

const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2].toString();

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    weh(JSON.parse(body).characters)
  }
});

function weh(list) {
  for (let i in list) {
    print(list[i])
  }
}

function print(url) {
  request(url, function (error, response, body) {
      if (error) { console.log(error); } else { finalprint(JSON.parse(body)); }
  });
}

function finalprint(info) {
  console.log(info.name);
}
