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

// Complete the steadyGene function below.
function steadyGene(gene) {
  /**
   * Strategy: "slinky" algorithm.
   *
   * Shortest substring that contains at least a given set of elements
   * can be completed in linear time with a sort of "slinky" algorithm.
   * Essentially, keep two pointers, one for the end of the string and one
   * for the beginning. Try to increment the end of the string, then if the
   * current string encounters an element that we need to include, "pull"
   * the beginning pointer forwards maximally until this the shortest possible
   * string that fulfills the condition ending at the end of the string is
   * found. Record into array like DP.
   *
   * TODO: since this question involves significant amounts of counter math
   * used Python instead
   */
  const L = new Array(gene.length)

  // first determine the minimum set of elements the substring must include
  const T = gene.length / 4
  const frequencies = { A: -T, C: -T, G: -T, T: -T };
  for (let c of gene) {
    frequencies[c]++;
  }
  for (let c in frequencies) {
    if (frequencies[c] < 0) {
      frequencies[c] = 0;
    }
  }
  console.log(frequencies);

  let i = 0;
  let j = 0;
  const count = { A: 0, C: 0, G: 0, T: 0 };
  while (j < gene.length) {
    j += 1
  }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const gene = readLine();

    let result = steadyGene(gene);

    ws.write(result + "\n");

    ws.end();
}
