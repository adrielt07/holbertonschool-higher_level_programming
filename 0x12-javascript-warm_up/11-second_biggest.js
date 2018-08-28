#!/usr/bin/node

function filter (array) {
  let newArray = [];
  for (let i = 2, j = 0; i < array.length; i++, j++) {
    newArray[j] = parseInt(array[i]);
  }
  return newArray.sort();
}

if (process.argv.length < 4) {
  console.log(0);
} else {
  let array = filter(process.argv);
  console.log(array[array.length - 2]);
}
