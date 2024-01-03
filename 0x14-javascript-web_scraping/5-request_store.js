#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const fs = require('fs');
const req = require('request');
const argv = process.argv;
const reqURL = argv[2];

req.get(reqURL, (err, res, body) => {
  if (err) { console.log(err); } else {
    const data = body;
    fs.writeFile(argv[3], data, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
