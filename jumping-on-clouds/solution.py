#!/bin/python3

import math
import os
import random
import re
import sys

CUMULUS = 0
THUNDERHEAD = 1

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    '''
    Let L(i) denote the minimum number of steps required to reach the end.

        L(i) = min(1 + L(i + 1), 1 + L(i + 2))
             = 1 + min(L(i + 1), L(i + 2))
    '''
    L = {}
    L[len(c) - 1] = 0
    for i in reversed(range(len(c) - 1)):
        cloud = c[i]
        if cloud is CUMULUS:
            L[i] = 1 + min(
                L[i + 1] if i + 1 in L else math.inf,
                L[i + 2] if i + 2 in L else math.inf)
    return L[0]

'''
NOTE:
Even simpler is to notice that there is always a solution, and that it's always
better to jump two spaces than one. In that case, the greedy solution of always
trying to jump two spaces first, then one space if not possible, will work.
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
