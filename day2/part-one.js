/*
 * Node has native promises now, very cool. No array destructuring though,
 * bummer. Learned about process.exit(), figure I should call that whenever
 * finishing the "main" function for code clarity and error handling.
 *
 * This could've been solved using the same method as Day 1 (a single
 * readFile call and then processing the result by splitting on '\n') however
 * I wanted to try out the readline package, and the readline package allows
 * more asynchronicity as the file is processed line by line rather than all
 * at once.
 */

'use strict';
const fs = require('fs');
const rl = require('readline');

let fileName = process.argv[2] || 'input.txt';
let readStream = fs.createReadStream(fileName);
getTotalWrappingPaper(readStream).then((totalWrappingPaper) => {
  console.log(totalWrappingPaper);
  process.exit(0);
}).catch((err) => {
  console.error(err);
  process.exit(1);
});

function getTotalWrappingPaper(stream) {
  return new Promise((resolve, reject) => {
    let totalWrappingPaper = 0;
    let lines = rl.createInterface({
      input: stream
    });

    lines.on('line', (line) => {
      let dimensions = line.split('x');
      let l = dimensions[0];
      let w = dimensions[1];
      let h = dimensions[2];
      totalWrappingPaper += getWrappingPaper(l, w, h);
    });

    lines.on('close', () => {
      resolve(totalWrappingPaper);
    });

    stream.on('error', (err) => {
      reject(err);
    });
  });
}

function getWrappingPaper(l, w, h) {
  let side1 = l * w;
  let side2 = l * h;
  let side3 = w * h;
  let slack = Math.min(side1, side2, side3);
  return 2 * side1 + 2 * side2 + 2 * side3 + slack;
}
