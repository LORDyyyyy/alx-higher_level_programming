#!/usr/bin/node

const [, , ...args] = process.argv;
const nums = [];

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args.forEach((element) => (nums.push(parseInt(element))));
  nums.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
