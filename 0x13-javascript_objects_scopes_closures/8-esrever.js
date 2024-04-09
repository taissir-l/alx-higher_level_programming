#!/usr/bin/node

exports.esrever = function (list) {
  const len = Math.floor(list.length / 2);
  for (let i = 0; i < len; i++) {
    const l = list.length - i - 1;
    const h = list[l];

    list[l] = list[i];
    list[i] = h;
  }

  return (list);
};
