#!/usr/bin/node

const add = (a, b) => {
  return a + b;
};

const [,, arg1, arg2] = process.argv;

const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

if (!isNaN(num1) && !isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
