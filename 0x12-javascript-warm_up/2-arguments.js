#!/usr/bin/node

const { argv } = require('process');

console.log(argv.length - 2 === 0 ? 'No argument' : (argv.length - 2 === 1 ? 'Argument found' : 'Arguments found'));
