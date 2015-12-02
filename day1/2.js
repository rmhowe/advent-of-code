'use strict';
const fs = require('fs');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  console.log(getFirstBasementIndex(String(data)));
});

function getFirstBasementIndex(directions) {
  let currentFloor = 0;
  let firstBasement;

  directions.split('').some((floor, index) => {
    if (floor === '(') {
      currentFloor++;
    } else if (floor === ')') {
      currentFloor--;
    }

    if (currentFloor === -1) {
      firstBasement = index + 1;
      return true;
    }
  });

  return firstBasement;
}
