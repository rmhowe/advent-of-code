/*
 * This was pretty simple, decided to give python a break and come back to
 * the nice comfort of javascript. Also abusing the fact here that there are
 * no out of bounds errors on arrays in javascript, it'll just return undefined.
 * Nice to know node handles template strings, but no default arguments yet
 * (I mean that's V8's fault, not node)
 */

'use strict';
const fs = require('fs');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  let initialSequence = String(data).trim();
  console.log(getLookSay(initialSequence, 50).length);
});

function getLookSay(sequence, iterations) {
  let nextSequence = '';
  let characters = sequence.split('');
  let characterCount = 1;
  characters.forEach((character, i) => {
    if (character === characters[i + 1]) {
      characterCount++;
    } else {
      nextSequence += `${characterCount}${character}`;
      characterCount = 1;
    }
  });

  if (iterations === 1) {
    return nextSequence;
  } else {
    return getLookSay(nextSequence, iterations - 1);
  }
}
