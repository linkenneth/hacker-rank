#!/bin/python

'''
Reflection:

Some bullshit math calculations. Not hard at all just need to find how to
represent diagonals correctly, and to find the bounding range for these
diagonals.
'''

import math
import os
import random
import re
import sys

def findD1Bounds(n, row, column):
    '''
    Given the row and column positions of the queen, find bounding pseudo-
    obstacles that can be considered "bounds" on the board. Returned
    value is row-wise coordinate.
    '''
    d1_low = row - min(row, column)
    d1_high = row + n + 1 - max(row, column)
    return d1_low, d1_high

def findD2Bounds(n, row, column):
    '''
    Returned value is column-wise coordinate.
    '''
    ordinal = row + column
    d2_low = max(ordinal - n - 1, 0)
    d2_high = min(n + 1, ordinal)
    return d2_low, d2_high

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # print obstacles

    queen = (r_q, c_q)
    row_low, row_high = 0, n + 1
    column_low, column_high = 0, n + 1

    d1_low, d1_high = findD1Bounds(n, r_q, c_q)
    d2_low, d2_high = findD2Bounds(n, r_q, c_q)
    # print 'd1', d1_low, d1_high
    # print 'd2', d2_low, d2_high
    for obstacle in obstacles:
        r_o, c_o = obstacle
        if isSameRow(queen, obstacle):
            # print 'same row', queen, obstacle
            if c_o < c_q:
                column_low = max(column_low, c_o)
            elif c_q < c_o:
                column_high = min(column_high, c_o)
        if isSameColumn(queen, obstacle):
            # print 'same column', queen, obstacle
            if r_o < r_q:
                row_low = max(row_low, r_o)
            elif r_q < r_o:
                row_high = min(row_high, r_o)
        if isSameD1(queen, obstacle):
            # print 'same d1', queen, obstacle
            if r_o < r_q:
                d1_low = max(d1_low, r_o)
            elif r_q < r_o:
                d1_high = min(d1_high, r_o)
        if isSameD2(queen, obstacle):
            # print 'same d2', queen, obstacle
            if c_o < c_q:
                d2_low = max(d2_low, c_o)
            elif c_q < c_o:
                d2_high = min(d2_high, c_o)

    # print column_low, column_high
    # return (
    #     column_high - column_low - 2, # same row
    #     row_high - row_low - 2, # same column
    #     d1_high - d1_low - 2, # same d1
    #     d2_high - d2_low - 2, # same d2
    # )
    return (
        column_high - column_low - 2 + # same row
        row_high - row_low - 2 + # same column
        d1_high - d1_low - 2 + # same d1
        d2_high - d2_low - 2 # same d2
    )

def isSameRow(a, b):
    return a[0] == b[0]

def isSameColumn(a, b):
    return a[1] == b[1]

def isSameD1(a, b):
    '''
    D1 refers to the diagonal going from the bottom left to the top right.
    '''
    return a[0] - a[1] == b[0] - b[1]

def isSameD2(a, b):
    '''
    D2 refers to the diagonal going from the top left to the bottom right.
    '''
    return a[0] + a[1] == b[0] + b[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = raw_input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in xrange(k):
        obstacles.append(map(int, raw_input().rstrip().split()))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
