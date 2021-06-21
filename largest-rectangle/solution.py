#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(heights):
  '''
  This is the standard skyline problem. Different possible solutions here:
  (1) Check the O(N^2) set of possible starting points (p0) and ending points
  (p1) of the rectangle. Time: O(N^2).
  (2) Notice that a low height implies that all previous possible rectangles with
  height higher than this height must end here. Therefore, use a priority queue
  (or heap) and pop all the heights that are greater than this one. Compute the
  area of that rectangle and compare it to the max. This is the method used
  here. Time: O(N log N), since each item is pushed and popped exactly once, and
  O(log N) amortized cost to maintain heap order.
  '''
  heap = []
  largest = 0
  for p1, h1 in enumerate(heights + [0]):
    min_p = float('inf')
    while len(heap) > 0 and heap[0][2] > h1:
      _, p0, h0 = heappop(heap)
      area = (p1 - p0) * h0
      largest = max(largest, area)
      min_p = min(min_p, p0)
    heappush(heap, (-h1, min(min_p, p1), h1))
  return largest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
