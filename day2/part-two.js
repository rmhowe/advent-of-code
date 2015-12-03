/*
 * Not much new learned on top of part one
 */

'use strict';
const fs = require('fs');
const rl = require('readline');

let fileName = process.argv[2] || 'input.txt';
let readStream = fs.createReadStream(fileName);
getTotalRibbon(readStream).then((totalRibbon) => {
  console.log(totalRibbon);
  process.exit(0);
}).catch((err) => {
  console.error(err);
  process.exit(1);
});

function getTotalRibbon(stream) {
  return new Promise((resolve, reject) => {
    let totalRibbon = 0;
    let lines = rl.createInterface({
      input: stream
    });

    lines.on('line', (line) => {
      let dimensions = line.split('x');
      let l = dimensions[0];
      let w = dimensions[1];
      let h = dimensions[2];
      totalRibbon += getRibbon(l, w, h);
    });

    lines.on('close', () => {
      resolve(totalRibbon);
    });

    stream.on('error', (err) => {
      reject(err);
    });
  });
}

function getRibbon(l, w, h) {
  let smallestPerimeter = 2 * l + 2 * w + 2 * h - 2 * Math.max(l, w, h);
  let cubicVolume = l * w * h;
  return smallestPerimeter + cubicVolume;
}
