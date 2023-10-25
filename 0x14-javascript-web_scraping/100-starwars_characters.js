#!/usr/bin/node

const request = require('request');

const movId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movId}/`;

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movData = JSON.parse(body);
  const chars = movData.characters;

  for (const charLink of chars) {
    request(charLink, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charName = JSON.parse(body).name;

      console.log(charName);
    });
  }
});
