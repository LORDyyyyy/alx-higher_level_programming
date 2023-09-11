#!/usr/bin/node

const { argv } = require('process');
const len = argv.length - 2;

console.log(len === 0 ? 'undefined is undefined' : (len === 1 ? argv[2] + ' is undefined' : argv[2] + ' is ' + argv[3]));
