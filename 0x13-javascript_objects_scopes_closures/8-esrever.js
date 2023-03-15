#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let n = list.length - 1; n >= 0; n--) {
    reversed.push(list[n]);
  }
  return reversed;
};
