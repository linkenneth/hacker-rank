#!/bin/python3
'''
Naive: O(N^3) or sum_{k=1...N}( O(N^2 (N-K)) )
  for each size N
    for each window of size N in the array
      traverse the window to find the max

Naive with heap: O(N^2 log N)
  for each size N O(N)
    traverse array and accumulate window of size N O(N log N)
      find max O(1)

DP:
Notice that min(W, p), the min size for window of size W and at position p, is
equal to min(min(W - 1, p), min(W - 1, p + 1)). Therefore, DP with these
tables can reduce the size of the problem to O(W^2) ~= O(N^2). Is this good
enough? No.
'''

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
  pass

def riddle_dp(arr):
  '''
  Too slow to pass large test cases. See riddle.
  '''
  N = len(arr)
  min_w = {} # dict of (win_size, win_position) to minimum
  for i, el in enumerate(arr):
    min_w[(1, i)] = el
  for w in range(2, len(arr) + 1):
    for i in range(N - w + 1):
      # print('w, i', w, i)
      min_w[(w, i)] = min(min_w[(w - 1, i)], min_w[(w - 1, i + 1)])
  # print('min_w', min_w)
  return [max(min_w[(w, i)] for i in range(N - w + 1)) for w in range(1, len(arr) + 1)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
