#!/usr/bin/node
// prints all characters of a Star Wars movie
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let chars = [];

req(url, (error, response, body) => {
  if (error) { console.log(error); return; }
  const data = JSON.parse(body);
  chars = data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === chars.length) {
    return;
  }

  req(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
