'use strict';
const fs = require('fs');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  console.log(getFloor(String(data)));
});

function getFloor(directions) {
  let currentFloor = 0;

  directions.split('').forEach((floor) => {
    if (floor === '(') {
      currentFloor++;
    } else if (floor === ')') {
      currentFloor--;
    }
  });

  return currentFloor;
}
