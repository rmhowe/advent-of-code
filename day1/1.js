'use strict';
const fs = require('fs');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  console.log(getFloor(String(data)));
});

function getFloor(directions) {
  return directions.split('').reduce((previousFloor, floor) => {
    if (floor === '(') {
      return previousFloor + 1;
    } else if (floor === ')') {
      return previousFloor - 1;
    }
    return previousFloor;
  }, 0);
}
