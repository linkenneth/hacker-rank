#!/bin/python

import math
import os
import random
import re
import sys

def dfs(grid, x, y):
    if not inBounds(grid, x, y):
        return 0
    elif (x, y) in visited:
        return 0
    elif grid[x][y] == 0:
        return 0

    # print 'dfs', x, y

    visited.add((x, y))

    size = 0
    for x1, y1 in neighbors(x, y):
        size += dfs(grid, x1, y1)
    return size + 1

def neighbors(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            yield (x + i, y + j)

def inBounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

visited = set()

# Complete the maxRegion function below.
def maxRegion(grid):
    maxSize = 0
    for x, row in enumerate(grid):
        # print row
        for y, value in enumerate(row):
            if value == 0:
                continue
            elif (x, y) in visited:
                continue
            size = dfs(grid, x, y)
            # print 'size', size
            maxSize = max(maxSize, size)
    return maxSize

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    m = int(raw_input())

    grid = []

    for _ in xrange(n):
        grid.append(map(int, raw_input().rstrip().split()))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
