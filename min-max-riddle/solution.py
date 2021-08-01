#!/bin/python3

# TODO: implement the stack O(N) version

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

Domination windows:
Let us say that i dominates a contiguous range of n values if it's lower than
all n of its neighboring values. This means that i will show up as a min window
when considering window sizes of up to size n. We want to find the largest i
such that it domaintes other numbers in a window of size n. Now how to find this
efficiently? If we iterate through each i and compare it to its n neighbors,
that will also be O(N^2) time.

Start with lowest number and 1-dimensional flood fill. This will take O(N^2)
time in the worst case though.

However, you don't actually have to perform the flood fill. Instead, we can just
use the coordinates of lower numbers and perform something like binary search
to find the closest coordinates to a given coordinate in O(log N) time.

Overall this means that we iterate through each number, starting from the
lowest, and perform O(log N) time binary searches to find the boundaries over
which this element i dominates. Total time is O(N log N).
'''

import math
import os
import random
import re
import sys

from collections import defaultdict
from heapq import heappush, heappop
from bisect import insort_left

# Complete the riddle function below.
def riddle(lst):
  '''
  Holy fuck.

  Better summary than above of what's happening:

  Define an value `v` in the list to dominate a range of size `n`, including `v`
  itself, if `v` is smaller than all other numbers in this contiguous range.
  Define `v`'s "dominating window" to be the largest such range. If `v` has a
  dominating window of size `n`, then it must show up as a value when we take
  minimums of size `w`. Therefore, to find the maximum of all such minimum
  windows, we only need to find the maximum `v` which dominates a range of size
  `n` or greater, for each `n` between 1 and `N`.

  To do this, the naive algorithm is to, for each number, flood fill in each
  direction until you hit a number smaller than itself. However, we can instead
  start with the smallest number, and keep a list of indices which we have
  already processed, that we know is smaller than the number we're processing.
  Using binary search, we can find the interval indices in which the current
  index lies, and find the bounding interval in O(log N) time. Repeat for each
  of `n` numbers for a total time complexity of O(N log N).

  Finally, for each window size `w`, find the maximum `v` that dominates a range
  of size `n` or larger.

  It seems like this is not the best solution though. There is a O(N) solution
  using stacks.
  '''
  max_by_w_size = { w: -float('inf') for w in range(1, len(lst) + 1) }
  # note that bounding_indices are indexes into len(lst), not values themselves
  bounding_indices = [-1, len(lst)]
  sorted_lst = sorted(enumerate(lst), key=lambda x: x[1])
  for i, value in sorted_lst:
    # note that l_index and r_index are indices to the bounding indices
    r_index = bsearch(bounding_indices, i)
    l_index = r_index - 1
    l_point = bounding_indices[l_index]
    r_point = bounding_indices[r_index]
    # (l_point + 1, r_point) defines a "dominating window" for `value`
    w = r_point - (l_point + 1)
    assert w > 0
    max_by_w_size[w] = max(max_by_w_size[w], value)
    insort_left(bounding_indices, i)

  m = -float('inf')
  maxes = []
  for w in reversed(range(1, len(lst) + 1)):
    m = max(m, max_by_w_size[w])
    maxes.append(m)
  return reversed(maxes)

def bsearch(lst, target):
  i, j = 0, len(lst)
  while i < j:
    mid = (i + j) // 2
    if lst[mid] == target:
      return mid + 1 # insert on the right side of the same number, not that it should matter?
    elif lst[mid] < target:
      i = mid + 1
    else:
      j = mid
  return i

def riddle_dp(arr):
  '''
  Too slow to pass large test cases. See `riddle`.
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
