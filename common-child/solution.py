#!/bin/python3

import math
import os
import random
import re
import sys

import pprint

# Complete the commonChild function below.
def commonChild(s1, s2):
    '''
    Strategy:

    Construct directed "graph" where letters are vertices and edges are whether
    a letter follows another in the sequence of letters. Size of graph is at
    most O(n) letters and O(n^2) connections.

    Search one graph and match the other. For each path in graph, traverse
    other graph to find matching child string. Each letter in first graph is
    visited only once???

    fuck that DP it

    Let L(i, j) be the longest common child between strings A and B.

    L(i, j) = max( L(i - 1, j - 1) + 1 if A[i] == B[j],
                   L(i - 1, j), L(i, j - 1) )
    '''
    '''
    L = [[0] * (len(s2) + 1) for _ in xrange(len(s2) + 1)]
    print 'test'
    for i in xrange(1, len(s1) + 1):
        if i % 100 == 0:
            print 'i, j', i, j
        for j in xrange(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                L[i][j] = max(L[i][j], 1 + L[i - 1][j - 1])
            L[i][j] = max(L[i][j], L[i - 1][j], L[i][j - 1])
            # print i, j, L[i - 1][j - 1]
            # pprint.pprint(L)
    return L[len(s1)][len(s2)]
    '''
    L = [[0] * (len(s2) + 1) for _ in xrange(2)]
    # print 'test'
    for i in xrange(1, len(s1) + 1):
        # if i % 100 == 0:
        #     print 'i, j', i, j
        for j in xrange(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                L[1][j] = max(L[1][j], 1 + L[0][j - 1])
            L[1][j] = max(L[1][j], L[0][j], L[1][j - 1])
            # print i, j, L[i - 1][j - 1]
        # pprint.pprint(L)
        # print L
        L[0], L[1] = L[1], [0] * (len(s2) + 1)
    return L[0][len(s2)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
