#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
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
