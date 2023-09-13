#!/usr/bin/node

const fs = require('fs');

const srcFile1 = process.argv[2];
const srcFile2 = process.argv[3];
const destFile = process.argv[4];

const content1 = fs.readFileSync(srcFile1, 'utf8');
const content2 = fs.readFileSync(srcFile2, 'utf8');

const allContent = content1 + content2;

fs.writeFileSync(destFile, allContent);
