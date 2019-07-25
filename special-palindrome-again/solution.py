#!/bin/python3

import math
import os
import random
import re
import sys

'''
Note that a special substring can be defined recursively as:
    aXa
where 'X' is another special substring, and 'a' is a letter that is the
same.

Strategy: Per-letter expansion

For each letter, see how far you can expand the substring in both directions.
Repeat for two-letter base substrings. On can expand the whole string (length n)
for each character (n of them).

Time: O(n^2)
Space: O(n)

Note: answer is at most O(n^2). We would need to not simulate the problem in
order to go below O(n^2).

Strategy: Dynamic programming

Let L(i, j) denote the number of special substrings between i and j.
    L(i, j) = L(i + 1, j) + L(i, j - 1) - L(i + 1, j - 1) (to avoid overcount)
              + 1 (if a[i] === a[j] and a[i + 1:j - 1] is a substring)

Keep two DP arrays, one for whether something is a substring. Does this work?
Since size of this is up to O(n^2)...

Can't think of better solution, but is it enough to add some optimization
for the case of long single-letter runs? For runs of length k, add some # of
substrings, then treat the entire run as a single letter.

----------------------------------

OH. All the characters except middle one must be the SAME. This means, after
accounting for consecutive runs, substrings are at most length 2 on each side.
Also, even-lettered palindromes can't have more than one letter type because of
this rule.

New solution:
-- keep track of last run length
-- at the end of a run, add consecutive run count
-- on new letter, check if next letter is same as current new letter. If it is,
start new run. If it's not, do a backwards palindrome check as you advance
forward in the run.
'''

def consecutiveRunCount(length):
    return length * (length + 1) // 2

# Complete the substrCount function below.
def substrCount(n, s):
    totalCount = 0

    # preprocess to remove consecutive runs
    newS = []
    currentChar = None
    currentCharCount = 1
    for char in s:
        if currentChar is None:
            currentChar = char
        elif currentChar == char:
            currentCharCount += 1
        else:
            totalCount += consecutiveRunCount(currentCharCount)
            newS.append(currentChar)
            currentChar = char
            currentCharCount = 1
    totalCount += consecutiveRunCount(currentCharCount)
    newS.append(currentChar)

    # expand for single palindrome
    for i, char in enumerate(newS):
        if i - 1 < 0 or i + 1 >= len(newS):
            continue
        if newS[i - 1] == newS[i + 1]:
            totalCount += 1

    # expand for double palindrome

    return totalCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
