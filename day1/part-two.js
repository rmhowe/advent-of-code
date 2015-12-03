/*
 * More standard javascript, using 'some' as an iterator so that I can
 * break when the first basement instruction is found.
 *
 * This solution doesn't handle newlines like the python version, if I
 * needed multi-line support I would just count the newlines as I was
 * going and then subtract them from the index at the end
 */

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
