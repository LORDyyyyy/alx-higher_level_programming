#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const api = process.argv[2];
const fileName = process.argv[3];

request(api, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
