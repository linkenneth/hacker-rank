/**
 * The solution needs to be slightly more efficient. Try 2D Rabin-Karp
 * algorithm (ie. hash submatrices).
 *
 * TODO: this seems to be even slower. Before was O(R * C * r * c) worst case,
 * but now it always requires O(R * C * (r + c)) at least to compute hashes...
 */

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
   * 2D Rabin-Karp algorithm. Compute all possible hashes (just sum of ints)
   * of submatrices in O(R * C) time using a rolling window, then compare
   * against the hash of P. O(R * C) comparisons each in constant time.
   * If any match, do actual comparison. Of course, the worst case is that
   * all hashes match, but this is unlikely.
   */
  const hashes = [...Array(G.length - P.length + 1)].map(
    () => Array(G[0].length - P[0].length + 1).fill(0));


  // compute all hashes
  for (let R = 0; R < G.length - P.length + 1; R++) {
    if (R === 0) {
      // initial seed
      for (let r = 0; r < P.length; r++) {
        for (let c = 0; c < P[0].length; c++) {
          hashes[0][0] += +G[r][c];
        }
      }
    } else {
      hashes[R][0] = hashes[R - 1][0]
      for (let c = 0; c < P[0].length; c++) {
        hashes[R][0] -= +G[R - 1][c];
        hashes[R][0] += +G[R + P.length - 1][c];
      }
    }

    for (let C = 1; C < G[0].length - P[0].length + 1; C++) {
      hashes[R][C] = hashes[R][C - 1]
      for (let r = 0; r < P.length; r++) {
        hashes[R][C] -= +G[R + r][C - 1];
        hashes[R][C] += +G[R + r][C + P[0].length - 1];
      }
    }
  }
  console.log('Done constructing hashes.');

  // compute hash of P
  let pHash = 0;
  for (let r = 0; r < P.length; r++) {
    for (let c = 0; c < P[0].length; c++) {
      pHash += +P[r][c];
    }
  }
  // console.log('hashes', hashes);
  // console.log('pHash', pHash);

  // check if any match, and perform actual comparison if match
  for (let R = 0; R < hashes.length; R++) {
    for (let C = 0; C < hashes[0].length; C++) {
      if (pHash === hashes[R][C]) {
        let stop = false;
        for (let r = 0; r < P.length; r++) {
          for (let c = 0; c < P[0].length; c++) {
            if (G[R + r][C + c] !== P[r][c]) {
              stop = true;
              break;
            } else if (r === P.length - 1 && c === P[0].length - 1) {
              return 'YES'
            }
          }
        }
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
        console.log('R, C', R, C);

        let G = [];

        for (let i = 0; i < R; i++) {
            const GItem = readLine();
            G.push(GItem);
        }

        const rc = readLine().split(' ');

        const r = parseInt(rc[0], 10);

        const c = parseInt(rc[1], 10);
        console.log('r, c', r, c);

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
