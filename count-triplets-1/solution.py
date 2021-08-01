#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
  singlets = Counter()
  doublets = Counter()
  triplets = Counter()
  for i in reversed(arr):
    j, k = i * r, i * r * r
    triplets[i] += doublets[j] # 1-5-25 += count(5-25)
    doublets[i] += singlets[j] # 1-5 += count(5)
    singlets[i] += 1
  return sum(triplets.values())

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  nr = input().rstrip().split()

  n = int(nr[0])

  r = int(nr[1])

  arr = list(map(int, input().rstrip().split()))

  ans = countTriplets(arr, r)

  fptr.write(str(ans) + '\n')

  fptr.close()
