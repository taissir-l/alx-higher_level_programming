#!/usr/bin/node
const arg = process.argv;
if (arg.length <= 3) {
  console.log(0);
} else {
  const arr = arg.slice(2);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = Math.floor(Number(arr[i]));
  }
  const val = Math.max(...arr);
  let maxa = -100;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > maxa && arr[i] < val) {
      maxa = arr[i];
    }
  }
  console.log(maxa);
}
