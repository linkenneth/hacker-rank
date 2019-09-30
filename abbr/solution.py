#!/bin/python

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    '''
    This seems like sort of a trick problem. Actually the problem is basically
    to see find the sequence B in A, disregarding capitalization. Take a greedy
    approach and always match the first letter that matches.
    DOESNT WORK. need to consider instancesl ike:

    gGi
    GI

    or

    gIi
    GI

    Let L(i, j) be whether the subproblem a[i:], b[j:] can be solved.

    L(i, j) = L(i + 1, j + 1) if a[i] == b[i] and both are uppercase
            = any(L(i + 1, j + 1), L(i + 1, j)) if a[i] == b[i]
                                                but a[i] is lowercase
            = False if a[i] != b[i] and a[i] is uppercase
            = L(i + 1, j) if a[i] != b[i] and a[i] is lowercase
    '''
    # print a, b
    L = [[None] * (len(b) + 1) for _ in xrange(len(a) + 1)]

    for i in xrange(len(a), -1, -1):
        for j in xrange(len(b), -1, -1):
            if j == len(b) and i == len(a):
                L[i][j] = True
            elif i == len(a):
                L[i][j] = False
            elif j == len(b):
                L[i][j] = a[i].islower() and L[i + 1][j]
            elif a[i] == b[j]:
                L[i][j] = L[i + 1][j + 1]
            elif a[i].upper() == b[j]:
                L[i][j] = any((L[i + 1][j + 1], L[i + 1][j]))
            elif a[i].isupper():
                L[i][j] = False
            elif a[i].islower():
                L[i][j] = L[i + 1][j]
            else:
                assert 0
            # print 'i, j', i, j, L[i][j]
    # print L
    return 'YES' if L[0][0] else 'NO'

    # i = 0
    # j = 0
    # while i < len(a):
    #     # print 'i, j', i, j, a[i], b[j]
    #     if (j < len(b) and
    #         (a[i] == b[j] or
    #          ord(a[i]) - ord('a') == ord(b[j]) - ord('A'))):
    #         i += 1
    #         j += 1
    #     elif a[i].isupper():
    #         return 'NO'
    #     else:
    #         i += 1
    # return 'YES' if j == len(b) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
