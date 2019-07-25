#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    '''
    Strategy: Parse into events / Mountain-valley

    Note that these intervals can be thought of as two events, one which
    increases the current value by k, and the other which decreases the current
    value by k. Thus, O(m) intervals creates O(2m) events. We can proceed
    through the events in sorted order (O(m log m) for sorting) and simulate
    the array in O(m log m) time.

    Time: O(m log m)
    Space: O(m)

    NOTE: From editorials, you can think of the ith element in this array as
    the prefix sum of elements 1 to i.
    '''
    # preprocess queries into a series of "increase" and "decrease" events at
    # beginning and end of intervals
    events = []
    for a, b, k in queries:
        events.append((a, k))
        events.append((b + 1, -k))
    events.sort()

    # iterate over events and keep track of global max
    prevI = 0
    prevMax = 0
    current = 0
    for i, k in events:
        # print(i, k, current, prevMax, prevI)
        if prevI != i and current > prevMax:
            prevMax = current
            prevI = i
        current += k

    return prevMax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
