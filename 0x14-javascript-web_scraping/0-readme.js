#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
const argv = process.argv;

fs.readFile(argv[2], 'utf-8', (err, data) => {
  if (err) { console.log(err); } else { console.log(data); }
});
