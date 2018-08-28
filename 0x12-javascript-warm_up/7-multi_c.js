#!/usr/bin/node

const CisFun = 'C is fun';
const occur = parseInt(process.argv[2], 10);

if (isNaN(occur)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occur; i++) { console.log(CisFun); }
}
