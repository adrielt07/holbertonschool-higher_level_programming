#!/usr/bin/node

const argument = process.argv[2];

if (argument === null) {
  console.log('No argument');
} else {
  console.log(argument);
}
