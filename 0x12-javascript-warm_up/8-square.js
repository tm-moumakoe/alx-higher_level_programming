#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2]) || argv[2] === undefined) console.log('Missing size');
else {
  const size = Number(argv[2]);
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
