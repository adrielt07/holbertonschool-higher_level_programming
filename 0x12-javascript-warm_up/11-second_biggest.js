#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let array = process.argv.slice();
  for (let i = 0; i < array.length; i++) { array[i] = parseInt(array[i]); }
  console.log(parseInt(array[array.length - 2]));
}
