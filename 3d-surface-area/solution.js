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

const topArea = (A, i, j) => { return 1; }
const bottomArea = topArea;
const _adjacentArea = (adjacentFn) => {
  return (A, i, j) => {
    const [newI, newJ] = adjacentFn(i, j);
    if (newI < 0 || newI >= A.length || newJ < 0 || newJ >= A[0].length) {
      return A[i][j];
    } else if (A[newI][newJ] < A[i][j]) {
      return A[i][j] - A[newI][newJ];
    } else {
      return 0;
    }
  }
}
const leftArea = _adjacentArea((i, j) => [i - 1, j])
const rightArea = _adjacentArea((i, j) => [i + 1, j])
const forwardArea = _adjacentArea((i, j) => [i, j - 1])
const backwardArea = _adjacentArea((i, j) => [i, j + 1])

// Complete the surfaceArea function below.
function surfaceArea(A) {
  let area = 0;
  for (let i = 0; i < A.length; i++) {
    for (let j = 0; j < A[0].length; j++) {
      area += topArea(A, i, j);
      area += bottomArea(A, i, j);
      area += leftArea(A, i, j);
      area += rightArea(A, i, j);
      area += forwardArea(A, i, j);
      area += backwardArea(A, i, j);
    }
  }
  return area;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const HW = readLine().split(' ');

    const H = parseInt(HW[0], 10);

    const W = parseInt(HW[1], 10);

    let A = Array(H);

    for (let i = 0; i < H; i++) {
        A[i] = readLine().split(' ').map(ATemp => parseInt(ATemp, 10));
    }

    let result = surfaceArea(A);

    ws.write(result + "\n");

    ws.end();
}
