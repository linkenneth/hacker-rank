'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the lilysHomework function below.
function lilysHomework(arr) {
  /**
   * From what I can tell, there two possible "most beautiful" orderings:
   * (1) the ascending sorted array
   * (2) the descending sorted array
   *
   * Every swap can cause one element of the array to be perfectly placed,
   * and the last swap causes both elements to be perfectly placed.
   * 1 9 3 7 5 6 4 8 2 10
   * TODO: not done yet. also need to handle duplicate numbers
   */
  const ascending = arr.slice().sort();
  const descending = arr.slice().reverse();
  // argsort?
  for (let beautiful of [ascending, descending]) {
    const beautifulIndices = new Map(beautiful.map([x, i]);
    let i = 0;
    let j = 0;
    let swaps = 0;
    const visited = new Array(arr.length);
    while (i < arr.length) {
      if (beautiful[j] !== arr[j]) {

      }
    }
  }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    let result = lilysHomework(arr);

    ws.write(result + "\n");

    ws.end();
}
