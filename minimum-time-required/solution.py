#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the minTime function below.
def minTime(machines, goal):
  '''
  Method: first reverse binary search to find rough order of magnitude of days,
  then binary search as usual.
  '''
  counter = Counter(machines)
  time, total_output = 0.5, 0
  while total_output < goal:
    time = int(2 * time)
    total_output = getTotalOutput(time, counter)
  low, hi = time // 2, time
  while low < hi:
    mid = (low + hi) // 2
    total_output = getTotalOutput(mid, counter)
    if total_output == goal:
      # at this point mid is not necessarily the lowest possible time
      # at which we reach the goal. Need to linear search backwards as well.
      hi = mid
    elif total_output < goal:
      low = mid + 1
    else:
      hi = mid - 1
  return low

def getTotalOutput(time, counter):
  return sum(
    (time // cycle_time) * output for cycle_time, output in counter.items()
  )

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  nGoal = input().split()

  n = int(nGoal[0])

  goal = int(nGoal[1])

  machines = list(map(int, input().rstrip().split()))

  ans = minTime(machines, goal)

  fptr.write(str(ans) + '\n')

  fptr.close()
