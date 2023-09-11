#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const [,, arg] = process.argv;

const num = parseInt(arg);

console.log(factorial(num));
