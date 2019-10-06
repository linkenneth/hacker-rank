'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the matrixRotation function below.
function matrixRotation(matrix, r) {
  const M = matrix.length;
  const N = matrix[0].length;
  const layerCount = Math.ceil(Math.min(M, N) / 2);

  // construct circular arrays for each layer
  const layers = new Array(layerCount);
  for (let l = 0; l < layerCount; l++) {
    layers[l] = [];
    // top
    for (let i = l; i < N - l; i++) {
      layers[l].push(matrix[l][i]);
    }
    // right
    for (let i = l + 1; i < M - l - 1; i++) {
      layers[l].push(matrix[i][N - l - 1]);
    }
    // bottom
    for (let i = N - l - 1; i >= l; i--) {
      layers[l].push(matrix[M - l - 1][i]);
    }
    // left
    for (let i = M - l - 2; i >= l + 1; i--) {
      layers[l].push(matrix[i][l]);
    }
  }
  // console.log('layers', layers);

  // rotate said circular array
  for (let l = 0; l < layerCount; l++) {
    const L = layers[l].length;
    layers[l] = layers[l].slice(r % L, L).concat(layers[l].slice(0, r % L));
  }
  // console.log('rotated layers', layers);

  // TODO: learn to initialize 2D arrays easier in JS
  // populate new matrix
  const newMatrix = new Array(M);
  for (let m = 0; m < M; m++) { newMatrix[m] = new Array(N); }
  for (let l = 0; l < layerCount; l++) {
    // top
    let j = 0;
    for (let i = l; i < N - l; i++) {
      newMatrix[l][i] = layers[l][j++];
    }
    // right
    for (let i = l + 1; i < M - l - 1; i++) {
      newMatrix[i][N - l - 1] = layers[l][j++];
    }
    // bottom
    for (let i = N - l - 1; i >= l; i--) {
      newMatrix[M - l - 1][i] = layers[l][j++];
    }
    // left
    for (let i = M - l - 2; i >= l + 1; i--) {
      newMatrix[i][l] = layers[l][j++];
    }
  }
  return newMatrix;
}

function printMatrix(matrix) {
  for (let r = 0; r < matrix.length; r++) {
    console.log(...matrix[r]);
  }
}

function main() {
    const mnr = readLine().replace(/\s+$/g, '').split(' ');

    const m = parseInt(mnr[0], 10);

    const n = parseInt(mnr[1], 10);

    const r = parseInt(mnr[2], 10);

    let matrix = Array(m);

    for (let i = 0; i < m; i++) {
        matrix[i] = readLine().replace(/\s+$/g, '').split(' ').map(matrixTemp => parseInt(matrixTemp, 10));
    }

    let newMatrix = matrixRotation(matrix, r);
    printMatrix(newMatrix);
}
