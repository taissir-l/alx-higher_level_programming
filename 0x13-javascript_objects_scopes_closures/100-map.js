#!/usr/bin/node
const list = require('./100-data.js').list;
const arg = list.map((element, index) => element * index);
console.log(list);
console.log(arg);
