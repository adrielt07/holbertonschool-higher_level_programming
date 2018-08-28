#!/usr/bin/node

const occur = parseInt(process.argv[2], 10);
const print = 'X';

if (isNaN(occur)) {
  console.log('Missing size');
} else {
  let output = '';
  for (let i = 0; i < occur; i++) { output += print; }
  for (let j = 0; j < occur; j++) { console.log(output); }
}
