#!/bin/python

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    '''
    Let L(i) denote the number of ways Davis can climb a staircase of height i.

    L(i) = L(i - 1) + L(i - 2) + L(i - 3)
    '''
    L = {}
    L[-3] = 0
    L[-2] = 0
    L[-1] = 0
    L[0] = 0
    L[1] = 1
    L[2] = L[1] + 1
    L[3] = L[2] + L[1] + 1

    for i in xrange(4, n + 1):
        L[i] = L[i - 1] + L[i - 2] + L[i - 3]
    #     print 'i', i, 'L[i]', L[i]
    # print L
    return L[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(raw_input())

    for s_itr in xrange(s):
        n = int(raw_input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
