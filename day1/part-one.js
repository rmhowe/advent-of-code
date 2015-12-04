/*
 * Learning about typical node constructs, using fs, using the process
 * object. Everything else is just standard javascript.
 */

'use strict';
const fs = require('fs');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  console.log(getFloor(String(data)));
});

function getFloor(directions) {
  let directionsArray = directions.split('');
  let finalFloor = directionsArray.reduce((previousFloor, direction) => {
    if (direction === '(') {
      return previousFloor + 1;
    } else if (direction === ')') {
      return previousFloor - 1;
    }
    return previousFloor;
  }, 0);

  return finalFloor;
}
