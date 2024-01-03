#!/usr/bin/node
/**
 * prints the title of a Star Wars movie where the episode number matches
 * a given integer
 */
const req = require('request');
const argv = process.argv;
const reqURL = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

req.get(reqURL, (err, res, body) => {
  if (err) { console.log(err); } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
