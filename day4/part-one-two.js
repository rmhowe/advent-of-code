/*
 * This is currently not working, not sure why...
 */

'use strict';
const fs = require('fs');
const crypto = require('crypto');

let fileName = process.argv[2] || 'input.txt';
fs.readFile(fileName, (err, data) => {
  console.log(getKeyPart(String(data)));
});

function getKeyPart(secretKey) {
  let keyPart = 0;
  let digest = '';
  while (!digest.startsWith('00000')) {
    keyPart++;
    let md5sum = crypto.createHash('md5');
    md5sum.update(secretKey + keyPart);
    digest = md5sum.digest('hex');
  }

  return keyPart;
}
