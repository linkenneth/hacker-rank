#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
  counter = defaultdict(lambda: [])
  for i, c in enumerate(cost):
    counter[c].append(i + 1)

  for c, indices in counter.items():
    if c == money - c:
      if len(indices) == 2:
        return [min(indices), max(indices)]
      elif len(indices) > 2:
        raise 'wtf'
    elif money - c in counter:
      indices = [indices[0], counter[money - c][0]]
      return [min(indices), max(indices)]

def whatFlavors1(cost, money):
  '''
  Seems to standard 2SUM. One solution is to sort, then manipulate two pointers.
  O(T * (N log N)) time. Another is to use a counter.
  '''
  sorted_costs = sorted(enumerate(cost), key=lambda x: x[1])
  i, j = 0, len(sorted_costs) - 1
  while i != j:
    ii, si, ij, sj = *sorted_costs[i], *sorted_costs[j]
    if si + sj == money:
      return list(sorted([ii + 1, ij + 1]))
    elif si + sj < money:
      i += 1
    else:
      j -= 1

if __name__ == '__main__':
  t = int(input().strip())

  for t_itr in range(t):
    money = int(input().strip())

    n = int(input().strip())

    cost = list(map(int, input().rstrip().split()))

    ii, ij = whatFlavors(cost, money)
    print(f'{ii} {ij}')
