#!/bin/python3

import math
import os
import random
import re
import sys

import bisect

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
  '''
  Algorithm: use prefix sums, and store them in a sorted data structure.

  First, notice that a contiguous sum in (i, j) is equivalent to
    sum(0, j) - sum(0, i).
  Using this, we can compute contiguous sums using two prefix sums. We would
  like to find:
    max( (p[i] - p[j]) % m ), j < i
  where p[i] is the prefix sum at an index i.

  Doing this naively, however, would still yield an O(N^2) algorithm as we
  iterate through all possible pairs (i, j). However, notice that for a
  particular p[i], we would like to find the smallest p[j] larger than p[i] that
  we have already seen (ie. with j < i). We can do this by iterating through the
  array and use a sorted data structure like a self-balancing tree to retrieve
  the smallest p[j] greater than p[i] in O(log n) time. Unfortunately, since
  we're doing this in Python, for now we're just using `bisect`, for which
  insertion time is O(n). Let's hope this passes. If not, implementing that
  self-balancing sorted data structure will allow this algorithm to achieve O(N
  log N) time.
  '''
  max_, p_i = 0, 0
  # NOTE: you can consider `prefix` as an array with elements p[i] as above.
  # However, in practice, we skip that step and directly store prefixes in a
  # sorted data structure.
  prefix = []
  for i, a_i in enumerate(a):
    p_i = (a_i + p_i) % m
    max_ = max(max_, p_i % m)
    j = bisect.bisect_right(prefix, p_i)
    if j < len(prefix):
      # prefix[j] is the smallest prefix sum larger than p_i
      max_ = max(max_, (p_i - prefix[j]) % m)
    bisect.insort_left(prefix, p_i)
  return max_

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  q = int(input().strip())

  for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = maximumSum(a, m)

    fptr.write(str(result) + '\n')

  fptr.close()
