#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    '''
    Let L(i) be the max sum that can be attained with elements arr[i:].

    L(i) = max(arr[i] + L(i + 2), L(i + 1))
    '''
    print 'maxSubsetSum', arr
    L = [0] * (len(arr) + 2)
    L[-1] = 0
    L[-2] = 0

    for i in xrange(len(arr) - 1, -1, -1):
        L[i] = max(arr[i] + L[i + 2], L[i + 1])
    print L
    return L[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
