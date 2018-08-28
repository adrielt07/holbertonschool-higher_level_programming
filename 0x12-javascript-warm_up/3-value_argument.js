#!/usr/bin/node

const argument = process.argv[2];

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(argument);
}
