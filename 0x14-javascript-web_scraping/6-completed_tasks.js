#!/usr/bin/node
// computes the number of tasks completed by user id
const req = require('request');
const argv = process.argv;
const reqURL = argv[2];
const list = {};

req.get(reqURL, (err, res, body) => {
  if (err) { console.log(err); } else {
    const data = JSON.parse(body);
    let user = 'default';
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (!(data[i].userId in list)) {
          user = data[i].userId;
          list[user] = 1;
        } else {
          user = data[i].userId;
          list[user] += 1;
        }
      }
    }
    console.log(list);
  }
});
