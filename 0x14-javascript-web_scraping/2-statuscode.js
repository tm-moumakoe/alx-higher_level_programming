#!/usr/bin/node
// displays the status code of a GET request
const req = require('request');
const argv = process.argv;

req(argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode);
});
