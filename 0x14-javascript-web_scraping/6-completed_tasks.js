#!/usr/bin/node

const request = require('request');
let url;
if (process.argv[2] === undefined) {
  url = 'https://jsonplaceholder.typicode.com/todos';
} else {
  url = process.argv[2];
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let parsed = JSON.parse(body);
    let info = {};
    for (let i in parsed) {
      if (parsed[i].userId in info === false) {
        info[parsed[i].userId] = 0;
      }
      if (parsed[i].completed === true) {
        info[parsed[i].userId]++;
      }
    }
    console.log(info);
  }
});
