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

// Complete the highestValuePalindrome function below.
function highestValuePalindrome(s, n, k) {
  /**
   * Strategy: Greedy.
   *
   * Find number of mismatches. If > k, return -1.
   * If === k, just take max every mimsatch.
   * If < k, start with beginning and switch to 9's for each set of mismatches
   * until k left.
   */
  let mismatches = 0;
  for (let i = 0; i <= n - i - 1; i++) {
    if (s[i] !== s[n - i - 1]) {
      mismatches++;
    }
  }
  if (k < mismatches) {
    return '-1';
  } else {
    let palindrome = [];
    for (let i = 0; i <= n - i - 1; i++) {
      if (i === n - i - 1 && k > 0) {
        palindrome.push('9');
        continue;
      }
      const count9 = [s[i], s[n - i - 1]].filter(x => x === '9').length;
      // console.log('i, n-i-1', i, n-i-1);
      // console.log('k, mismatches, count9', k, mismatches, count9);
      const mismatchCount = s[i] === s[n - i - 1];

      if (k - 1 - count9 - mismatchCount >= mismatches) {
        palindrome.push('9');
        k -= 2 - count9;
        if (s[i] !== s[n - i - 1]) {
          mismatches -= 1;
        }
      } else {
        palindrome.push(Math.max(s[i], s[n - i - 1]));
        if (s[i] !== s[n - i - 1]) {
          k -= 1;
          mismatches -= 1;
        }
      }
    }

    if (n % 2 === 0) {
      return palindrome.join('') + [...palindrome].reverse().join('');
    } else {
      const last = palindrome.pop();
      return palindrome.join('') + last + [...palindrome].reverse().join('');
    }
  }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    const s = readLine();

    let result = highestValuePalindrome(s, n, k);

    ws.write(result + "\n");

    ws.end();
}
