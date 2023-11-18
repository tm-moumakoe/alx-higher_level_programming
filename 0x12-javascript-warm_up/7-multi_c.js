#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2]) || argv[2] === undefined) console.log('Missing number of occurrences');
else {
  const x = Number(argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
