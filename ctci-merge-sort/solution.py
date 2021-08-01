#!/bin/python3

# TODO: this is broken

import math
import os
import random
import re
import sys

from collections import defaultdict
from heapq import heappush, heappop

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(lst):
  '''
  Examples:

  Unsorted: 3 1 1 1 2 2 2 1 1 (14 swaps)
  Unsorted: 1 1 1 2 2 2 1 1 3 (6 swaps)
  Unsorted: 1 1 2 1 2 2 1 1 3 (7 swaps)
  Sorted:   1 1 1 1 1 2 2 2 3 (0 swaps)

  Unsorted: 7 5 3 1 (6 swaps)
  Sorted:   1 3 5 7 (0 swaps)

  Hypothesis: the number of inversions required is equal to the sum of the
  number of items smaller than the current item after it.

  Let V(i, n) be the number of items after the ith index less than n.

  TODO: runs?

  D(i) = D(i + 1) + 1
  '''
  items_by_coordinate = defaultdict(lambda: [])
  for i, item in enumerate(lst):
    heappush(items_by_coordinate[item], i)
  sorted_lst = sorted(lst)
  distance = 0
  for i, bucket in enumerate(sorted_lst):
    j = heappop(items_by_coordinate[bucket])
    distance += abs(j - i)
  assert distance % 2 == 0
  return int(distance / 2)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  t = int(input().strip())

  for t_itr in range(t):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countInversions(arr)

    fptr.write(str(result) + '\n')

  fptr.close()
