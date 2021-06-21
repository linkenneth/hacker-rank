#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
  '''
  Greedy algorithm: continue to remove the highest stack.
  '''
  cylinders = [list(reversed(h)) for h in [h1, h2, h3]]
  heights = [sum(h) for h in cylinders]
  while not all(h == heights[0] for h in heights):
    i = argmax(heights)
    height = cylinders[i].pop()
    heights[i] -= height
  return heights[0]

def argmax(lst):
  return max(enumerate(lst), key=lambda x: x[1])[0]

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  first_multiple_input = input().rstrip().split()

  n1 = int(first_multiple_input[0])

  n2 = int(first_multiple_input[1])

  n3 = int(first_multiple_input[2])

  h1 = list(map(int, input().rstrip().split()))

  h2 = list(map(int, input().rstrip().split()))

  h3 = list(map(int, input().rstrip().split()))

  result = equalStacks(h1, h2, h3)

  fptr.write(str(result) + '\n')

  fptr.close()
