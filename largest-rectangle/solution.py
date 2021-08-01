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
  Actually though the optimal solution involves using a stack, not a heap.

  Maintain a stack of the currently partially started rectangles. Whenever we
  see a height lower than the latest starts, continue ending rectangle until all
  the rectangles in the stack are no longer lower than the current height.
  '''
  heights = heights + [0]
  area = 0
  positions = [] # positions represents the current list of partially started rectangles
  i = 0
  while i < len(heights):
    if not positions or heights[i] >= heights[positions[-1]]:
      # increase: start a new rectangle
      positions.append(i)
      i += 1
    else:
      # decrease: end a previously started rectangle
      # NOTE: whenever we decrease, we don't calculate the currently started
      # rectangle.
      # As an example:
      # heights:   5 12 11 7
      #                    ^
      # positions: 0  1
      # we are computing the rectangle from 12-11 here.
      prevPos = positions.pop()
      area = max(area, heights[prevPos] * (i - 1 - positions[-1] if positions else i))
  return area


  #
  # for i, height in enumerate(heights):
  #   print('positions', positions)
  #   print('i, h', i, height)
  #   print('area', area)
  #   while height < heights[positions[-1]]: # 10 < 11
  #     print(height, 'is <', heights[positions[-1]], 'popping...')
  #     prevPos = positions.pop()
  #     prevHeight = heights[prevPos]
  #     area = max(area, prevHeight * (i - prevPos))
  #   if height > heights[positions[-1]]:
  #     positions.append(i)
  # while positions:
  #   print('positions', positions)
  #   prevPos = positions.pop()
  #   prevHeight = heights[prevPos]
  #   print('area', area)
  #   print('prevPos, prevHeight', prevPos, prevHeight)
  #   area = max(area, prevHeight * (len(heights) - prevPos))
  # print('area final', area)
  # return area

def largestRectangleHeap(heights):
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
