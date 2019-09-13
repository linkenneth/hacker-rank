'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the roadsAndLibraries function below.
function roadsAndLibraries(n, c_lib, c_road, roads) {
  if (c_lib < c_road) {
    return c_lib * n;
  }

  /*
   * Plan: run DFS to find connected components. Math on size of connected
   * components.
   */
  const map = {};
  for (let city = 1; city <= n; city++) {
    map[city] = [];
  }

  for (let [cityA, cityB] of roads) {
    map[cityA].push(cityB);
    map[cityB].push(cityA);
  }

  const visited = new Set();
  const components = [0];
  let componentId = 0;
  for (let city = 1; city <= n; city++) {
    if (visited.has(city)) {
      continue;
    }

    const queue = [city];
    while (queue.length) {
      const city = queue.pop();
      if (visited.has(city)) {
        continue;
      }
      visited.add(city);
      components[componentId]++;
      for (let neighbor of map[city]) {
        if (!visited.has(neighbor)) {
          queue.push(neighbor);
        }
      }
    }
    components[++componentId] = 0;
  }

  let cost = (components.length - 1) * c_lib;
  for (let componentSize of components) {
    if (componentSize > 0) {
      cost += c_road * (componentSize - 1);
    }
  }

  return cost;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    console.log('start reading', Date.now());
    // console.log(inputString);
    const q = parseInt(readLine(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
      let readTime = Date.now();
    console.log('reading input', qItr, Date.now());
        const nmC_libC_road = readLine().split(' ');

        const n = parseInt(nmC_libC_road[0], 10);

        const m = parseInt(nmC_libC_road[1], 10);

        const c_lib = parseInt(nmC_libC_road[2], 10);

        const c_road = parseInt(nmC_libC_road[3], 10);

        let cities = Array(m);

        for (let i = 0; i < m; i++) {
            cities[i] = readLine().split(' ').map(citiesTemp => parseInt(citiesTemp, 10));
        }

    console.log('done reading. starting computing', Date.now());
    console.log('total read time', Date.now() - readTime);
    let time = Date.now();
        const result = roadsAndLibraries(n, c_lib, c_road, cities);
    console.log('done computing', Date.now());
    console.log('total time diff', Date.now() - time);

        ws.write(result + '\n');
    }

    ws.end();
}
