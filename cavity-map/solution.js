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

function neighbors(r, c) {
  return [[r + 1, c], [r - 1, c], [r, c - 1], [r, c + 1]];
}

// Complete the cavityMap function below.
function cavityMap(grid) {
  const newGrid = [...Array(grid.length)].map(() => new Array(grid[0].length));
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (r >= 1 && r < grid.length - 1 && c >= 1 && c < grid[0].length - 1 &&
          neighbors(r, c).every(([r1, c1]) => grid[r1][c1] < grid[r][c])) {
        newGrid[r][c] = 'X';
      } else {
        newGrid[r][c] = grid[r][c];
      }
    }
  }
  return newGrid.map((row) => row.join(''));
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let grid = [];

    for (let i = 0; i < n; i++) {
        const gridItem = readLine();
        grid.push(gridItem);
    }

    let result = cavityMap(grid);

    ws.write(result.join("\n") + "\n");

    ws.end();
}
