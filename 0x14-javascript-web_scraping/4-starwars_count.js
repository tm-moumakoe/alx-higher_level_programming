#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles”
 * is present
 */
const req = require('request');
const argv = process.argv;
const reqURL = argv[2];

req.get(reqURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body);
    const results = allData.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) { count += 1; }
      }
    }
    console.log(count);
  }
});
