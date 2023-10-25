#!/usr/bin/node

const request = require('request');

const api = process.argv[2];

request(api, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);

  const countTasks = {};

  for (const todo of data) {
    if (todo.completed) {
      if (countTasks[todo.userId]) {
        countTasks[todo.userId]++;
      } else {
        countTasks[todo.userId] = 1;
      }
    }
  }

  console.log(countTasks);
});
