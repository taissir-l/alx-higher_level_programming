#!/usr/bin/node
const dict = require('./101-data.js').dict;
const s = {};
for (const key in dict) {
  if (s[dict[key]] === undefined) {
    s[dict[key]] = [key];
  } else {
    s[dict[key]].push(key);
  }
}

console.log(s);
