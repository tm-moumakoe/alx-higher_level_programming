#!/usr/bin/node
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const { argv } = require('process');
add(Number(argv[2]), Number(argv[3]));
