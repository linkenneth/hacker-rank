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

// Complete the gridSearch function below.
function gridSearch(G, P) {
  /**
   * Brute force. Let's see if it works. Are there better solutions such as
   * a modified 2D KMP?
   */
  for (let R = 0; R < G.length - P.length; R++) {
    for (let C = 0; C < G[0].length - P[0].length; C++) {
      let stop = false;
      for (let r = 0; r < P.length; r++) {
        for (let c = 0; c < P[0].length; c++) {
          if (G[R + r][C + c] !== P[r][c]) {
            stop = true;
            break;
          } else if (r === P.length - 1 && c === P[0].length - 1) {
            return 'YES';
          }
        }
        if (stop) { break; }
      }
    }
  }
  return 'NO';
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const RC = readLine().split(' ');

        const R = parseInt(RC[0], 10);

        const C = parseInt(RC[1], 10);

        let G = [];

        for (let i = 0; i < R; i++) {
            const GItem = readLine();
            G.push(GItem);
        }

        const rc = readLine().split(' ');

        const r = parseInt(rc[0], 10);

        const c = parseInt(rc[1], 10);

        let P = [];

        for (let i = 0; i < r; i++) {
            const PItem = readLine();
            P.push(PItem);
        }

        let result = gridSearch(G, P);

        ws.write(result + "\n");
    }

    ws.end();
}
